def calculate(distance: int, price_per_l: float, l_per_100: float):
    fuel = distance * l_per_100 / 100
    return round(fuel * price_per_l, 2)