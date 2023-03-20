def PrintLengte(Iets):
    print("Lengte string",Iets,"is",len(Iets))

Tekst = "PYTHON IS EEN KLASSE TAAL"
LegeTekst = ""
Karakter = "a"
Tekst1 = "ABC"
Tekst2 = "DEF"
Provincies = "Er zijn 12 provincies in Nederland"

PrintLengte(Tekst)
PrintLengte(LegeTekst)
PrintLengte(Karakter)
PrintLengte(Tekst1+Tekst2)
PrintLengte(Tekst1)

p = Provincies[8:10]
print(p)