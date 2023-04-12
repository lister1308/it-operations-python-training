"""
Opdracht:
☐ Zorg ervoor dat de vragen en de dieren zo kort mogelijk worden opgeslagen, zonder voorzetsels (‘een’ kat) en zonder vraagtekens en hoofdletters
☐ Zorg ervoor dat de communicatie met de gebruiker wel netjes met volledige zinnen gebeurt
☑ Sla de data op in een bestand en vraag dit bij het opstarten van het programma weer op
☑ Gebruik de pickle of json module
☐ Maak het mogelijk om vragen achteraf te wijzigen
☐ Gebruik kleur en opmaak bij het tonen van vragen en antwoorden
☑ Maak een functie om alle dieren te laten zien
☐ Bouw leuke features in
"""

# Het programma begint met een basisset aan dieren
# De gebruikte datastructuur is een Python dictionary
from os.path import exists
import json

bestand = 'dieren.json'
alle_dieren = []
alle_vragen = []


def lees_dieren_in(bestand):
    if exists(bestand):
        with open(bestand,'r') as fp:
            dieren = json.load (fp)
    else:
        dieren = {
        'vraag': 'Heeft het dier 4 poten?',
            'nee': {
            'vraag': 'Kruipt het op bladeren?',
            'ja':'rups',
            'nee':'huismus'
            },
            'ja': 'olifant'
        }
        schrijf_dieren_weg(bestand,dieren)

    return dieren

def schrijf_dieren_weg(bestand,dieren):
    # save huidige dictionary in directory
    with open('dieren.json', 'w') as fp:
        json.dump(dieren, fp)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Herhalen zolang de gebruiker dat wil
def raad_het_dier():
    print(bcolors.WARNING + 'Neem een dier in gedachten...' + bcolors.ENDC)
    prompt = bcolors.OKGREEN + 'Ben je er klaar voor?' + bcolors.ENDC
    while vraag_ja_nee(prompt):
        doorloop_dieren_boomstructuur(dieren)
        prompt = bcolors.OKCYAN + 'Wil je nog een keer spelen?' + bcolors.ENDC
    schrijf_dieren_weg(bestand, dieren)

# Doorloop een tak
def doorloop_dieren_boomstructuur(tak):
    # We stellen eerst de vraag die op de tak beschikbaar is
    # De vraag heeft het formaat ['is'|'heeft'] het dier 'eigenschap'
    richting = vraag_ja_nee(tak['vraag'].capitalize() + '?')
    nieuwe_tak = lagere_tak(tak, richting)

    if dier_gevonden(nieuwe_tak):
        eindig_spel(nieuwe_tak, tak, richting)
    else:
        doorloop_dieren_boomstructuur(nieuwe_tak)

# Een dier is gevonden als de tak waarop we zitten eindigt in een blad,
# in plaats van in een lagere tak. Een blad is een string, een
# lagere tak is een dict. We controleren op een blad met de functie
# isinstance
def dier_gevonden(tak):
    is_blad = not isinstance(tak, dict)
    return is_blad

def eindig_spel(blad, stam, richting):
    if vraag_ja_nee(bcolors.OKCYAN + 'Is je dier misschien een ' + bcolors.BOLD + bcolors.HEADER + blad + '?' + bcolors.ENDC):
        print(bcolors.BOLD + bcolors.OKGREEN + 'Yes! Ik heb het geraden! Ik ben zo goed!' + bcolors.ENDC)
    else:
        bewaar_nieuw_dier(stam, welke_kant(richting), blad)

def bewaar_nieuw_dier(hogere_tak, kant, oud_dier):
    nieuw_dier = input(bcolors.OKCYAN + 'Oh, wat jammer dat ik het niet heb geraden! Welk dier zat je aan te denken? ' + bcolors.ENDC)
    if nieuw_dier.startswith('een '):
        nieuw_dier = nieuw_dier[4:len(nieuw_dier)]
    nieuwe_vraag = input(bcolors.OKCYAN + 'En welke vraag had ik moeten stellen om onderscheid te maken tussen een ' + bcolors.FAIL + oud_dier.lower() + bcolors.OKCYAN + ' en een ' + bcolors.OKGREEN + nieuw_dier.lower() + '? ' + bcolors.ENDC)

    hogere_tak[kant] = {
        'vraag': nieuwe_vraag.lower().rstrip('? ').lstrip(' ').replace('  ', ' '),
        'ja': nieuw_dier.lower(),
        'nee': oud_dier
    }

# Geef een deel van de boomstructuur terug die begint met
# ja of nee
def lagere_tak(tak, richting):
    if richting:
        return tak['ja']
    else:
        return tak['nee']

def welke_kant(ja):
    if ja:
        return 'ja'
    else:
        return 'nee'

def vraag_ja_nee(vraag):
    antwoord = input(vraag + ' ')
    if antwoord == "":
        menu()
    return is_ja(antwoord)

