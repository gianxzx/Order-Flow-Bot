import random
import string

def generate_order_id():
    letters = ''.join(random.choices(string.ascii_uppercase, k=6))
    numbers = ''.join(random.choices(string.digits, k=4))
    return f"ORD-{letters}-{numbers}"
