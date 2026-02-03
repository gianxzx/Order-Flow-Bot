import nextcord
from nextcord import Interaction
from src.handlers.claim_handler import claim_callback
from src.handlers.close_handler import close_order  # Optional if needed
from src.config.constants import CLAIM_BUTTON, DECLINE_BUTTON

from index import bot  # use the bot instance from index.py

@bot.event
async def on_interaction(interaction: Interaction):
    # Handle only component interactions (buttons)
    if not interaction.type.name == "component":
        return

    custom_id = interaction.data.get("custom_id")

    if custom_id == CLAIM_BUTTON:
        # You need to pass order content & customer_id to claim_callback
        # Example placeholders, replace with actual logic
        order_content = "Sample order content"
        customer_id = 1234567890
        await claim_callback(interaction, order_content, customer_id)

    elif custom_id == DECLINE_BUTTON:
        # Delete the original embed message to decline
        await interaction.message.delete()
        await interaction.response.send_message("❌ Order declined!", ephemeral=True)
