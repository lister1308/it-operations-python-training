# zinnengenerator
import random
# python -m pip install requests
import requests
# python -m pip install bs4
from bs4 import BeautifulSoup
#
import argparse
import TekstNaarSpraak
import zinnengenerator_dictv3 as woordenlijsten

# argumenten voor als code vanuit webinterface wordt aangeroepen
parser = argparse.ArgumentParser(description="Omschrijving: genereer een random zin of zelfs complete alinea")
parser.add_argument('--samenhang', action='store_true', help='Is er samenhang tussen de zinnen, default 1 = ja, of 0 = nee')
parser.add_argument('--print', default='alinea', help='Print een zin of alinea')
parser.add_argument('--aantal', default='5', type=int, help='Print aantal zinnen of zinnen in een alinea')
parser.add_argument('--sound', action='store_true', help='geef deze mee als je zin wilt laten uitspreken')
parser.add_argument('--thema',default=None,help="themas zijn: voorwerpen,meubels,mensen,dieren,voertuigen,plaatsen,gebouwen,bomen,planten")
args = parser.parse_args()

if args.thema == 'random':
    args.thema = None


# Functie voor het bepalen van het lidwoord. Afgestapt van bepaling dmv logica in de functie aangezien 
# er te veel uitzonderingen zijn en dit zorgt voor niet lekker lopende zinnen.
def lidwoord(zelfstandig_naamwoord):
    # uitzondering voor funfactor namen docenten
    if zelfstandig_naamwoord in woordenlijsten.docenten:
        return ""
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
        thema = random.choice(list(woordenlijsten.bijvoeglijke_naamwoorden.keys()))
    return random.choice(woordenlijsten.bijvoeglijke_naamwoorden[thema])

#<koppelwoord> ::= “op” | “in” | “voor” | “onder” | …
def koppelwoord(thema, werkwoord):   
    return random.choice(woordenlijsten.werkwoorden[thema][werkwoord])

#<lijdend_voorwerp> ::= <onderwerp>
def lijdend_voorwerp(thema=None):
    # if thema is None:
        # thema = random.choice(list(lijdende_voorwerpen.keys()))
    #return random.choice(lijdende_voorwerpen[thema])
    return onderwerp(thema)

#<werkwoord> ::= “staat” | “zit” | “ligt” | …
def werkwoord(thema=None):
    if thema is None:
        thema = random.choice(list(woordenlijsten.werkwoorden.keys()))
    return random.choice(list(woordenlijsten.werkwoorden[thema].keys()))

#<zelfstandig_naamwoord> ::= “glas” | “pen” | “netwerkkabel” | …
def zelfstandig_naamwoord(thema=None):
    if thema is None:
        thema = random.choice(list(woordenlijsten.zelfstandige_naamwoorden.keys()))
    return random.choice(woordenlijsten.zelfstandige_naamwoorden[thema])

#<onderwerp> ::= <lidwoord> <zelfstandig_naamwoord> | <lidwoord> <bijvoegelijk_naamwoord> <zelfstandig_naamwoord>
def onderwerp(thema=None):
    zsn = zelfstandig_naamwoord(thema)
    # Maak het random of er een bijvoeglijk naamwoord voor het zelfstandig naamwoord staat
    if random.choice([True, False]):
        return lidwoord(zsn) + " " + zsn
    else:
        return lidwoord(zsn) + " " + bijvoeglijk_naamwoord(thema) + " " + zsn

#<zin> ::= <onderwerp> <werkwoord> “.” | <onderwerp> <werkwoord> <koppelwoord> <lijdend_voorwerp> “.”

class Volzin:
    def __init__(self, soort=None, thema=None, onderw=None):
        if thema is None:
            thema = random.choice(list(woordenlijsten.themas.keys()))
        if onderw is None:
            onderw = onderwerp(thema)
        self.thema = thema
        self.onderwerp = onderw
        self.werkwoord = werkwoord(thema)
        self.koppelwoord = koppelwoord(thema, self.werkwoord)
        self.lijdend_voorwerp_thema = random.choice(woordenlijsten.themas[thema])
        # Kies een random bijpassen thema bij het onderwerp thema
        self.lijdend_voorwerp = lijdend_voorwerp(self.lijdend_voorwerp_thema)
        # Zorg dat het onderwerp en lijdend voorwerp niet hetzelfde zelfstandige naamwoord bevatten
        while (self.lijdend_voorwerp.split())[-1] == (self.onderwerp.split())[-1]:
            self.lijdend_voorwerp = lijdend_voorwerp(thema) 
        #Simpele of uitgebreide zinnen
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
            zin = Volzin(soort="Uitgebreid",thema=args.thema)
            alinea = alinea + " " + zin.zin

    if samenhang == 1:
        zin1 = Volzin(soort="Uitgebreid",thema=args.thema)
        alinea = zin1.zin
        for _ in range(aantalzinnen-1):
            onderwerpzin = zin1.lijdend_voorwerp
            zin2 = Volzin(soort="Uitgebreid",onderw=onderwerpzin,thema=args.thema)
            alinea = alinea + " " + zin2.zin
            zin1=zin2
            
    return alinea

# huiswerk:
# Functies opnemen in een module
# keuze van de woorden in de dictionaries: voorstel Wouter verder uitwerken
# fun factor diverse mogelijkheden: web (opties in webinterface voor thema/aantal/geluid/zin vs alinea) 
# wordt thema goed gebruikt nu, themacontrole? Bert
# plaatjes van henny, rudi, evert maken ahv zakelijk tekenen: Tom
# yoda mode (osv mode), groningse mode
#
if args.print == 'zin':
    for _ in range(int(args.aantal)):
       mijn_zin = Volzin(thema=args.thema)
       print(mijn_zin)
       if args.sound:
            TekstNaarSpraak.VertelMij(mijn_zin)
else:
    mijn_alinea = alinea(int(args.samenhang),int(args.aantal))
    print(mijn_alinea)
    if args.sound:
        TekstNaarSpraak.VertelMij(mijn_alinea)
