def pozycz(slownik_ksiazek, historia, liczba_sztuk, tytul):
    if liczba_sztuk <= 0:
        print(">> Liczba sztuk pozyczanej ksiazki musi byc wieksza 0.")
        return slownik_ksiazek, historia
    if tytul in slownik_ksiazek and slownik_ksiazek[tytul] >= liczba_sztuk:
        print(f">> Pozyczam {liczba_sztuk} sztuk '{tytul}'.")
        slownik_ksiazek[tytul] -= liczba_sztuk
    else:
        print(f">> Niewystarczajaca liczba sztuk ksiazki.")
        return slownik_ksiazek, historia
    historia.append(["POZYCZ", tytul, liczba_sztuk])
    return slownik_ksiazek, historia

def dodaj(slownik_ksiazek, historia, liczba_sztuk, tytul):
    if liczba_sztuk < 0:
        print(">> Liczba sztuk dodawanej ksiazki musi byc wieksza lub rowna 0.")
        return slownik_ksiazek, historia
    print(f">> Dodaje '{tytul}' w liczbie {liczba_sztuk}")
    if tytul not in slownik_ksiazek:
        slownik_ksiazek[tytul] = 0
    slownik_ksiazek[tytul] += liczba_sztuk
    historia.append(["DODAJ", tytul, liczba_sztuk])
    return slownik_ksiazek, historia


def sprawdz(slownik_ksiazek, nazwa_ksiazki):
    if nazwa_ksiazki in slownik_ksiazek and slownik_ksiazek[nazwa_ksiazki] > 0:
        print(f"> Ksiazka '{nazwa_ksiazki}' jest dostepna.")
    else:
        print(f"> Niestety, ksiazka '{nazwa_ksiazki}' jest niedostepna.")


def wypisz(slownik_ksiazek):
    print("Lista dostepnych ksiazek:")
    for tytul, liczba_sztuk in slownik_ksiazek.items():
        print(f"{tytul:<35.35s} | {liczba_sztuk:>3.0f}")


def unikalne(slownik_ksiazek):
    print("> Lista tytulow w bazie danych:")
    for tytul in slownik_ksiazek.keys():
        print(f">> {tytul}")


def liczba(slownik_ksiazek):
    liczba_ksiazek = 0
    for sztuk in slownik_ksiazek.values():
        liczba_ksiazek += sztuk
    print(f"> Calkowita liczba woluminow w bibliotece: {liczba_ksiazek}")


def wypisz_historie(historia):
    print("\nHistoria: ")
    for wpis in historia:
        print(wpis)


def wypisz_wybrana_historie(historia, od, do):
    if do < od:
        print("OD musi byc wieksze od DO.")
    elif od >= len(historia):
        print(f"OD musi byc mniejsze niz dlugos listy: {len(historia)}.")
    elif od < 0 or do < 0:
        print("OD i DO nie moga byc ujemne.")
    else:
        print(f"Fragment historii od {od} do {do}:")
        for wpis in historia[od:do+1]:
            print(wpis)


if __name__ == "__main__":
    # Test funkcji
    test_historia = [
        ["DODAJ", "Hobbit", 10],
        ["POZYCZ", "Hobbit", 2],
        ["DODAJ", "Python Zaawansowany", 5],
    ]
    wypisz_historie(test_historia)

    # Test dodawania ksiazki
    test_slownik = {}
    test_historia = []
    oczekiwany_wynik = {'Python': 2}
    oczekiwana_historia = [['DODAJ', 'Python', 2]]
    test_slownik, test_historia = dodaj(test_slownik, test_historia, 2, "Python")
    assert test_slownik == oczekiwany_wynik, f"Blad dodawnia do biblioteki, oczekiwano {oczekiwany_wynik}, otrzymano {test_slownik}."
    assert test_historia == oczekiwana_historia, f"Blad historii, oczekiwano: {oczekiwana_historia}, otrzymano {test_historia}"
