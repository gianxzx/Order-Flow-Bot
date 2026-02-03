from nextcord import Embed

def order_embed(order_id: str, order_content: str):
    return Embed(
        title=f"New Order - {order_id}",
        description=order_content,
        color=0x3498db
    )

def completion_embed(order_id: str, chef_mention: str, customer_mention: str):
    return Embed(
        title=f"✅ Order Completed - {order_id}",
        description=f"👨‍🍳 Chef: {chef_mention}\n"
                    f"🎯 Customer: {customer_mention}\n"
                    f"🏆 Points awarded to both!",
        color=0x2ecc71
    )

def stats_embed(user_name: str, total_orders: int, points: int, is_chef=False):
    title = f"👨‍🍳 Chef Stats: {user_name}" if is_chef else f"📊 Stats: {user_name}"
    return Embed(
        title=title,
        description=f"Total Orders Completed: {total_orders}\nPoints: {points}",
        color=0x3498db
    )
