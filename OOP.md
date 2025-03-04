# Klasy w Pythonie

## Podstawy
    
    class NazwaKlasy:
        arg_klasowy = 10

        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2
    
    
    class NazwaKlasy(KlasaRodzica, KlasaRodzica2):
        arg_klasowy = 10

        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2