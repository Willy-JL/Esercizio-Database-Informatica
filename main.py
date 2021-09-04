import os
import sys
import json
import time


def pulisci_schermo():
    if sys.platform.startswith("linux"):
        os.system("clear")
    elif sys.platform.startswith("win"):
        os.system("cls")


def salva_database():
    with open("database.json", "w", encoding="utf-8") as file:
        json.dump(database, file, indent=4)


def lista_tabelle():
    if len(database) == 0:
        print("   Non ci sono tabelle nel database!")
    else:
        for tabella in database:
            print(" - ", tabella)


def visualizza_tabella():
    while True:
        print("Quale tabella vuoi visualizzare? (Premi invio per tornare indietro)")
        lista_tabelle()
        tabella_da_visualizzare = input(">>> ")

        if tabella_da_visualizzare == "":
            pulisci_schermo()
            return

        if tabella_da_visualizzare not in database:
            print("\nQuesta tabella non esiste!")
            time.sleep(2)
            pulisci_schermo()
            continue

        break

    print(f"\n\nTabella: {tabella_da_visualizzare} (Premi invio per tornare indietro)")

    larghezze = [len(nome_colonna) for nome_colonna in database[tabella_da_visualizzare][0]]
    for riga in database[tabella_da_visualizzare]:
        for i, valore in enumerate(riga):
            larghezze[i] = max(len(valore), larghezze[i])

    for i, riga in enumerate(database[tabella_da_visualizzare]):
        for j, valore in enumerate(riga):
            print(valore + (" " * (larghezze[j] - len(valore))) + (" | " if j != (len(larghezze) - 1) else "\n"), end="")
        if i == 0:
            print("-|-".join(["-" * larghezza for larghezza in larghezze]))

    input()
    pulisci_schermo()


def crea_tabella():
    while True:
        print("Che nome avrà la nuova tabella? (Premi invio per tornare indietro)")
        nome_tabella = input(">>> ")

        if nome_tabella == "":
            pulisci_schermo()
            return

        if nome_tabella in database:
            print("\nEsiste già una tabella con questo nome!")
            time.sleep(2)
            pulisci_schermo()
            continue

        break

    print("\n\nScrivi su righe separate i nomi delle colonne da creare e premi invio per confermare...")
    colonne = []
    while True:
        nuova_colonna = input()
        if nuova_colonna in colonne:
            continue
        if nuova_colonna == "" and len(colonne) > 0:
            break
        if nuova_colonna != "":
            colonne.append(nuova_colonna)

    while True:
        print(f"\n\nVerrà creata la tabella '{nome_tabella}' con colonne '" + "', '".join(colonne) + "'. Confermi?")
        conferma = input(">>> ")

        if conferma.lower() in ["s", "si"]:
            database[nome_tabella] = []
            database[nome_tabella].append(colonne)
            salva_database()
            print("\nLa tabella è stata creata con successo!")
            time.sleep(2)
            pulisci_schermo()
            return

        if conferma.lower() in ["n", "no"]:
            pulisci_schermo()
            return

        print("\nScelta invalida!")
        continue


