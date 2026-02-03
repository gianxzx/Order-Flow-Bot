import asyncio
from nextcord.ext import commands
from src.database.supabase import supabase
from src.config.env import ADMIN_ROLE_IDS

bot = commands.Bot(command_prefix="!")  # Replace if you import main bot

@bot.command(name="close")
async def close_order(ctx):
    author = ctx.author

    # Check if author is admin or chef role (simplified, add your role check)
    if not any(role.id in ADMIN_ROLE_IDS for role in author.roles):
        await ctx.send("❌ You are not allowed to close this order.")
        return

    # Fetch order info from channel name or pinned message (simplified example)
    order_id = ctx.channel.name.split("order-")[-1]

    # Example: fetch customer_id from channel topic or message (adapt to your bot logic)
    customer_id = 1234567890  # Placeholder

    # Update Supabase points for chef
    supabase.table("users").update({"points": 1}).eq("id", author.id).execute()
    # Update Supabase points for customer
    supabase.table("users").update({"points": 1}).eq("id", customer_id).execute()

    # Send final completion message
    await ctx.send(
        f"✅ Order {order_id} completed!\n"
        f"👨‍🍳 Chef: {author.mention}\n"
        f"🎯 Points awarded: 1 to chef and customer <@{customer_id}>"
    )

    # Delete the channel after 5 seconds
    await asyncio.sleep(5)
    await ctx.channel.delete()
