import nextcord
from nextcord.ext import commands
from src.config.env import DISCORD_TOKEN, GUILD_ID
from src.handlers import webhook_handler, claim_handler, close_handler, discount_handler
from src.commands import customer_stats, chef_stats, adjust_points, lb_reset
from src.events import ready, message_create, interaction_create

# ----------------------
# Bot Setup
# ----------------------
intents = nextcord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ----------------------
# Load Events
# ----------------------
bot.add_listener(ready.on_ready)
bot.add_listener(message_create.on_message)

# interaction_create handles buttons
bot.add_listener(interaction_create.on_interaction)

# ----------------------
# Load Commands
# ----------------------
# Slash commands are already registered inside their files
# If needed, you can also manually add them:
# bot.add_application_command(customer_stats.customer_stats)
# bot.add_application_command(chef_stats.chef_stats)
# bot.add_application_command(adjust_points.adjust_points)
# bot.add_application_command(lb_reset.lb_reset)
# discount_handler has its own slash command

# ----------------------
# Run Bot
# ----------------------
print("🔹 Starting Discord Bot...")
bot.run(DISCORD_TOKEN)
