from mathematica.algebra.matrices import add_matrices, sub_matrices


def test_add_matrices():
    a = [[1, 2, 3], [1, 2, 3]]
    b = [[2, 3, 4], [2, 3, 4]]

    r = [[3, 5, 7], [3, 5, 7]]

    assert add_matrices(a, b) == r


def test_sub_matrices():
    a = [[1, 2, 3], [1, 2, 3]]
    b = [[2, 3, 4], [2, 3, 4]]

    r = [[-1, -1, -1], [-1, -1, -1]]

    assert sub_matrices(a, b) == r

