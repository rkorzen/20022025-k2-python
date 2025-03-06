
def calculate(distance: int, price_per_l: float, l_per_100: float):
    fuel = distance *  l_per_100 / 100
    return round(fuel * price_per_l, 2)


if __name__ == "__main__":

    assert calculate(100, 1, 100) == 100
    assert calculate(100, 1, 50) == 50
    assert calculate(400, 6.5, 5) == 130

