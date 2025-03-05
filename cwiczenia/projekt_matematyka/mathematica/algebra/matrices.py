def add_matrices(a, b):
    result = []
    for row_a, row_b in zip(a, b):
        row = []
        for el_row_a, el_row_b in zip(row_a, row_b):
            row.append(el_row_a + el_row_b)
        result.append(row)
    return result


def sub_matrices(a, b):
    result = []
    for row_a, row_b in zip(a, b):
        row = []
        for el_row_a, el_row_b in zip(row_a, row_b):
            row.append(el_row_a - el_row_b)
        result.append(row)
    return result
