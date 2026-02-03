import { SlashCommandBuilder } from "discord.js";
import { ENV } from "../config/env.js";
import { supabase } from "../database/supabase.js";

export const adjustPoints = {
  data: new SlashCommandBuilder()
    .setName("adjust-points")
    .setDescription("Admin: Adjust points for a customer or chef")
    .addUserOption(option => 
      option.setName("user")
            .setDescription("User to adjust")
            .setRequired(true))
    .addIntegerOption(option =>
      option.setName("points")
            .setDescription("New points value")
            .setRequired(true))
    .addStringOption(option =>
      option.setName("reason")
            .setDescription("Optional reason for adjustment")
            .setRequired(false)),

  async execute(interaction) {
    const userId = interaction.user.id;

    // Admin check
    if (!ENV.ADMIN_ROLE_IDS.includes(userId)) {
      return interaction.reply({ content: "You are not allowed to use this command.", ephemeral: true });
    }

    const targetUser = interaction.options.getUser("user");
    const newPoints = interaction.options.getInteger("points");
    const reason = interaction.options.getString("reason") || "No reason provided";

    try {
      // Update points in Supabase (assuming a 'points' column in 'users' table)
      const { error } = await supabase
        .from("users")
        .update({ points: newPoints })
        .eq("id", targetUser.id);

      if (error) throw error;

      await interaction.reply({
        content: `✅ Points for ${targetUser.tag} updated to ${newPoints}. Reason: ${reason}`,
        ephemeral: true
      });
    } catch (err) {
      console.error("Adjust points error:", err);
      await interaction.reply({ content: "Failed to adjust points.", ephemeral: true });
    }
  }
};
