import nextcord
from nextcord import Interaction, Embed
from nextcord.ext import commands
from src.config.env import ADMIN_ROLE_IDS
from src.database.supabase import supabase

bot = commands.Bot(command_prefix="!")

@bot.slash_command(name="adjust-points", description="Admin only: Adjust points for a user")
async def adjust_points(
    interaction: Interaction,
    target_user: nextcord.Member,
    new_points: int,
    reason: str = "No reason provided"
):
    # Check if user is admin
    if not any(role.id in ADMIN_ROLE_IDS for role in interaction.user.roles):
        await interaction.response.send_message("❌ You are not allowed to use this command.", ephemeral=True)
        return

    # Update Supabase
    supabase.table("users").update({"points": new_points}).eq("id", str(target_user.id)).execute()

    embed = Embed(
        title="✅ Points Adjusted",
        description=f"Admin: {interaction.user.mention}\n"
                    f"User: {target_user.mention}\n"
                    f"New Points: {new_points}\n"
                    f"Reason: {reason}",
        color=0xe67e22
    )

    await interaction.response.send_message(embed=embed)
