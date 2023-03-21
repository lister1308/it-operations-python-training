def vraag_aantal():
    getal = int(input("Voer een getal in: "))
    assert getal > 0, "Getal moet groter dan 0 zijn"
    return getal

#print (vraag_aantal())

lijst = [0.5,1,2]

laatste_getal = lijst[len(lijst)-1]
een_na_laatste_getal = lijst[len(lijst)-2]

nieuwegetal = laatste_getal + een_na_laatste_getal

lijst.append(nieuwegetal)

print(lijst)

