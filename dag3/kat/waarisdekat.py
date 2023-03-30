# waar is de kat
#
import random

# definieer variabelen
aantal_dozen = 5
doos_met_kat = 0
aantal_pogingen = 1
doos_te_openen = 0
kat_gevonden = False

def verstop_kat():
    # maak functie die een random getal terug geeft tussen 1 en max aantal dozen
    return (random.randint(1,aantal_dozen))

def welke_doos():
    # vraag gebruiker om een doos op te geven tussen 1 en max aantal_dozen
    # doos 0 = stoppen
    # geef terug doos nummer
    doos = 1 # zet op 1 om de lus in te gaan
    while doos != 0 or doos > aantal_dozen:
        doos = input(f"In welke doos zit de kat (tik 0 om te stoppen, doos tussen 1 en {aantal_dozen})? ")
        if not doos.isnumeric():
            print("Je moet een cijfer opgeven!")
            doos = 1
            continue
        elif int(doos) > aantal_dozen or int(doos) < 0: 
            print("Cijfer moet tussen 1 en {aantal_dozen} zitten")
            doos = 1
            continue
        else:
            return int(doos)

def controleer_inhoud(doos,dooskat):
    # kijk of opgegeven doos is doos waar kat zit
    # geef terug True of False 
    # Lucas
    if doos == dooskat:
        return True
    else:
        return False

def verplaats_kat(doos_met_kat):
    # verplaats de kat, 1 naar links of rechts
    # als in 1, kan je alleen naar 2, als in aantal_dozen, dan alleen naar links
    # geeft nieuwe doos terug

    '''als doos_met_kat is 1 dan
          doos_met_kat ← doos_met_kat + 1
       anders als doos_met_kat is aantal_dozen dan
         doos_met_kat ← doos_met_kat – 1
       anders
          doos_met_kat ← doos_met_kat + toevalsgetal: -1 of 1
     '''
    if doos_met_kat == 1:
        # verplaats kat naar rechts
        doos_met_kat += 1
    elif doos_met_kat == aantal_dozen:
        # verplaats kat naar links
        doos_met_kat -= 1
    else:
        # -1 is naar links, 1 is naar rechts
        keuze=[-1,1]

        waarde = int(random.choice(keuze))
        if waarde == -1:
            doos_met_kat -= 1
        else:
            doos_met_kat += 1

    return doos_met_kat

# lus die loopt zolang kat gevonden = False
# doos_met_kat = verstop_kat()
doos_met_kat = verstop_kat()
while not kat_gevonden:
    # doos_te_openen = welke_doos()
    doos_te_openen = welke_doos()
    # als controleer_inhoud(doos_te_openen,doos_met_kat) is:
    if controleer_inhoud(doos_te_openen,doos_met_kat) == True:
        print(f"Geweldig, je hebt onze kat gevonden in {aantal_pogingen} pogingen!")
        kat_gevonden = True
    else:
        print("Verkeerde doos, de kat loopt al weer verder")
        aantal_pogingen += 1
        doos_met_kat = verplaats_kat(doos_met_kat)
    # waar -> kat gevonden, stop lus
    # niet waar -> verplaats_kat(doos_met_kat)