Utwórz następującą strukture:

1. główny folder projektu
2. główny pakiet mathematica
3. wewnetrz mathematica pakiet geometry, algebra
4. w pakiecie geometry utworz modul figures  - z funkcjami sqeare_area, triangle_area
5. w pakiecie algebra utworz modul metrices z funkcjami add_matrices, sub_matrices
6. pakiet glowny tests z modulami test_geometry i test_algebra

```
projekt
    mathematica
        geometry
            figures.py
        algebra
            matrices.py
    tests
        test_geometry.py
        test_algebra.py
```

przydatna moze byc funkcja zip

```python
a = [1, 2, 3]
b = [2, 3, 4]

row = []
for el_a, el_b in zip(a, b):
    row.append(el_a + el_b)
```