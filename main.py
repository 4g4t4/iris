# Importujemy moduł csv, który pozwoli nam na pracę z plikami csv

import csv

# Definiujemy funkcję read_csv, która przyjmuje dwa argumenty: nazwę pliku oraz informację
# czy pierwszy wiersz zawiera etykiety kolumn (domyślnie ustawione na True).

def read_csv(Iris, has_headers=True):

    # Tworzymy pustą listę data, do której będziemy zapisywać dane z pliku.
    # Tworzymy również pustą listę headers, do której będziemy zapisywać etykiety kolumn (jeśli istnieją).

    data = []
    headers = []

    # Otwieramy plik o nazwie podanej jako argument funkcji w trybie do odczytu (mode='r').
    with open(Iris, 'r') as f:
        # Tworzymy obiekt reader za pomocą funkcji csv.reader, przekazując do niej otwarty plik.
        reader = csv.reader(f)
        # Sprawdzenie czy w pierwszym wierszu pliku znajdują się etykiety kolumn
        if has_headers:
            headers = next(reader)
        # Odczytanie danych z pliku csv o nazwie podanej w argumencie funkcji read_csv i zapisanie ich do listy data.
        for row in reader:
            data.append(row)
    return headers, data
# Wyświetlanie etykiet. Jeśli argument headers nie jest pusty (czyli zawiera etykiety), to są one wyświetlane, jeśli jest pusty zwraca "Brak etykiet w pliku."
def print_headers(headers):
        if headers:
            print("Etykiety:", *headers)
        else:
             print("Brak etykiet w pliku.")
headers, data = read_csv('Iris.csv')
print(headers)
print_headers(headers)
# Wypisanie danych datasetu, jeśli end=None, wypisuje cały zbiór, jeśli wpiszemy konkretne wartości wyświetlenie wg podanych danych
def print_data(data, start=0, end=None):

    if end is None:
        end = len(data)
    for row in data[start:end]:
        print(row)

print_data(data, start=0, end=6)
# Podział na zbiór treningowy, testowy oraz walidacyjny
def split_data(data, train_percentage, test_percentage, validation_percentage):
    train_size = int(len(data) * (train_percentage / 100))  # Ustawienie rozmiaru zbioru treningowego poprzez użycie liczby zbioru
                                                            #oraz zmienną "train_percentage" równą w tym przypadku 60%

    test_size = int(len(data) * (test_percentage / 100))    # Analogicznie pozostałe zbiory
    validation_size = int(len(data) * (validation_percentage / 100))
    # Utworzenie listy składającej się z elementów "data" od indexu 0 do indexu "train size",
    # czyli jego ostatniego elementu, który ma zostać wpisany do listy "train_data", analogicznie dla pozostałych list.
    train_data = data[:train_size]
    test_data = data[train_size:train_size+test_size]
    validation_data = data[train_size+test_size:train_size+test_size+validation_size]
    return train_data, test_data, validation_data
headers, data = read_csv('Iris.csv')
train_data, test_data, validation_data = split_data(data, 60, 20, 20)
print("Rozmiar całego zbioru :", len(data))
print("Rozmiar zbioru treningowego:", len(train_data))
print("Rozmiar zbioru testowego:", len(test_data))
print("Rozmiar zbioru walidacyjnego:", len(validation_data))

# Zmienna przechowująca index kolumny zawierającej etykietę , wartość -1 czyli jeszcze nie znaleziona
class_index = -1
# Wypisanie dla każdej z klas decyzyjnych jej nazwy oraz liczebności
def get_class_frequencies(data, class_index):
    classes = [row[class_index] for row in data] # zawiera wartości klas dla każdego wiersza
    frequencies = {} # pusty słownik, który służy do zliczania wystąpień poszczególnych klas
    for c in classes:
        if c in frequencies:
            frequencies[c] += 1
        else:
            frequencies[c] = 1
    return frequencies
# Funkcja "print_class_frequencies" przyjmuje jako argumenty dane oraz indeks kolumny zawierającej informację o klasie.
# Następnie wywołuje funkcję "get_class_frequencies", która zwraca słownik z częstościami wystąpień poszczególnych klas.
def print_class_frequencies(data, class_index):
    frequencies = get_class_frequencies(data, class_index)
    # Przechodzi po elementach słownika i dla każdego z nich wyświetla informację o klasie i jej liczebności.
    for c, count in frequencies.items():
        print(f'Klasa: {c}, Liczebność: {count}')

print_class_frequencies(data, class_index)

# Funkcja ta iteruje przez każdy wiersz w "data" i sprawdza, czy element pod indeksem "class_index" jest równy "desired_class".
# Jeśli tak, to wiersz jest drukowany
def print_rows_with_class(data, class_index, desired_class):
    for row in data:
        if row[class_index] == desired_class:
            print(row)
print_rows_with_class(data, -1, 'Iris-versicolor')

def save_to_csv(data, Iris):
    with open(Iris, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

save_to_csv(data[:10], 'Iris_partial.csv')





