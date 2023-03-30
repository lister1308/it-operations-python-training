# waar is de kat
#
import random

# definieer variabelen
aantal_dozen = 5
doos_met_kat = 0
aantal_pogingen = 0
doos_te_openen = 0
kat_gevonden = False

def verstop_kat():
    # maak functie die een random getal terug geeft tussen 1 en max aantal dozen

def welke_doos():
    # vraag gebruiker om een doos op te geven tussen 1 en max aantal_dozen
    # doos 0 = stoppen
    # geef terug doos nummer

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
        doos_met_kat += random.choice(keuze)



# lus die loopt zolang kat gevonden = False
# doos_met_kat = verstop_kat()
while not kat_gevonden:
    # doos_te_openen = welke_doos()
    # als controleer_inhoud(doos_te_openen,doos_met_kat) is:
    # waar -> kat gevonden, stop lus
    # niet waar -> verplaats_kat(doos_met_kat)