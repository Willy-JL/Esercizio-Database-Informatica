import os
import sys
import json
import time
import globals


def pulisci_schermo():
    if sys.platform.startswith("linux"):
        os.system("clear")
    elif sys.platform.startswith("win"):
        os.system("cls")


def salva_database():
    with open("database.json", "w", encoding="utf-8") as file:
        json.dump(globals.database, file, indent=4)


def lista_tabelle():
    print("Le seguenti tabelle solo disponibili:")
    if len(globals.database) == 0:
        print("   Non ci sono tabelle nel database!")
    else:
        for tabella in globals.database:
            print(" - ", tabella)


def visualizza_tabella():
    pulisci_schermo()  # placeholder


def crea_tabella():
    pulisci_schermo()  # placeholder


def modifica_tabella():
    pulisci_schermo()  # placeholder


def elimina_tabella():
    while True:
        lista_tabelle()
        print("Quale tabella vuoi eliminare? (Premi invio per tornare indietro)")
        tabella_da_eliminare = input(">>> ")

        if tabella_da_eliminare == "":
            pulisci_schermo()
            break

        if tabella_da_eliminare not in globals.database:
            print("\nQuesta tabella non esiste!")
            time.sleep(2)
            pulisci_schermo()
            continue

        del globals.database[tabella_da_eliminare]
        salva_database()
        print("\nTabella eliminata con successo!\n")
        time.sleep(2)
        pulisci_schermo()
        break



if __name__ == "__main__":
    pulisci_schermo()

    try:
        with open("database.json", "r", encoding="utf-8") as file:
            try:
                globals.database = json.load(file)
            except json.JSONDecodeError:
                print('Il file del database è corrotto! Creo un file vuoto...')
                time.sleep(2)
                pulisci_schermo()
                globals.database = {}
                salva_database()
    except FileNotFoundError:
        globals.database = {}
        salva_database()

    while True:
        print("Cosa vuoi fare? (Premi invio per uscire dal programma)")
        print("1) Visualizza tabella")
        print("2) Crea tabella")
        print("3) Modifica tabella")
        print("4) Elimina tabella")
        scelta = input(">>> ")

        if scelta not in ["1", "2", "3", "4", ""]:
            print("\nScelta invalida!")
            time.sleep(2)
            pulisci_schermo()
            continue

        if scelta == "":
            break

        pulisci_schermo()

        if scelta == "1":
            visualizza_tabella()

        if scelta == "2":
            crea_tabella()

        if scelta == "3":
            modifica_tabella()

        if scelta == "4":
            elimina_tabella()











"""
globals.database = {
    "persone": [
        [ "nome", "cognome", "eta", "professione" ]
        [ "umbo", "lugo",    18,    "studente"    ]
        [ "umbo", "lugo",    18,    "studente"    ]
        [ "umbo", "lugo",    18,    "studente"    ]
    ],
    "scuole": [
        [ "nome",    "luogo",  "studenti", "cup_size_average" ]
        [ "aleardi", "verona", "tanti",    None               ]
        [ "aleardi", "verona", "tanti",    None               ]
        [ "aleardi", "verona", "tanti",    None               ]
    ]
}
"""
