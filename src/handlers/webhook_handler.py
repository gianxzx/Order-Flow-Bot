import nextcord
from nextcord import Interaction, ButtonStyle, Embed
from nextcord.ui import Button, View
from src.config.env import CHEF_ROLE_IDS
from src.utils.order_id import generate_order_id

async def handle_webhook_message(message):
    # Only process webhook messages
    if message.webhook_id is None:
        return

    order_id = generate_order_id()
    embed = Embed(
        title=f"New Order - {order_id}",
        description=message.content,
        color=0x3498db
    )

    # Buttons
    claim_button = Button(label="Claim", style=ButtonStyle.green, custom_id="claim")
    decline_button = Button(label="Decline", style=ButtonStyle.red, custom_id="decline")

    view = View()
    view.add_item(claim_button)
    view.add_item(decline_button)

    # Send to orders channel (replace with your channel ID)
    orders_channel = message.guild.get_channel(ORDER_CATEGORY_ID)  # placeholder, replace with orders channel ID
    if orders_channel:
        await orders_channel.send(content=" ".join(f"<@{r}>" for r in CHEF_ROLE_IDS), embed=embed, view=view)
