# Prosty kalkulator BMI na labki

def calculate_bmi(weight, height_cm):
    wzrost_m = height_cm / 100
    bmi = weight / (wzrost_m ** 2)
    return round(bmi, 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "niedowaga"
    elif bmi <= 24.9:
        return "waga prawidłowa"
    elif bmi <= 29.9:
        return "nadwaga"
    else:
        return "otyłość"


def read_positive_float(prompt, min_value, max_value):
    while True:
        wpis = input(prompt)
        if wpis == "":
            print("puste pole")
            continue
        try:
            liczba = float(wpis)
            if liczba >= min_value and liczba <= max_value:
                return liczba
            else:
                print("liczba poza zakresem")
        except ValueError:
            print("To nie jest liczba")


def add_person(results):
    print("\nDodawanie osoby:")
    imie = input("Podaj imie: ")
    while imie == "":
        print("imie nie moze byc puste")
        imie = input("podaj imie: ")

    wzrost = read_positive_float("Podaj wzrost w cm (80-250): ", 80, 250)
    waga = read_positive_float("Podaj wage w kg (20-300): ", 20, 300)

    wynik_bmi = calculate_bmi(waga, wzrost)
    kat = classify_bmi(wynik_bmi)

    osoba = {
        "name": imie,
        "height": wzrost,
        "weight": waga,
        "bmi": wynik_bmi,
        "category": kat
    }
    results.append(osoba)
    print("dodano do bazy")


def show_history(results):
    print("\n--- HISTORIA ---")
    if len(results) == 0:
        print("brak osob w histori.")
        return

    nr = 1
    for os in results:
        print(str(nr) + ". " + os["name"] + " - BMI: " + str(os["bmi"]) + " (" + os["category"] + ")")
        nr = nr + 1


def show_summary(results):
    print("\n--- PODSUMOWANIE ---")
    if len(results) == 0:
        print("nie mozna zrobic podsumowania, pusto")
        return

    suma_bmi = 0
    min_bmi = results[0]["bmi"]
    max_bmi = results[0]["bmi"]

    niedowaga = 0
    prawidlowa = 0
    nadwaga = 0
    otylosc = 0

    for os in results:
        akt_bmi = os["bmi"]
        suma_bmi = suma_bmi + akt_bmi

        if akt_bmi < min_bmi:
            min_bmi = akt_bmi
        if akt_bmi > max_bmi:
            max_bmi = akt_bmi

        if os["category"] == "niedowaga":
            niedowaga = niedowaga + 1
        elif os["category"] == "waga prawidłowa":
            prawidlowa = prawidlowa + 1
        elif os["category"] == "nadwaga":
            nadwaga = nadwaga + 1
        elif os["category"] == "otyłość":
            otylosc = otylosc + 1

    srednie = suma_bmi / len(results)

    print("liczba osób: " + str(len(results)))
    print("średnie BMI: " + str(round(srednie, 2)))
    print("min: " + str(min_bmi))
    print("max: " + str(max_bmi))
    print("niedowaga: " + str(niedowaga))
    print("waga prawidłowa: " + str(prawidlowa))
    print("nadwaga: " + str(nadwaga))
    print("otyłość: " + str(otylosc))


# Glowny program
results = []

while True:
    print("\nMENU:")
    print("1. dodaj wynik")
    print("2. wyświetl historię")
    print("3. pokaż podsumowanie")
    print("0. zakończ")

    wybor = input("wybierz opcje: ")

    if wybor == "1":
        add_person(results)
    elif wybor == "2":
        show_history(results)
    elif wybor == "3":
        show_summary(results)
    elif wybor == "0":
        print("koniec programu")
        break
    else:
        print("zly wybor, Wybierz 0, 1, 2 lub 3.")