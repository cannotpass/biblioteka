from modules.settings import (
    DEFAULT_HISTORY_FILE_PATH,
    DEFAULT_LIBRARY_FILE_PATH,
)


def wczytaj_historie(file_path=DEFAULT_HISTORY_FILE_PATH):
    """Format historii:
    Wpis 1
    Wpis 2
    Wpis 3
    ..."""
    historia = []
    with open(file_path) as f:
        for line in f:
            historia.append(line.strip())
    return historia


def zapisz_historie(historia, file_path=DEFAULT_HISTORY_FILE_PATH):
    """Format historii:
    Wpis 1
    Wpis 2
    Wpis 3
    ..."""
    with open(file_path, "w") as f:
        for line in historia:
            f.write(str(line) + '\n')


def wczytaj_biblioteke(file_path=DEFAULT_LIBRARY_FILE_PATH):
    """Format biblioteki:
    Hobbit;10
    Harry Potter i Komnata Tajemnic;25"""
    biblioteka = {}
    with open(file_path) as f:
        for line in f:
            tytul, sztuk = line.strip().split(';')
            biblioteka[tytul] = int(sztuk)
    return biblioteka


def zapisz_biblioteke(biblioteka, file_path=DEFAULT_LIBRARY_FILE_PATH):
    with open(file_path, "w") as f:
        for tytul, sztuk in biblioteka.items():
            f.write(f"{tytul};{sztuk}\n")
