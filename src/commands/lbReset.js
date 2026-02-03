import { SlashCommandBuilder } from "discord.js";
import { ENV } from "../config/env.js";
import { supabase } from "../database/supabase.js";

export const lbReset = {
  data: new SlashCommandBuilder()
    .setName("lbreset")
    .setDescription("Admin: Reset leaderboards for all users"),

  async execute(interaction) {
    const userId = interaction.user.id;

    // Admin check
    if (!ENV.ADMIN_ROLE_IDS.includes(userId)) {
      return interaction.reply({ content: "You are not allowed to use this command.", ephemeral: true });
    }

    try {
      // Reset all points to 0 in 'users' table
      const { error } = await supabase
        .from("users")
        .update({ points: 0 });

      if (error) throw error;

      await interaction.reply({ content: "✅ Leaderboards have been reset.", ephemeral: true });
    } catch (err) {
      console.error("Leaderboard reset error:", err);
      await interaction.reply({ content: "Failed to reset leaderboards.", ephemeral: true });
    }
  }
};
