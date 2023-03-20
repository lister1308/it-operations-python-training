# lijsten
print ("-"*100)
lijst = ["2xice tea", "kwark", "3xkoffie", "2xcola"]
print(lijst)
# toewijzen item aan variabele
lijst_item = lijst[2]
print(lijst_item)
# wijzigen variabel
lijst[2] = "4xkoffie"
print(lijst)
lijst += ["frikandelbroodje"]
# ga door lijst heen
for item in lijst:
    print(item)
print(lijst[2:4])
aanwezig = 'frikandelbroodje' in lijst
print("frikandelbroodje in lijst?",aanwezig)
print("hoeveel artikelen in lijst:",len(lijst))
print("Verwijder laatste uit lijst:",lijst.pop())
print(lijst)
print ("-"*100)
boodschappenlijst = [
    ['Ice Tea', 2],
    ['Cola Zero', 4],
    ['Tros Bananen', 4]
]

print(boodschappenlijst)
print("Voeg iets toe")
boodschappenlijst.append(["Eetrijpe avocado's",3,3,3])
print(boodschappenlijst)
print("Sorteer lijst")
boodschappenlijst.sort()
print(boodschappenlijst)

print("print van eerste artikel het aantal")
print(boodschappenlijst[0][1])
print ("-"*100)