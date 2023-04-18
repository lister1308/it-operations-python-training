# zinnengenerator
import random
# python -m pip install requests
import requests
# python -m pip install bs4
from bs4 import BeautifulSoup
#
import argparse

# argumenten voor als code vanuit webinterface wordt aangeroepen
parser = argparse.ArgumentParser(description="Omschrijving: genereer een random zin of zelfs complete alinea")
parser.add_argument('-s', '--samenhang', default=1, help='Is er samenhang tussen de zinnen, default 1 = ja, of 0 = nee')
parser.add_argument('-p', '--print', default='alinea', help='Print een zin of alinea')
parser.add_argument('-a', '--aantal', default='5', type=int, help='Print aantal zinnen of zinnen in een alinea')
parser.add_argument('--sound', action='store_true', help='geef deze mee als je zin wilt laten uitspreken')
args = parser.parse_args()

import TekstNaarSpraak

# Lijsten van woorden voor elk thema
zelfstandige_naamwoorden = {
    "voorwerpen": ["telefoon", "sleutel", "sjaal", "zonnebril", "muts", "revolver"],
    "meubels": ["bank", "bureau", "kruk", "kast", "tafel", "dressoir"],
    "mensen": ["vriend", "familie", "collega", "leraar", "Sinterklaas", "politieagent", "verpleegkundige", "chirurg", "helpdeskmedewerker", "systeembeheerder"],
    "dieren": ["hond", "kat", "konijn", "vogel", "rups", "kikker", "slang"],
    "voertuigen": ["fiets", "auto", "bus", "trein", "e-bike", "vrachtwagen", "brandweerauto"],
    "plaatsen": ["park", "strand", "supermarkt", "ziekenhuis", "bos"],
    "gebouwen": ["kasteel", "museum", "restaurant", "hotel", "vliegveld"],
    "bomen": ["eik", "beuk", "den", "esdoorn", "kastanje"],
    "planten": ["cactus", "orchidee", "tulp", "varen", "klimop", "monstera", "duizendknoop"]
}

lijdende_voorwerpen = {
    "voorwerpen": ["kabel", "oplader", "adapter", "toetsenbord", "patchkabel"],
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
    "meubels": ["comfortabele", "moderne", "klassieke", "verstelbare", "lelijke"],
    "mensen": ["sympathieke", "slimme", "grappige", "aardige"],
    "dieren": ["schattige", "speelse", "lieve", "trouwe"],
    "voertuigen": ["snelle", "efficiënte", "ruime", "luxueuze", "elektrische"],
    "plaatsen": ["drukke", "schone", "gezellige", "veilige"],
    "gebouwen": ["romantische", "chique", "historische", "unieke"],
    "bomen": ["grote", "oude", "mooie", "geurende"],
    "planten": ["groene", "bonte", "gezonde", "kleurrijke", "geurige"]
}

'''
Kun je een python dictionary maken die voor de onderstaande thema's 4 werkwoorden bevat in de enkelvoudige persoonsvorm in de vorm Hij/Zij/Het.

- voorwerpen
- meubels
- mensen
- dieren
- voertuigen
- plaatsen
- gebouwen
- bomen
- planten
'''
werkwoorden = {
    "voorwerpen": ["pakt", "zet", "duwt", "tilt", "grijpt", "gooit"],
    "meubels": ["stoft", "verplaatst", "monteert", "polijst", "poetst"],
    "mensen": ["praat", "werkt", "loopt", "luistert", "knuffelt"],
    "dieren": ["voedt", "aait", "traint", "observeert"],
    "voertuigen": ["rijdt", "parkeert", "onderhoudt", "tankt", "wast", "poetst"],
    "plaatsen": ["bezoekt", "ontdekt", "verlaat", "fotografeert", "bewondert"],
    "gebouwen": ["betreedt", "verlaat", "renoveert", "bewondert"],
    "bomen": ["plant", "snoeit", "observeert", "klimt", "knuffelt", "stekt",],
    "planten": ["plant", "verpot", "snoeit", "observeert", "stekt"]
}

koppelwoorden = ["op", "in", "voor", "onder"]

# Functie voor het bepalen van het lidwoord. Afgestapt van bepaling dmv logica in de functie aangezien 
# er te veel uitzonderingen zijn en dit zorgt voor niet lekker lopende zinnen.
def lidwoord(zelfstandig_naamwoord):
    try: 
        url = f"https://anw.ivdnt.org/article/{zelfstandig_naamwoord}"
        response = requests.get(url)
        # De HTML van de pagina parsen
        soup = BeautifulSoup(response.text, 'html.parser')

        # Het element vinden met de tag 'td' dat volgt op een element met de tekst 'Lidwoord'
        td_element = soup.find('th', string='Lidwoord').find_next('td')

        # Het lidwoord ophalen uit de tekst tussen de tags
        result = td_element.text.strip().lower()
                
        if result in ["het", "de"]:
            return result
        else:
            return "een"
    except:
        return "een"


