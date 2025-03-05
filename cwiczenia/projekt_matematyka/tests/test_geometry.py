from mathematica.geometry.figures import triangle_area, square_area


def test_triangle_area():

    assert triangle_area(1, 2) == 1
    assert triangle_area(2, 2) == 2

def test_square_area():

    assert square_area(10) == 100
    assert square_area(20) == 400
