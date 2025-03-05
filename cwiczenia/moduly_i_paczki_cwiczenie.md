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

                
                def add_matrices(a, b):
                    result = []
                    for row_a, row_b in zip(a, b):
                        row = []
                        for el_row_a, el_row_b in zip(row_a, row_b):
                            row.append(el_row_a + el_row_b)
                        result.append(row)
                     return result
                            
    tests
        test_geometry.py
        test_algebra.py
            # pip install pytest
            # pytest 
            from mathematica.algebra.matrices import add_matrices
            
            def test_add_matrices():
                a = [[1, 2, 3], [1, 2, 3]]
                b = [[2, 3, 4], [2, 3, 4]]
                
                r = [[3, 6, 7], [3, 6, 7]]
                
                assert add_matrices(a, b) == result
                
                
```

przydatna moze byc funkcja zip

```python

```