def is_ja(tekst):
    if tekst.lower().startswith('j'):
        return True
    else:
        return False

def verzamel_alle_vragen(data):
    # Als het huidige item een vraag is, voeg deze dan toe aan de lijst van vragen
    if (isinstance(data, dict)) and 'vraag' in data:
        alle_vragen.append(data['vraag'].capitalize() + '?')
    # Recursief doorgaan met zoeken naar vragen in de huidige dictionary
    for key in data:
        if isinstance(data[key], (dict, list)):
            verzamel_alle_vragen(data[key])

def verzamel_alle_dieren(data):
    # Als er een dier is gevonden voeg hem toe aan de lijst met alle dieren 
    # Zo niet, roep dan de functie nogmaals aan met de gevonden tak

    if dier_gevonden(data):
        alle_dieren.append(data.capitalize())
    
    else:
        if "ja" in data:
            verzamel_alle_dieren(data["ja"])
        if "nee" in data:
            verzamel_alle_dieren(data["nee"])

def toon_alle_dieren():
    verzamel_alle_dieren(dieren)
    print(bcolors.HEADER + 'Dit zijn alle dieren die ik ken:' + bcolors.ENDC)
    print(bcolors.WARNING + '\n'.join(sorted(alle_dieren)) + bcolors.ENDC)

def toon_alle_vragen():
    verzamel_alle_vragen(dieren)
    print(bcolors.HEADER + 'Dit zijn alle vragen die ik ken:' + bcolors.ENDC)
    print(bcolors.WARNING + '\n'.join(sorted(alle_vragen)) + bcolors.ENDC)

    
def menu():
    while True:
        print(bcolors.OKGREEN + '''
_  .-')     ('-.       ('-.     _ .-') _         ('-. .-.   ('-.   .-') _          _ .-') _              ('-.  _  .-')   
( \( -O )   ( OO ).-.  ( OO ).-.( (  OO) )       ( OO )  / _(  OO) (  OO) )        ( (  OO) )           _(  OO)( \( -O )  
 ,------.   / . --. /  / . --. / \     .'_       ,--. ,--.(,------./     '._        \     .'_   ,-.-') (,------.,------.  
 |   /`. '  | \-.  \   | \-.  \  ,`'--..._)      |  | |  | |  .---'|'--...__)       ,`'--..._)  |  |OO) |  .---'|   /`. ' 
 |  /  | |.-'-'  |  |.-'-'  |  | |  |  \  '      |   .|  | |  |    '--.  .--'       |  |  \  '  |  |  \ |  |    |  /  | | 
 |  |_.' | \| |_.'  | \| |_.'  | |  |   ' |      |       |(|  '--.    |  |          |  |   ' |  |  |(_/(|  '--. |  |_.' | 
 |  .  '.'  |  .-.  |  |  .-.  | |  |   / :      |  .-.  | |  .--'    |  |          |  |   / : ,|  |_.' |  .--' |  .  '.' 
 |  |\  \   |  | |  |  |  | |  | |  '--'  /      |  | |  | |  `---.   |  |          |  '--'  /(_|  |    |  `---.|  |\  \  
 `--' '--'  `--' `--'  `--' `--' `-------'       `--' `--' `------'   `--'          `-------'   `--'    `------'`--' '--'
              ''' + bcolors.ENDC)
        print("")
        print(bcolors.OKGREEN + "1. Speel het spel" + bcolors.ENDC)
        print(bcolors.WARNING + "2. Toon alle dieren" + bcolors.ENDC)
        print(bcolors.WARNING + "3. Toon alle vragen" + bcolors.ENDC)
        print(bcolors.OKBLUE + "4. Wijzig een vraag" + bcolors.ENDC)
        print('\n')
        keuze = input(bcolors.BOLD + bcolors.UNDERLINE + "Voer je keuze in (0-3): " + bcolors.ENDC)

        if keuze.isnumeric() and int(keuze) in range(0, 4):
            if keuze == "1":
                # Voer acties uit voor optie 1
                #print("Je hebt optie 1 gekozen.")
                raad_het_dier()
            elif keuze == "2":
                # Voer acties uit voor optie 2
                # print("Je hebt optie 2 gekozen.")
                toon_alle_dieren()
            elif keuze == "3":
                # Voer acties uit voor optie 3
                #print("Je hebt optie 3 gekozen.")
                toon_alle_vragen()
            elif keuze == "4":
                # Voer acties uit voor optie 3
                print("Je hebt optie 4 gekozen.")
            else:
                # Voer acties uit voor optie 0
                print("Doei!")
            break
        else:
            print(bcolors.FAIL + "Ongeldige keuze. Voer a.u.b. een getal tussen 1 en 3 in." + bcolors.ENDC)

dieren = lees_dieren_in(bestand)

menu()