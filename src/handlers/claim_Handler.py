import nextcord
from nextcord import Interaction, ChannelType, PermissionOverwrite
from nextcord.ui import View
from src.config.env import ORDER_CATEGORY_ID
from src.utils.permissions import create_ticket_permissions
from src.utils.order_id import generate_order_id

async def claim_callback(interaction: Interaction, order_content: str, customer_id: int):
    guild = interaction.guild
    chef = interaction.user

    # Delete original embed message
    await interaction.message.delete()

    # Create private ticket channel
    overwrites = {
        guild.default_role: PermissionOverwrite(view_channel=False),
        chef: PermissionOverwrite(view_channel=True, send_messages=True),
        guild.get_member(customer_id): PermissionOverwrite(view_channel=True, send_messages=True)
    }

    category = guild.get_channel(ORDER_CATEGORY_ID)
    ticket_channel = await guild.create_text_channel(
        name=f"order-{chef.name}",
        category=category,
        overwrites=overwrites,
        type=ChannelType.text
    )

    # Post order details
    await ticket_channel.send(
        f"📌 **Order ID:** {generate_order_id()}\n"
        f"👨‍🍳 **Claimed by:** {chef.mention}\n"
        f"📝 **Order Details:** {order_content}\n"
        f"📢 <@{customer_id}>, your order has been claimed!"
    )

    # Respond to chef
    await interaction.response.send_message(f"✅ Order claimed! Check {ticket_channel.mention}", ephemeral=True)
