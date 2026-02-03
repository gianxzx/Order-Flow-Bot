import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from src.config.env import DISCOUNT_CHANNEL_ID, SUPABASE_URL, SUPABASE_ANON_KEY
from src.database.supabase import supabase

bot = commands.Bot(command_prefix="!")

@bot.slash_command(name="discount", description="Apply a discount to a customer's order")
async def discount(
    interaction: Interaction,
    order_id: str,
    amount: float,
    customer_id: str,
    reason: str = "No reason provided"
):
    # Fetch original order price from Supabase (optional)
    order = supabase.table("orders").select("*").eq("order_id", order_id).execute()
    if not order.data:
        await interaction.response.send_message(f"❌ Order {order_id} not found.", ephemeral=True)
        return

    original_price = float(order.data[0]["total_price"])
    discounted_price = max(0, original_price - amount)

    # Send plain text message to discount channel
    guild = interaction.guild
    discount_channel = guild.get_channel(DISCOUNT_CHANNEL_ID)
    if discount_channel:
        await discount_channel.send(
            f"💰 Discount Applied!\n"
            f"Order ID: {order_id}\n"
            f"Customer: <@{customer_id}>\n"
            f"Original Price: {original_price}\n"
            f"Discounted Price: {discounted_price}\n"
            f"Reason: {reason}\n"
            f"Discount applied by: {interaction.user.mention}"
        )

    # Notify the customer
    await interaction.response.send_message(f"✅ Discount applied for <@{customer_id}>.", ephemeral=True)
