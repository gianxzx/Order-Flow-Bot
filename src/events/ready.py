import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix="!")  # Replace with your main bot instance

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    print("🔹 Bot is ready and online!")

    # Optional: sync slash commands globally
    await bot.sync_application_commands()
    print("🌐 Slash commands synced.")
