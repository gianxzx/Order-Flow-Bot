import { client } from "../bot.js";
import { ENV } from "../config/env.js";
import { BUTTONS } from "../config/constants.js";
import { EmbedBuilder, PermissionFlagsBits } from "discord.js";
import { supabase } from "../database/supabase.js";

// Handles Claim & Decline button interactions
export const initClaimHandler = () => {
  client.on("interactionCreate", async (interaction) => {
    if (!interaction.isButton()) return;

    const { customId, channel, user } = interaction;

    // ===== CLAIM BUTTON =====
    if (customId === BUTTONS.CLAIM) {
      try {
        // Delete the original order embed
        await interaction.message.delete();

        // Create private order-ticket channel
        const ticketChannel = await channel.guild.channels.create({
          name: `order-${user.username}`,
          type: 0, // GUILD_TEXT
          parent: ENV.ORDER_CATEGORY_ID,
          permissionOverwrites: [
            {
              id: user.id, // claiming chef
              allow: [PermissionFlagsBits.ViewChannel, PermissionFlagsBits.SendMessages]
            },
            {
              id: interaction.guild.id, // everyone else
              deny: [PermissionFlagsBits.ViewChannel]
            }
          ]
        });

        // Post order details
        const embed = new EmbedBuilder()
          .setTitle("Order Claimed")
          .setDescription(`Chef: ${user}\nOrder ID: TBD`)
          .setColor("Green")
          .setTimestamp();

        await ticketChannel.send({ content: `<@customer_id_here>`, embeds: [embed] });

        // TODO: Insert order into Supabase with status 'claimed'

        await interaction.reply({ content: "Order claimed and private channel created!", ephemeral: true });
      } catch (err) {
        console.error("Claim handler error:", err);
      }
    }

    // ===== DECLINE BUTTON =====
    if (customId === BUTTONS.DECLINE) {
      try {
        await interaction.message.delete();
        await interaction.reply({ content: "Order declined.", ephemeral: true });
      } catch (err) {
        console.error("Decline handler error:", err);
      }
    }
  });
};
