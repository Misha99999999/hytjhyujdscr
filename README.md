# Funkcija, lai saskaitītu divus skaitļus
def add(a, b):
    """
    Funkcija, kas veic saskaitīšanu starp diviem skaitļiem.
    """
    return a + b

# Funkcija, lai atņemtu divus skaitļus
def subtract(a, b):
    """
    Funkcija, kas veic atņemšanu starp diviem skaitļiem.
    """
    return a - b

# Funkcija, lai reizinātu divus skaitļus
def multiply(a, b):
    """
    Funkcija, kas veic reizināšanu starp diviem skaitļiem.
    """
    return a * b

# Funkcija, lai dalītu divus skaitļus
def divide(a, b):
    """
    Funkcija, kas veic dalīšanu starp diviem skaitļiem.
    Pārbauda, vai dalītājs nav nulle, jo dalīšana ar nulli ir neatļauta.
    """
    if b == 0:
        return "Kļūda: Dalīšana ar nulli nav iespējama!"
    else:
        return a / b

# Funkcija, kas pārbauda, vai viens skaitlis ir dalāms ar citu
def is_divisible(a, b):
    """
    Funkcija, kas pārbauda, vai pirmais skaitlis ir dalāms ar otro skaitli.
    """
    if b == 0:
        return "Kļūda: Dalīšana ar nulli nav iespējama!"
    elif a % b == 0:
        return True
    else:
        return False

# Funkcija, lai lietotājs izvēlētos aprēķinu veidu
def select_operation():
    """
    Funkcija, kas ļauj lietotājam izvēlēties veikt matemātisko operāciju.
    """
    print("Izvēlieties operāciju:")
    print("1. Saskaitīšana")
    print("2. Atņemšana")
    print("3. Reizināšana")
    print("4. Dalīšana")
    print("5. Pārbaudīt, vai skaitlis ir dalāms ar citu skaitli")
    
    choice = input("Ievadiet izvēles numuru (1/2/3/4/5): ")
    
    # Atgriež lietotāja izvēli
    return choice

# Funkcija, lai ievadītu skaitļus un izvēlēto operāciju
def get_numbers_and_perform_operation():
    """
    Funkcija, kas iegūst skaitļus no lietotāja un veic izvēlēto operāciju.
    """
    while True:
        # Iegūstam izvēlēto operāciju
        choice = select_operation()

        if choice == '1':
            # Saskaitīšana
            a = float(input("Ievadiet pirmo skaitli: "))
            b = float(input("Ievadiet otro skaitli: "))
            print(f"Rezultāts: {add(a, b)}")

        elif choice == '2':
            # Atņemšana
            a = float(input("Ievadiet pirmo skaitli: "))
            b = float(input("Ievadiet otro skaitli: "))
            print(f"Rezultāts: {subtract(a, b)}")

        elif choice == '3':
            # Reizināšana
            a = float(input("Ievadiet pirmo skaitli: "))
            b = float(input("Ievadiet otro skaitli: "))
            print(f"Rezultāts: {multiply(a, b)}")

        elif choice == '4':
            # Dalīšana
            a = float(input("Ievadiet pirmo skaitli: "))
            b = float(input("Ievadiet otro skaitli: "))
            result = divide(a, b)
            print(f"Rezultāts: {result}")

        elif choice == '5':
            # Dalāmības pārbaude
            a = int(input("Ievadiet pirmo skaitli: "))
            b = int(input("Ievadiet otro skaitli: "))
            result = is_divisible(a, b)
            if result == True:
                print(f"{a} ir dalāms ar {b}.")
            elif result == False:
                print(f"{a} nav dalāms ar {b}.")
            else:
                print(result)  # Ja ir kļūda dalīšanā ar nulli

        else:
            print("Nepareiza izvēle. Lūdzu izvēlieties derīgu operāciju.")

        # Jautā, vai lietotājs vēlas veikt vēl vienu aprēķinu
        again = input("Vai vēlaties veikt vēl vienu aprēķinu? (jā/nē): ").lower()
        if again != 'jā':
            print("Paldies par izmantošanu!")
            break

# Galvenā funkcija, kas palaidīs kalkulatoru
def main():
    """
    Galvenā funkcija, kas nodrošina kalkulatora darbību.
    """
    print("Laipni lūdzam matemātiskajā kalkulatorā!")
    get_numbers_and_perform_operation()

# Izsaucam galveno funkciju
if __name__ == "__main__":
    main()
