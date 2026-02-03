import { EmbedBuilder } from "discord.js";

// Common embed builders
export const createOrderEmbed = (title, description, color = "Blue") => {
  return new EmbedBuilder()
    .setTitle(title)
    .setDescription(description)
    .setColor(color)
    .setTimestamp();
};
