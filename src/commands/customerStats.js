import { SlashCommandBuilder } from "discord.js";
import { supabase } from "../database/supabase.js";

export const customerStats = {
  data: new SlashCommandBuilder()
    .setName("customer-stats")
    .setDescription("Shows customer order stats"),

  async execute(interaction) {
    const userId = interaction.user.id;

    // Fetch stats from Supabase
    const { data: stats, error } = await supabase
      .from("orders")
      .select("*", { count: "exact" })
      .eq("customer_id", userId)
      .eq("status", "completed");

    if (error) return interaction.reply({ content: "Failed to fetch stats.", ephemeral: true });

    const points = stats.length; // assuming 1 point per order
    await interaction.reply({
      content: `📊 You have completed ${stats.length} orders and earned ${points} points.`
    });
  }
};
