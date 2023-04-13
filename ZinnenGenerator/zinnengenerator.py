# zinnengenerator
import random
# bestand met daarin de dictionaries
# import zinnengenerator_dict.py

# Lijsten van woorden voor elk thema
zelfstandige_naamwoorden = {
    "voorwerpen": ["telefoon", "sleutel", "sjaal", "zonnebril"],
    "meubels": ["bank", "bureau", "kruk", "kast"],
    "mensen": ["vriend", "familie", "collega", "leraar"],
    "dieren": ["hond", "kat", "konijn", "vogel"],
    "voertuigen": ["fiets", "auto", "bus", "trein"],
    "plaatsen": ["park", "strand", "supermarkt", "ziekenhuis"],
    "gebouwen": ["kasteel", "museum", "restaurant", "hotel"],
    "bomen": ["eik", "beuk", "den", "esdoorn"],
    "planten": ["cactus", "orchidee", "tulp", "varen"]
}

lijdende_voorwerpen = {
    "voorwerpen": ["kabel", "oplader", "adapter", "toetsenbord"],
    "meubels": ["kussen", "plaid", "stoelkussen", "onderzetter"],
    "mensen": ["brief", "cadeau", "paraplu", "tas"],
    "dieren": ["bal", "speeltje", "riem", "voerbak"],
    "voertuigen": ["helm", "stoelhoes", "sneeuwkettingen", "dakdragers"],
    "plaatsen": ["karretje", "tas", "parasol", "koelbox"],
    "gebouwen": ["menukaart", "servet", "wijnkaart", "asbak"],
    "bomen": ["blad", "eikel", "dop", "tak"],
    "planten": ["bloem", "blad", "pot", "gieter"]
}

bijvoeglijke_naamwoorden = {
    "voorwerpen": ["roze", "glanzend", "oud", "duurzaam"],
    "meubels": ["comfortabel", "modern", "klassiek", "verstelbaar"],
    "mensen": ["sympathiek", "slim", "grappig", "aardig"],
    "dieren": ["schattig", "speels", "lief", "trouw"],
    "voertuigen": ["snel", "efficiënt", "ruim", "luxueus"],
    "plaatsen": ["druk", "schoon", "gezellig", "veilig"],
    "gebouwen": ["romantisch", "chique", "historisch", "uniek"],
    "bomen": ["groot", "oud", "mooi", "geurend"],
    "planten": ["groen", "bont", "gezond", "kleurrijk"]
}

werkwoorden = {
    "voorwerpen": ["vasthouden", "opladen", "gebruiken", "verliezen"],
    "meubels": ["schuiven", "verstellen", "monteren", "schoonmaken"],
    "mensen": ["ontmoeten", "helpen", "bezoeken", "adviseren"],
    "dieren": ["voeden", "aaien", "trainen", "uitlaten"],
    "voertuigen": ["besturen", "onderhouden", "wassen", "parkeren"],
    "plaatsen": ["bezoeken", "wandelen", "shoppen", "picknicken"],
    "gebouwen": ["bezichtigen", "reserveren", "betreden", "verlaten"],
    "bomen": ["planten", "snoeien", "verzorgen", "kappen"],
    "planten": ["water geven", "verpotten", "snoeien", "mesten"]
}

def lidwoord():
    lidwoorden = ["de", "het", "een"]
    return random.choice(lidwoorden)

# alternatief
#def lidwoord(zelfstandig_naamwoord):
#    if zelfstandig_naamwoord[0] in ['a', 'e', 'i', 'o', 'u']:
#        return random.choice['het','een']
#    else:
#        return random.choice['de', 'een']

def zelfstandig_naamwoord(thema=None):
    if thema is None:
        thema = random.choice(list(zelfstandige_naamwoorden.keys()))
    return random.choice(zelfstandige_naamwoorden[thema])

# huiswerk tijdelijke bestanden
# vermeld onder je module welke functies er in zitten
#
#import lucas.py
#
#
#import bert.py
#
#
#import frank.py
#
#
#import wouter.py
#
#
#import tom.py
#
#
#import erwin.py
#
#
"""
- dictionary van: lidwoord, zelfstandig_naamwoord, lijdend_voorwerp, bijvoeglijk_naamwoord, werkwoord, koppelwoord
- functie met als aanroep, dictionary, geeft terug random entry
- bij zin, eerst zelfstandig naamwoord, dan lidwoord
"""
print(lidwoord())