import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")
GUILD_ID = int(os.getenv("GUILD_ID"))

WEBHOOK_ID = int(os.getenv("WEBHOOK_ID"))
WEBHOOK_TOKEN = os.getenv("WEBHOOK_TOKEN")

CHEF_ROLE_IDS = [int(x) for x in os.getenv("CHEF_ROLE_IDS").split(",")]
ADMIN_ROLE_IDS = [int(x) for x in os.getenv("ADMIN_ROLE_IDS").split(",")]

ORDER_CATEGORY_ID = int(os.getenv("ORDER_CATEGORY_ID"))
DISCOUNT_CHANNEL_ID = int(os.getenv("DISCOUNT_CHANNEL_ID"))

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
