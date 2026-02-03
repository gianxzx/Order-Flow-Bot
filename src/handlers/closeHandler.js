import { client } from "../bot.js";
import { ENV } from "../config/env.js";
import { supabase } from "../database/supabase.js";
import { EmbedBuilder, PermissionFlagsBits } from "discord.js";

// Handles !close command in private ticket channels
export const initCloseHandler = () => {
  client.on("messageCreate", async (message) => {
    if (message.author.bot) return;
    if (!message.content.startsWith("!close")) return;

    const guild = message.guild;
    const channel = message.channel;

    try {
      // Check if user is claiming chef or admin
      const member = await guild.members.fetch(message.author.id);
      const isAdmin = ENV.ADMIN_ROLE_IDS.includes(member.id);
      // TODO: You will also check if this member is the claiming chef for this order

      if (!isAdmin /* && not claiming chef */) {
        return message.reply("You are not allowed to close this order.");
      }

      // TODO: Update order status to 'completed' in Supabase
      // TODO: Add 1 point to chef and customer

      // Send final embed
      const embed = new EmbedBuilder()
        .setTitle("Order Completed ✅")
        .setDescription("Points awarded to Chef and Customer")
        .setColor("Green")
        .setTimestamp();

      await channel.send({ embeds: [embed] });

      // Delete the channel after 10 seconds
      setTimeout(() => channel.delete().catch(() => {}), 10000);

    } catch (err) {
      console.error("Close handler error:", err);
    }
  });
};
