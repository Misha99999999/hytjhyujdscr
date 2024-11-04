import random
import time

# Inicializē mainīgos
inventory = []
player_alive = True
time_limit = 10  # Laika limits katrai izvēlei

# Definē funkciju, kas sāk spēli un vada ciklu, kamēr spēlētājs ir dzīvs
def start_game():
    while player_alive:
        entrance()

def entrance():
    print("Tu atrodies spoku mājas ieejā. Vai vēlies iet 'iekšā' vai bēgt 'prom'?")
    choice = get_input()
    if choice == "iekšā":
        foyer()
    elif choice == "prom":
        print("Tu izbēdzi droši. Spēle beigusies!")
        end_game()
    else:
        print("Nepareiza izvēle. Mēģini vēlreiz.")
        entrance()

def foyer():
    print("Tu ieej foajē. Ir tumšs, bet redzi durvis uz 'virtuvi', 'dzīvojamo istabu', 'pagrabu' un 'bibliotēku'.")
    show_map()
    choice = get_input()
    if choice == "virtuve":
        kitchen()
    elif choice == "dzīvojamā istaba":
        living_room()
    elif choice == "pagrabs":
        basement()
    elif choice == "bibliotēka":
        library()
    else:
        print("Nepareiza izvēle. Mēģini vēlreiz.")
        foyer()

def kitchen():
    print("Tu esi virtuvē. Tā ir biedējoša, un tu atrod rūsinātu nazi. Vai tu to 'ņem' vai atstāj 'aizvērtu'?")
    choice = get_input()
    if choice == "ņem":
        inventory.append("nazis")
        print("Tu paņēmi nazi.")
    encounter_spook()

def living_room():
    print("Dzīvojamā istaba ir putekļaina un tajā ir dīvains spogulis. Vai tu vēlies 'skatīties' spogulī vai iet 'atpakaļ'?")
    choice = get_input()
    if choice == "skatīties":
        print("Spogulis ir nolādēts! Tu pārvērties par spoku. Spēle beigusies.")
        end_game()
    elif choice == "atpakaļ":
        foyer()
    else:
        print("Nepareiza izvēle.")
        living_room()

def basement():
    print("Tu atrodi durvis uz pagrabu. Tās ir aizslēgtas. Ja tev būtu atslēga, tu varētu tās 'atvērt'.")
    choice = get_input()
    if choice == "atvērt":
        if "atslēga" in inventory:
            print("Tu atvēri durvis un izbēgi no spoku mājas! Tu uzvari!")
            end_game()
        else:
            print("Durvis ir aizslēgtas. Tev nepieciešama atslēga.")
            foyer()
    else:
        print("Nepareiza izvēle.")
        foyer()

def library():
    print("Bibliotēka ir pilna ar vecām grāmatām. Tu atrodi noliktu atslēgu. Ko tu gribi 'paņemt' vai 'atstāt'?")
    choice = get_input()
    if choice == "paņemt":
        inventory.append("atslēga")
        print("Tu paņēmi atslēgu.")
    elif choice == "atstāt":
        print("Tu atstāji visu tā, kā ir.")
    encounter_spook()

def encounter_spook():
    if random.choice([True, False]):  # 50% iespēja, ka spoks parādīsies
        print("Pēkšņi parādās spoks! Vai tu vēlies 'cīnīties' vai 'bēgt'?")
        action = get_input()
        if action == "cīnīties":
            if "nazis" in inventory:
                print("Tu uzvarēji spoku ar nazi! Tu atgriezies foajē.")
                foyer()
            else:
                print("Tev nav ar ko aizstāvēties. Spēle beigusies.")
                end_game()
        elif action == "bēgt":
            print("Tu aizbēdzi atpakaļ uz foajē.")
            foyer()
        else:
            print("Nepareiza izvēle.")
            foyer()
    else:
        print("Tu esi drošībā. Turpināsim.")

def show_map():
    print("Pieejamās istabas: virtuve, dzīvojamā istaba, pagrabs, bibliotēka.")

def get_input():
    start_time = time.time()
    choice = input(">>> ").lower()
    while time.time() - start_time < time_limit:
        if choice in ["iekšā", "prom", "virtuve", "dzīvojamā istaba", "pagrabs", "bibliotēka", "ņem", "aizvērtu", "skatīties", "atpakaļ", "paņemt", "atstāt", "cīnīties", "bēgt", "inventārs"]:
            return choice
        choice = input("Nepareiza izvēle. Mēģini vēlreiz (laiks līdz: {:.1f} sekundēm): ".format(time_limit - (time.time() - start_time))).lower()
    print("Laika limits ir beidzies! Spēle beigusies.")
    end_game()

def show_inventory():
    if inventory:
        print("Tavs inventārs: " + ", ".join(inventory))
    else:
        print("Tavs inventārs ir tukšs.")

def end_game():
    global player_alive
    player_alive = False
    if "nazis" in inventory and "atslēga" in inventory:
        print("Tu izbēg no mājas, izmantojot nazis un atslēgu. Tu esi uzvarējis!")
    elif "nazis" in inventory:
        print("Tu esi drošībā ar nazi, bet māja joprojām tevi tur. Spēle beigusies.")
    elif "atslēga" in inventory:
        print("Tu atradi atslēgu, bet nevari aizbēgt bez aizsardzības. Spēle beigusies.")
    else:
        print("Tu esi iedzīts stūrī. Spēle beigusies.")
    print("Paldies, ka spēlēji Piedzīvojums Spoku Mājā!")

# Sāk spēli
print("Sveicināts Piedzīvojums Spoku Mājā!")
start_game()
