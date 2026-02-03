import nextcord
from nextcord import Interaction, Embed
from nextcord.ext import commands
from src.config.env import ADMIN_ROLE_IDS
from src.database.supabase import supabase

bot = commands.Bot(command_prefix="!")

@bot.slash_command(name="lbreset", description="Admin only: Reset all leaderboards")
async def lb_reset(interaction: Interaction):
    # Check if user is admin
    if not any(role.id in ADMIN_ROLE_IDS for role in interaction.user.roles):
        await interaction.response.send_message("❌ You are not allowed to use this command.", ephemeral=True)
        return

    # Reset customers
    supabase.table("users").update({"points": 0, "total_orders": 0, "total_successful_orders": 0}).execute()

    embed = Embed(
        title="♻️ Leaderboards Reset",
        description=f"Admin: {interaction.user.mention}\nAll customer and chef stats have been reset.",
        color=0xe74c3c
    )

    await interaction.response.send_message(embed=embed)
