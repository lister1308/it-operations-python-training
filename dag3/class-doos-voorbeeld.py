class Doos:
    def __init__(self, breedte, hoogte, diepte):
        self.breedte = breedte
        self.hoogte = hoogte
        self.diepte = diepte
        self.label = None
        self.isOpen = True

    def __str__(self):
        if self.label is not None:
            return "Het label op deze doos zegt '" + self.label + "'"
        else:
            return "Er zit geen label op deze doos"

    def plaklabel(self, tekst):
        self.label = tekst

    def sluit(self, doeDicht):
        if doeDicht:
            self.isOpen = False
        else:
            self.isOpen = True

verhuisdoos = Doos(30,30,30)
print(verhuisdoos)
verhuisdoos.plaklabel("doos van lucas")
verhuisdoos.sluit(True)
print(verhuisdoos)

del verhuisdoos
try:
    print(verhuisdoos)
except:
    print("De functie print(verhuisdoos) werkt niet omdat deze met del verwijdert is")