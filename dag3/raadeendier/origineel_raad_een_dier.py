# Het programma begint met een basisset aan dieren
# De gebruikte datastructuur is een Python dictionary

dieren = {
    'vraag': 'Heeft het dier 4 poten?',
    'nee': {
        'vraag': 'Kruipt het op bladeren?',
        'ja':'rups',
        'nee':'huismus'
    },
    'ja': 'olifant'
}

# Herhalen zolang de gebruiker dat wil
def raad_het_dier():
    print('Neem een dier in gedachten...')
    prompt = 'Ben je er klaar voor?'
    while vraag_ja_nee(prompt):
        doorloop_dieren_boomstructuur(dieren)
        prompt = 'Wil je nog een keer spelen?'

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
    if vraag_ja_nee('Is je dier misschien een ' + blad + '?'):
        print('Yes! Ik het het geraden! Ik ben zo goed!')
    else:
        bewaar_nieuw_dier(stam, welke_kant(richting), blad)

def bewaar_nieuw_dier(hogere_tak, kant, oud_dier):
    nieuw_dier = input('Oh, wat jammer dat ik het niet heb geraden! Welk dier zat je aan te denken? ')
    if nieuw_dier.startswith('een '):
        nieuw_dier = nieuw_dier[4:len(nieuw_dier)]
    nieuwe_vraag = input('En welke vraag had ik moeten stellen om onderscheid te maken tussen een ' + oud_dier.lower() + ' en een ' + nieuw_dier.lower() + '? ')

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
    return is_ja(antwoord)

def is_ja(tekst):
    if tekst.lower().startswith('j'):
        return True
    else:
        return False

raad_het_dier()