def modifica_tabella():
    while True:
        print("Quale tabella vuoi modificare? (Premi invio per tornare indietro)")
        lista_tabelle()
        tabella_da_modificare = input(">>> ")

        if tabella_da_modificare == "":
            pulisci_schermo()
            return

        if tabella_da_modificare not in database:
            print("\nQuesta tabella non esiste!")
            time.sleep(2)
            pulisci_schermo()
            continue

        pulisci_schermo()
        break

    while True:
        print(f"Tabella selezionata: {tabella_da_modificare}")
        print("Cosa vuoi fare? (Premi invio per tornare indietro)")
        print(" 1) Aggiungi riga")
        print(" 2) Modifica riga")
        print(" 3) Elimina riga")
        scelta = input(">>> ")

        if scelta not in ["1", "2", "3", ""]:
            print("\nScelta invalida!")
            time.sleep(2)
            pulisci_schermo()
            continue

        if scelta == "":
            pulisci_schermo()
            break

        if scelta == "1":
            print("\n\nScrivi su righe separate i valori per le colonne '" + "', '".join(database[tabella_da_modificare][0]) + "'...")
            valori = []
            for _ in range(len(database[tabella_da_modificare][0])):
                nuovo_valore = input()
                valori.append(nuovo_valore)

            while True:
                print("\n\nVerrà aggiunta la riga '" + "', '".join(valori) + "'. Confermi?")
                conferma = input(">>> ")

                if conferma.lower() in ["s", "si"]:
                    database[tabella_da_modificare].append(valori)
                    salva_database()
                    print("\nLa riga è stata aggiunta con successo!")
                    time.sleep(2)
                    pulisci_schermo()
                    break

                if conferma.lower() in ["n", "no"]:
                    pulisci_schermo()
                    break

                print("\nScelta invalida!")
                continue

        if scelta == "2":
            while True:
                larghezze = [len(nome_colonna) for nome_colonna in database[tabella_da_modificare][0]]
                for riga in database[tabella_da_modificare]:
                    for i, valore in enumerate(riga):
                        larghezze[i] = max(len(valore), larghezze[i])
                larghezza_i = len(str(len(database[tabella_da_modificare]) - 1))

                print("\n\nQuale riga vuoi modificare? (Premi invio per tornare indietro)")
                for i, riga in enumerate(database[tabella_da_modificare]):
                    print((f"{i}) " + (" " * (larghezza_i - len(str(i))))) if i != 0 else (" " * (larghezza_i + 2)), end="")
                    for j, valore in enumerate(riga):
                        print(valore + (" " * (larghezze[j] - len(valore))) + (" | " if j != (len(larghezze) - 1) else "\n"), end="")
                    if i == 0:
                        print((" " * (larghezza_i + 2)) + "-|-".join(["-" * larghezza for larghezza in larghezze]))

                riga_da_modificare = input(">>> ")

                if riga_da_modificare == "":
                    pulisci_schermo()
                    break

                if riga_da_modificare.isnumeric() and int(riga_da_modificare) > 0 and int(riga_da_modificare) < len(database[tabella_da_modificare]):
                    print("\n\nScrivi su righe separate i valori per le colonne '" + "', '".join(database[tabella_da_modificare][0]) + "'...")
                    valori = []
                    for _ in range(len(database[tabella_da_modificare][0])):
                        nuovo_valore = input()
                        valori.append(nuovo_valore)

                    while True:
                        print("\n\nVerrà modificata la riga '" + "', '".join(database[tabella_da_modificare][int(riga_da_modificare)]) + "' con i nuovi valori '" + "', '".join(valori) + "'. Confermi?")
                        conferma = input(">>> ")

                        if conferma.lower() in ["s", "si"]:
                            database[tabella_da_modificare][int(riga_da_modificare)] = valori
                            salva_database()
                            print("\nLa riga è stata modificata con successo!")
                            time.sleep(2)
                            pulisci_schermo()
                            break

                        if conferma.lower() in ["n", "no"]:
                            pulisci_schermo()
                            break

                        print("\nScelta invalida!")
                        continue
                    break

                print("\nScelta invalida!")
                continue

        if scelta == "3":
            while True:
                larghezze = [len(nome_colonna) for nome_colonna in database[tabella_da_modificare][0]]
                for riga in database[tabella_da_modificare]:
                    for i, valore in enumerate(riga):
                        larghezze[i] = max(len(valore), larghezze[i])
                larghezza_i = len(str(len(database[tabella_da_modificare]) - 1))

                print("\n\nQuale riga vuoi eliminare? (Premi invio per tornare indietro)")
                for i, riga in enumerate(database[tabella_da_modificare]):
                    print((f"{i}) " + (" " * (larghezza_i - len(str(i))))) if i != 0 else (" " * (larghezza_i + 2)), end="")
                    for j, valore in enumerate(riga):
                        print(valore + (" " * (larghezze[j] - len(valore))) + (" | " if j != (len(larghezze) - 1) else "\n"), end="")
                    if i == 0:
                        print((" " * (larghezza_i + 2)) + "-|-".join(["-" * larghezza for larghezza in larghezze]))

                riga_da_eliminare = input(">>> ")

                if riga_da_eliminare == "":
                    pulisci_schermo()
                    break

                if riga_da_eliminare.isnumeric() and int(riga_da_eliminare) > 0 and int(riga_da_eliminare) < len(database[tabella_da_modificare]):
                    while True:
                        print("\n\nVerrà eliminata la riga '" + "', '".join(database[tabella_da_modificare][int(riga_da_eliminare)]) + "'. Confermi?")
                        conferma = input(">>> ")

                        if conferma.lower() in ["s", "si"]:
                            del database[tabella_da_modificare][int(riga_da_eliminare)]
                            salva_database()
                            print("\nLa riga è stata eliminata con successo!")
                            time.sleep(2)
                            pulisci_schermo()
                            break

                        if conferma.lower() in ["n", "no"]:
                            pulisci_schermo()
                            break

                        print("\nScelta invalida!")
                        continue
                    break

                print("\nScelta invalida!")
                continue


def elimina_tabella():
    while True:
        print("Quale tabella vuoi eliminare? (Premi invio per tornare indietro)")
        lista_tabelle()
        tabella_da_eliminare = input(">>> ")

        if tabella_da_eliminare == "":
            pulisci_schermo()
            return

        if tabella_da_eliminare not in database:
            print("\nQuesta tabella non esiste!")
            time.sleep(2)
            pulisci_schermo()
            continue

        break

    while True:
        print(f"\n\nVerrà eliminata la tabella '{tabella_da_eliminare}'. Confermi?")
        conferma = input(">>> ")

        if conferma.lower() in ["s", "si"]:
            del database[tabella_da_eliminare]
            salva_database()
            print("\nLa tabella è stata eliminata con successo!")
            time.sleep(2)
            pulisci_schermo()
            break

        if conferma.lower() in ["n", "no"]:
            pulisci_schermo()
            break

        print("\nScelta invalida!")
        continue


if __name__ == "__main__":
    pulisci_schermo()

    try:
        with open("database.json", "r", encoding="utf-8") as file:
            try:
                database = json.load(file)
            except json.JSONDecodeError:
                print('Il file del database è corrotto! Creo un file vuoto...')
                time.sleep(2)
                pulisci_schermo()
                database = {}
                salva_database()
    except FileNotFoundError:
        database = {}
        salva_database()

    while True:
        print("Cosa vuoi fare? (Premi invio per uscire dal programma)")
        print(" 1) Visualizza tabella")
        print(" 2) Crea tabella")
        print(" 3) Modifica tabella")
        print(" 4) Elimina tabella")
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
