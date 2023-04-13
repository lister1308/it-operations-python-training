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
    "voorwerpen": ["roze", "glanzende", "oude", "duurzame"],
    "meubels": ["comfortabele", "moderne", "klassieke", "verstelbare"],
    "mensen": ["sympathieke", "slimme", "grappige", "aardige"],
    "dieren": ["schattige", "speelse", "lieve", "trouwe"],
    "voertuigen": ["snelle", "efficiënte", "ruime", "luxueuze"],
    "plaatsen": ["drukke", "schone", "gezellige", "veilige"],
    "gebouwen": ["romantische", "chique", "historische", "unieke"],
    "bomen": ["grote", "oude", "mooie", "geurende"],
    "planten": ["groene", "bonte", "gezonde", "kleurrijke"]
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

koppelwoorden = ["op", "in", "voor", "onder"]

#<lidwoord> ::= “de” | “het” | “een”
#def lidwoord():
#    lidwoorden = ["de", "het", "een"]
#    return random.choice(lidwoorden)

# alternatief
def lidwoord(zelfstandig_naamwoord):
    if zelfstandig_naamwoord[0] in ['a', 'e', 'i', 'o', 'u']:
        return 'het'
    else:
        return 'de'
        

#<bijvoegelijk_naamwoord> ::= “blauwe” | “grote” | “volle” | …
def bijvoeglijk_naamwoord(thema=None):
    if thema is None:
        thema = random.choice(list(bijvoeglijke_naamwoorden.keys()))
    return random.choice(bijvoeglijke_naamwoorden[thema])

#<koppelwoord> ::= “op” | “in” | “voor” | “onder” | …
def koppelwoord(): 
    return random.choice(koppelwoorden)

#<lijdend_voorwerp> ::= <onderwerp>
def lijdend_voorwerp(thema=None):
    if thema is None:
        thema = random.choice(list(lijdende_voorwerpen.keys()))
    return random.choice(lijdende_voorwerpen[thema])

#<werkwoord> ::= “staat” | “zit” | “ligt” | …
def werkwoord(thema=None):
    if thema is None:
        thema = random.choice(list(werkwoorden.keys()))
    return random.choice(werkwoorden[thema])

#<zelfstandig_naamwoord> ::= “glas” | “pen” | “netwerkkabel” | …
def zelfstandig_naamwoord(thema=None):
    if thema is None:
        thema = random.choice(list(zelfstandige_naamwoorden.keys()))
    return random.choice(zelfstandige_naamwoorden[thema])

#<onderwerp> ::= <lidwoord> <zelfstandig_naamwoord> | <lidwoord> <bijvoegelijk_naamwoord> <zelfstandig_naamwoord>
def onderwerp(thema=None):
    zsn = zelfstandig_naamwoord(thema)
    if random.choice([True, False]):
        return lidwoord(zsn) + " " + zsn
    else:
        return lidwoord(zsn) + " " + bijvoeglijk_naamwoord(thema) + " " + zsn

#<zin> ::= <onderwerp> <werkwoord> “.” | <onderwerp> <werkwoord> <koppelwoord> <lijdend_voorwerp> “.”
def volzin(thema=None):
    if thema is None:
        thema = random.choice(list(zelfstandige_naamwoorden.keys()))
    if random.choice([True, False]):
        zin = onderwerp(thema) + " " + werkwoord(thema) + "."
    else:
        zin = onderwerp(thema) + " " + werkwoord(thema) + " " + koppelwoord() + " " + lijdend_voorwerp(thema) + "."
    return zin.capitalize()

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
print(volzin())