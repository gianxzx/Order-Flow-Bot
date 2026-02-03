import { Client, GatewayIntentBits, Partials } from "discord.js";
import { ENV } from "./config/env.js";

import "./events/ready.js";
import "./events/interactionCreate.js";
import "./events/messageCreate.js";

export const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent
  ],
  partials: [Partials.Channel]
});

client.login(ENV.DISCORD_TOKEN);
