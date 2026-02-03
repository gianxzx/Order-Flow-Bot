import { client } from "../bot.js";
import { ENV } from "../config/env.js";
import { BUTTONS } from "../config/constants.js";
import { generateOrderId } from "../utils/orderId.js";
import { ActionRowBuilder, ButtonBuilder, ButtonStyle, EmbedBuilder } from "discord.js";

// Listen for messages in the webhook channel
export const initWebhookHandler = () => {
  client.on("messageCreate", async (message) => {
    // Ignore bot messages
    if (message.author.bot) return;

    // Only process messages from the designated webhook
    if (message.webhookId !== ENV.WEBHOOK_ID) return;

    try {
      // Generate a unique order ID
      const orderId = generateOrderId();

      // Create embed for orders channel
      const embed = new EmbedBuilder()
        .setTitle(`New Order - ${orderId}`)
        .setDescription(message.content)
        .setColor("Blue")
        .setTimestamp();

      // Buttons: Claim / Decline
      const row = new ActionRowBuilder().addComponents(
        new ButtonBuilder()
          .setCustomId(BUTTONS.CLAIM)
          .setLabel("Claim")
          .setStyle(ButtonStyle.Success),
        new ButtonBuilder()
          .setCustomId(BUTTONS.DECLINE)
          .setLabel("Decline")
          .setStyle(ButtonStyle.Danger)
      );

      // Send embed + buttons to orders channel
      const ordersChannel = await client.channels.fetch(ENV.ORDER_CATEGORY_ID); // Replace with real orders channel ID if needed
      await ordersChannel.send({
        content: `<@&${ENV.CHEF_ROLE_IDS.join(">, <@&")}>`,
        embeds: [embed],
        components: [row]
      });

    } catch (err) {
      console.error("Webhook handler error:", err);
    }
  });
};
