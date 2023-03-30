# Testcode om de functie verplaats_kat te testen

import random

# definieer variabelen
aantal_dozen = 5
doos_met_kat = 0
aantal_pogingen = 0
doos_te_openen = 0
kat_gevonden = False




def verplaats_kat(doos_met_kat):
    # verplaats de kat, 1 naar links of rechts
    # als in 1, kan je alleen naar 2, als in aantal_dozen, dan alleen naar links
    # geeft nieuwe doos terug

       
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

    return doos_met_kat



doos_met_kat = verplaats_kat(doos_met_kat)
if doos_met_kat == 1:
    print('rechts')
else:
    print("links")

print(doos_met_kat)