# alternatief
#def lidwoord(zelfstandig_naamwoord):
#    if zelfstandig_naamwoord[0] in ['a', 'e', 'i', 'o', 'u']:
#        return 'het'
#    else:
#        return 'de'
        

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
    #return random.choice(lijdende_voorwerpen[thema])
    return onderwerp(thema)

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

class Volzin:
    def __init__(self, soort=None, thema=None, onderw=None):
        if thema is None:
            thema = random.choice(list(zelfstandige_naamwoorden.keys()))
        if onderw is None:
            onderw = onderwerp(thema)
        self.thema = thema
        self.onderwerp = onderw
        self.werkwoord = werkwoord(thema)
        self.koppelwoord = koppelwoord()
        self.lijdend_voorwerp = lijdend_voorwerp(thema)
        if soort == "Simpel":
            self.zin = self.onderwerp + " " + self.werkwoord + "."
        elif soort == "Uitgebreid":
            self.zin = self.onderwerp + " " + self.werkwoord + " " + self.koppelwoord + " " + self.lijdend_voorwerp + "."
        else:
            if random.choice([True, False]):
                self.zin = self.onderwerp + " " + self.werkwoord + "."
            else:
                self.zin = self.onderwerp + " " + self.werkwoord + " " + self.koppelwoord + " " + self.lijdend_voorwerp + "."
        self.zin = self.zin.capitalize()
        
    def __str__(self):
        return self.zin
'''
def volzin(thema=None):
    if thema is None:
        thema = random.choice(list(zelfstandige_naamwoorden.keys()))

    if random.choice([True, False]):
        zin = onderwerp(thema) + " " + werkwoord(thema) + "."
    else:
        zin = onderwerp(thema) + " " + werkwoord (thema) + " " + koppelwoord() + " " + lijdend_voorwerp(thema) + "."
    return zin.capitalize()
'''

# Meerdere zinnen met een bepaalde samenhang vormen samen een alinea:
# <alinea> ::= <zin> | <zin> <zin> | <zin> <zin> <zin> | …
# De samenhang wordt veroorzaakt doordat de zinnen in een alinea naar elkaar verwijzen, 
# over het zelfde onderwerp verhalen of overeenkomstige onderwerpen bevatten. 
# Deze samenhang wordt in te realiseren programma bestuurd met de parameter samenhang.

# Met de parameter samenhang in de functie alinea wordt bedoeld, de mate waarin een onderwerp in 
# de volgende zin herhaald wordt. 

# Met 0 is er geen herhaling, met 1 wordt een gebruikt lijdend voorwerp in de volgende zin als 
# onderwerp gebruikt, enzovoorts.

# Voorbeelden
# Het volle glas staat op de tafel. De kat loopt door de kamer. (samenhang 0)
# Het volle glas staat op de tafel. De tafel staat in de kamer. (samenhang 1)

def alinea (samenhang = 1, aantalzinnen = 2):
    alinea = ""
    if samenhang == 0:
        for _ in range(aantalzinnen):
            zin = Volzin(soort="Uitgebreid")
            alinea = alinea + " " + zin.zin

    if samenhang == 1:
        zin1 = Volzin(soort="Uitgebreid")
        alinea = zin1.zin
        for _ in range(aantalzinnen-1):
            onderwerpzin = zin1.lijdend_voorwerp
            zin2 = Volzin(soort="Uitgebreid",onderw=onderwerpzin)
            alinea = alinea + " " + zin2.zin
            zin1=zin2
            
    return alinea

# huiswerk:
# Functies opnemen in een module
# geen dubbele onderwerpen in 1 zin, zelfde voor bijvoeglijk naamwwoord: Lucas
# keuze van de woorden in de dictionaries: Erwin
# stem in nederlands en omzetten naar functie die je aanroept met zin: Frank / Bert
# nadenken over alinea: Wouter
# fun factor diverse mogelijkheden: web / geluid / ascii art, wat wordt uiteindelijke presentatie?
# wordt thema goed gebruikt nu, themacontrole? Bert
# plaatjes van henny, rudi, evert maken ahv zakelijk tekenen: Tom
# yoda mode (osv mode), groningse mode
#
if args.print == 'zin':
    for _ in range(int(args.aantal)):
       mijn_zin = Volzin()
       print(mijn_zin)
       if args.sound:
            TekstNaarSpraak.VertelMij(mijn_zin)
else:
    mijn_alinea = alinea(int(args.samenhang),int(args.aantal))
    print(mijn_alinea)
    if args.sound:
        TekstNaarSpraak.VertelMij(mijn_alinea)
