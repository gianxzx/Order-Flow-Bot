import "dotenv/config";

export const ENV = {
  DISCORD_TOKEN: process.env.DISCORD_TOKEN,
  CLIENT_ID: process.env.CLIENT_ID,
  GUILD_ID: process.env.GUILD_ID,

  WEBHOOK_ID: process.env.WEBHOOK_ID,
  WEBHOOK_TOKEN: process.env.WEBHOOK_TOKEN,

  CHEF_ROLE_IDS: process.env.CHEF_ROLE_IDS?.split(","),
  ADMIN_ROLE_IDS: process.env.ADMIN_ROLE_IDS?.split(","),

  ORDER_CATEGORY_ID: process.env.ORDER_CATEGORY_ID,
  DISCOUNT_CHANNEL_ID: process.env.DISCOUNT_CHANNEL_ID,

  SUPABASE_URL: process.env.SUPABASE_URL,
  SUPABASE_ANON_KEY: process.env.SUPABASE_ANON_KEY
};
