from nextcord import PermissionOverwrite

def create_ticket_permissions(guild, chef_member, customer_member):
    """
    Returns a dictionary of permission overwrites for a private ticket channel
    """
    overwrites = {
        guild.default_role: PermissionOverwrite(view_channel=False),
        chef_member: PermissionOverwrite(view_channel=True, send_messages=True),
        customer_member: PermissionOverwrite(view_channel=True, send_messages=True)
    }
    return overwrites
