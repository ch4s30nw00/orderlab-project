import numpy as np
a=100

def subtotal(unit_price: int, quantity: int) -> int:
    b=10
    if unit_price < 0 or quantity < 0:
        raise ValueError("negative input")
    return unit_price * quantity
