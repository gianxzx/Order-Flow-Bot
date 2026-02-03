import nextcord
from nextcord.ext import commands
from src.config.env import ADMIN_ROLE_IDS
from src.handlers.close_handler import close_order  # Import your close handler function

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_message(message):
    # Ignore bots
    if message.author.bot:
        return

    # Handle !close command
    if message.content.lower().startswith("!close"):
        await close_order(message)  # Pass message to your handler
