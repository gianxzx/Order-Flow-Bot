import { PermissionFlagsBits } from "discord.js";

// Helpers for channel permission overwrites
export const createTicketPermissions = (chefId, customerId, guildId) => [
  {
    id: chefId,
    allow: [PermissionFlagsBits.ViewChannel, PermissionFlagsBits.SendMessages]
  },
  {
    id: customerId,
    allow: [PermissionFlagsBits.ViewChannel, PermissionFlagsBits.SendMessages]
  },
  {
    id: guildId,
    deny: [PermissionFlagsBits.ViewChannel]
  }
];
