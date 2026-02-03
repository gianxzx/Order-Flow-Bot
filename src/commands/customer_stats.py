import nextcord
from nextcord import Interaction, Embed
from nextcord.ext import commands
from src.database.supabase import supabase

bot = commands.Bot(command_prefix="!")

@bot.slash_command(name="customer-stats", description="Show your customer stats")
async def customer_stats(interaction: Interaction):
    user_id = str(interaction.user.id)

    # Fetch user stats from Supabase
    result = supabase.table("users").select("*").eq("id", user_id).execute()

    if not result.data:
        await interaction.response.send_message("❌ No stats found for you.", ephemeral=True)
        return

    user_data = result.data[0]
    points = user_data.get("points", 0)
    total_orders = user_data.get("total_orders", 0)

    embed = Embed(
        title=f"📊 Stats for {interaction.user.display_name}",
        description=f"Total Orders Completed: {total_orders}\nPoints: {points}",
        color=0x3498db
    )

    await interaction.response.send_message(embed=embed, ephemeral=True)
