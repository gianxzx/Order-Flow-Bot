import nextcord
from nextcord import Interaction, Embed
from nextcord.ext import commands
from src.database.supabase import supabase

bot = commands.Bot(command_prefix="!")

@bot.slash_command(name="chef-stats", description="Show your chef stats")
async def chef_stats(interaction: Interaction):
    user_id = str(interaction.user.id)

    # Fetch user stats from Supabase
    result = supabase.table("users").select("*").eq("id", user_id).execute()

    if not result.data:
        await interaction.response.send_message("❌ No stats found for you.", ephemeral=True)
        return

    user_data = result.data[0]
    points = user_data.get("points", 0)
    total_successful_orders = user_data.get("total_successful_orders", 0)

    embed = Embed(
        title=f"👨‍🍳 Chef Stats: {interaction.user.display_name}",
        description=f"Total Successful Orders: {total_successful_orders}\nPoints Earned: {points}",
        color=0x1abc9c
    )

    await interaction.response.send_message(embed=embed, ephemeral=True)
