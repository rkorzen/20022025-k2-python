"""
Napisz funkcję analyze_text(content: str), która przyjmie tekst jako argument i zwróci słownik z analizą:

    word_count: liczba słów w tekście,
    longest_word: najdłuższe słowo w tekście,
    most_common_letter: najczęściej występująca litera.

📌 Wskazówki:

    Możesz użyć max() z key=len, aby znaleźć najdłuższe słowo.
    Możesz użyć Counter z collections, aby policzyć częstotliwość liter.

Napisz funkcję process_words(words: list[str], func), która przyjmuje listę słów i funkcję func,
a następnie zwraca nową listę słów przetworzonych przez tę funkcję.
📌 Wskazówka: func może być np. str.upper lub str[::-1].

Stwórz dekorator @execution_time, który będzie mierzył czas wykonania funkcji i wypisywał go w konsoli.
📌 Wskazówka: użyj time.perf_counter() przed i po wywołaniu funkcji.


Dodatkowo

Wywołaj process_words() z funkcja anonimowya lambda, np. lambda word: word[::-1] (odwracanie słów).
Dodaj dodatkowy dekorator @log_calls, który będzie logował każde wywołanie funkcji i jej argumenty.

"""