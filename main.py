"""
Program biblioteczny:

# Nie interesują nas autorzy, tylko tytuly.

1. DODAJ     Dodanie ksiazek
2. POZYCZ    Wyjecie ksiazek (wypozyczenie)
# 3. WYPISZ    Wypisanie listy ksiazek z liczba sztuk
# 4. SPRAWDZ   Sprawdzenie czy dana ksiazka jest na stanie
# 5. UNIKALNE  Wypisanie liczby unikalnych tytulow w bibliotece
# 6. LICZBA    Wypisanie sumy liczb woluminow w bibliotece
# 7. KONIEC    Zakonczenie dzialania programu
"""

slownik_ksiazek = {
    "Harry Potter: Kamien Filozoficzny": 1,
    "Wladca Pierscieni: Powrot Krola": 10,
    "Hobbit": 12,
    "Ulysses": 0,
}

LISTA_KOMEND = ['DODAJ', 'POZYCZ', 'WYPISZ', 'SPRAWDZ', 'UNIKALNE', 'LICZBA', 'KONIEC']

while True:
    print(f"Wybierz komende z listy: {LISTA_KOMEND}")
    akcja = input("Podaj komende: ")
    if akcja == 'KONIEC':
        print('Koncze dzialanie programu...')
        break
    elif akcja == 'DODAJ':
        tytul = input("> Podaj tytul ksiazki: ")
        liczba_sztuk = int(input("> Podaj liczbe sztuk: "))
        if liczba_sztuk < 0:
            print(">> Liczba sztuk dodawanej ksiazki musi byc wieksza lub rowna 0.")
            continue
        print(f">> Dodaje '{tytul}' w liczbie {liczba_sztuk}")
        if tytul not in slownik_ksiazek:
            slownik_ksiazek[tytul] = 0
        slownik_ksiazek[tytul] += liczba_sztuk
    elif akcja == 'WYPISZ':
        print("Lista dostepnych ksiazek:")
        for tytul, liczba_sztuk in slownik_ksiazek.items():
            print(f"{tytul:<35.35s} | {liczba_sztuk:>3.0f}")
    elif akcja == 'SPRAWDZ':
        nazwa_ksiazki = input('Podaj nazwe ksiazki do sprawdzenia: ')
        if nazwa_ksiazki in slownik_ksiazek and slownik_ksiazek[nazwa_ksiazki] > 0:
            print(f"> Ksiazka '{nazwa_ksiazki}' jest dostepna.")
        else:
            print(f"> Niestety, ksiazka '{nazwa_ksiazki}' jest niedostepna.")
    elif akcja == 'UNIKALNE':
        print("> Lista tytulow w bazie danych:")
        for tytul in slownik_ksiazek.keys():
            print(f">> {tytul}")
    elif akcja == 'LICZBA':
        liczba_ksiazek = 0
        for sztuk in slownik_ksiazek.values():
            liczba_ksiazek += sztuk
        print(f"> Calkowita liczba woluminow w bibliotece: {liczba_ksiazek}")
    else:
        print(f"Nieznana komenda: {akcja}")
