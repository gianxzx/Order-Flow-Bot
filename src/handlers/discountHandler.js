import { client } from "../bot.js";
import { ENV } from "../config/env.js";
import { supabase } from "../database/supabase.js";

// Handles /discount command for chefs
export const initDiscountHandler = () => {
  client.on("interactionCreate", async (interaction) => {
    if (!interaction.isChatInputCommand()) return;
    if (interaction.commandName !== "discount") return;

    const { options } = interaction;

    try {
      const orderId = options.getString("order_id");
      const amount = options.getNumber("discount_amount");
      const customerId = options.getUser("customer").id;
      const reason = options.getString("reason") || "No reason provided";

      // TODO: Fetch original order price from Supabase
      const originalPrice = 100; // Placeholder for now
      const discountedPrice = originalPrice - amount;

      // Send text message to discount channel
      const discountChannel = await client.channels.fetch(ENV.DISCOUNT_CHANNEL_ID);
      const messageText = `
📢 Discount Applied
Order ID: ${orderId}
Customer: <@${customerId}>
Original Price: $${originalPrice}
Discount Amount: $${amount}
New Price: $${discountedPrice}
Reason: ${reason}
      `;

      await discountChannel.send({ content: messageText });

      // Ping the customer
      await discountChannel.send({ content: `<@${customerId}> You got a discount!` });

      await interaction.reply({ content: "Discount applied successfully!", ephemeral: true });
    } catch (err) {
      console.error("Discount handler error:", err);
      await interaction.reply({ content: "Failed to apply discount.", ephemeral: true });
    }
  });
};
