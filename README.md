# Kurs - Python 2 bootcamp

Szkolenie uzupelniajace z Pythona

1. Sprawdzenie aktualnego stanu wiedzy
2. Podstawy pracy z VIM i GIT
3. Wprowadzenie do markdown

| A | B | 
|---|---|
| 1 | 2 |


$y=x^2$

4. Omowienie typów liczbowych

    [typy liczbowe](type_liczbowe_w_pythonie.md)


## Podstawy pracy z vim

Otwarcie pliku do edycji:


    vim <nazwa_pliku>


wejście w tryb edycji:

    i

wejście w tryb poleceń:

    Esc


zapis pliku:

    :w

wyjscie z pliku:


    :q


zapis i wyjscie:

    :wq

po kazdym poleceniu enter


## Podstawy pracy z git


Tworzenie nowego repo lokalnie:

    git init

Powiązanie ze zdalnym repozytorium:

    git remote add origin <url>

Sprawdzenie z jakimi zdalnymi repo jesteśmy powiązani

    git remote -v

Sklonowanie istniejącego repozytorium:

    git clone <url>

   
### praca lokalna

    git status

to doda konkretny plik na stos

    git add <sciezka do pliku>

to doda wszystkie pliki na stos  
   
    git add .
   
zapis zmian:

    git commit


    git commit -m "<commit message>"


### praca ze zdalnym repo


wyslanie zmian:

    git push origin <nazwa brancha>


pobranie zmian


    git pull origin <nazwa brancha>







