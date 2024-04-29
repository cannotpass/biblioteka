"""
Program biblioteczny:

# Nie interesują nas autorzy, tylko tytuly.

# 1. DODAJ     Dodanie ksiazek
# 2. POZYCZ    Wyjecie ksiazek (wypozyczenie)
# 3. WYPISZ    Wypisanie listy ksiazek z liczba sztuk
# 4. SPRAWDZ   Sprawdzenie czy dana ksiazka jest na stanie
# 5. UNIKALNE  Wypisanie liczby unikalnych tytulow w bibliotece
# 6. LICZBA    Wypisanie sumy liczb woluminow w bibliotece
# 7. KONIEC    Zakonczenie dzialania programu
"""
from modules.io import (
    wczytaj_historie,
    zapisz_historie,
    wczytaj_biblioteke,
    zapisz_biblioteke,
)

from modules.actions import (
    pozycz,
    sprawdz,
    dodaj,
    wypisz,
    unikalne,
    liczba,
    wypisz_historie,
)

slownik_ksiazek = wczytaj_biblioteke()
historia = wczytaj_historie()

LISTA_KOMEND = ['DODAJ', 'POZYCZ', 'WYPISZ', 'SPRAWDZ', 'UNIKALNE', 'LICZBA', 'KONIEC']

while True:
    print(f"Wybierz komende z listy: {LISTA_KOMEND}")
    akcja = input("Podaj komende: ")
    if akcja == 'KONIEC':
        print('Koncze dzialanie programu...')
        break
    elif akcja == 'POZYCZ':
        tytul = input("> Podaj tytul ksiazki: ")
        liczba_sztuk = int(input("> Podaj liczbe sztuk: "))
        slownik_ksiazek, historia = pozycz(slownik_ksiazek, historia, liczba_sztuk, tytul)
    elif akcja == 'DODAJ':
        tytul = input("> Podaj tytul ksiazki: ")
        liczba_sztuk = int(input("> Podaj liczbe sztuk: "))
        slownik_ksiazek, historia = dodaj(slownik_ksiazek, historia, liczba_sztuk, tytul)
    elif akcja == 'WYPISZ':
        wypisz(slownik_ksiazek)
    elif akcja == 'SPRAWDZ':
        nazwa_ksiazki = input('Podaj nazwe ksiazki do sprawdzenia: ')
        sprawdz(slownik_ksiazek, nazwa_ksiazki)
    elif akcja == 'UNIKALNE':
        unikalne(slownik_ksiazek)
    elif akcja == 'LICZBA':
        liczba(slownik_ksiazek)
    elif akcja == 'HISTORIA':
        wypisz_historie(historia)
    else:
        print(f"Nieznana komenda: {akcja}")

zapisz_historie(historia)
zapisz_biblioteke(slownik_ksiazek)
