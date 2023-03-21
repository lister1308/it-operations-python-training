#
# '''' Programma om de fibonaccie reeks mee te berekenen ''''
def fibonaccilijst(aantal_getallen):
    teller = aantal_getallen
    while teller > 0:
        laatste_getal = start_lijst[len(start_lijst)-1]
        een_na_laatste_getal = start_lijst[len(start_lijst)-2]

        nieuwe_getal = laatste_getal + een_na_laatste_getal

        start_lijst.append(nieuwe_getal)
        teller -= 1


# Functie om aantal getallen op te vragen
def vraag_aantal():
    getal = int(input("Voer een getal in: "))
    assert getal > 0, "Getal moet groter dan 0 zijn"
    return getal


# Lijst met getallen 0.5, 1 en 2 waarmee gestart wordt. Deze lijst wordt niet aangepast.
# 
start_lijst = [0.5, 1, 2]

getal = vraag_aantal()

if getal <=3:
    teller = 3 - getal
    while teller > 0:
        start_lijst.pop()
        teller -= 1
else:
    fibonaccilijst(getal-3)



print(start_lijst)





    