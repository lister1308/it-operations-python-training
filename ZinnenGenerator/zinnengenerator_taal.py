import random
import requests
from bs4 import BeautifulSoup
import zinnengenerator_dictv3 as woordenlijsten


# Functie voor het bepalen van het lidwoord. Afgestapt van bepaling dmv logica in de functie aangezien 
# er te veel uitzonderingen zijn en dit zorgt voor niet lekker lopende zinnen.
def lidwoord(zelfstandig_naamwoord):
    # Uitzondering voor funfactor namen docenten
    if zelfstandig_naamwoord.lower() in woordenlijsten.docenten:
        return ""
    # Try voor het geval de pagina niet bereikbaar is/een foutmelding heeft of het woord niet gevonden kan worden.
    # In dat geval return dan "een".
    try: 
        url = f"https://anw.ivdnt.org/article/{zelfstandig_naamwoord}"
        response = requests.get(url)
        # De HTML van de pagina parsen
        soup = BeautifulSoup(response.text, 'html.parser')
        # Zoek de rijtitel (th) 'Lidwoord' in de HTML broncode en zoek vervolgens de volgende cel (td) in de rij en haal hiervan de waarde op.
        td_element = soup.find('th', string='Lidwoord').find_next('td')
        result = td_element.text.strip().lower()
                
        if result in ["het", "de"]:
            return result
        else:
            return "een"
    except:
        return "een"


# Alternatief met logica
#def lidwoord(zelfstandig_naamwoord):
#    if zelfstandig_naamwoord[0] in ['a', 'e', 'i', 'o', 'u']:
#        return 'het'
#    else:
#        return 'de'
        

# Haal het bijvoeglijk naamwoord op uit de dictionary passend bij het onderwerpthema.
# Wanneer geen thema meegegeven, kies dan random een thema uit de dictionary. 
def bijvoeglijk_naamwoord(thema=None):
    if thema is None:
        thema = random.choice(list(woordenlijsten.bijvoeglijke_naamwoorden.keys()))
    return random.choice(woordenlijsten.bijvoeglijke_naamwoorden[thema])

# Haal het koppelwoord (voorzetsel) op uit de dictionary, passend bij het werkwoord 
# binnen het onderwerpthema. 
def koppelwoord(thema, werkwoord):   
    return random.choice(woordenlijsten.werkwoorden[thema][werkwoord])

# 
def lijdend_voorwerp(thema=None):
    return onderwerp(thema)

# Haal het werkwoord op uit de dictionary passend bij het onderwerpthema.
# Wanneer geen thema meegegeven, kies dan random een thema uit de dictionary. 
def werkwoord(thema=None):
    if thema is None:
        thema = random.choice(list(woordenlijsten.werkwoorden.keys()))
    return random.choice(list(woordenlijsten.werkwoorden[thema].keys()))

# Haal het zelfstandig naamwoord op uit de dictionary passend bij het onderwerpthema.
# Wanneer geen thema meegegeven, kies dan random een thema uit de dictionary. 
def zelfstandig_naamwoord(thema=None):
    if thema is None:
        thema = random.choice(list(woordenlijsten.zelfstandige_naamwoorden.keys()))
    return random.choice(woordenlijsten.zelfstandige_naamwoorden[thema])

# Bepaald het onderwerp van de zin
def onderwerp(thema=None):
    # Bepaal het zelfstandig naamwoord zodat deze ook kan worden gebruikt om het lidwoord op te halen
    zsn = zelfstandig_naamwoord(thema)
    # Maak het random of er een bijvoeglijk naamwoord voor het zelfstandig naamwoord staat
    # Verwijder de spatie aan het begin in het geval dat het lidwoord wegvalt
    if random.choice([True, False]):
        return (lidwoord(zsn) + " " + zsn).lstrip(' ')
    else:
        return (lidwoord(zsn) + " " + bijvoeglijk_naamwoord(thema) + " " + zsn).lstrip(' ')

# Genereer een volzin
class Volzin:
    def __init__(self, soort=None, thema=None, onderw=None):
        if thema is None:
            thema = random.choice(list(woordenlijsten.themas.keys()))
        if onderw is None:
            onderw = onderwerp(thema)
        if soort is None:
            soort = random.choice(["Simpel", "Uitgebreid"])
        self.soort = soort
        self.thema = thema
        self.onderwerp = onderw

        self.werkwoord = werkwoord(self.thema)
        self.koppelwoord = koppelwoord(self.thema, self.werkwoord)
        self.lijdend_voorwerp_thema = random.choice(woordenlijsten.themas[self.thema])
        # Kies een random bijpassen thema bij het onderwerp thema
        self.lijdend_voorwerp = lijdend_voorwerp(self.lijdend_voorwerp_thema)
        # Zorg dat het onderwerp en lijdend voorwerp niet hetzelfde zelfstandige naamwoord bevatten
        # Haal voor het vergelijken het bijvoegelijke naamwoord er af
        while (self.lijdend_voorwerp.split())[-1] == (self.onderwerp.split())[-1]:
            self.lijdend_voorwerp = lijdend_voorwerp(self.thema) 
        #Simpele of uitgebreide zinnen
        if self.soort == "Simpel":
            self.zin = self.onderwerp + " " + self.werkwoord + "."
        elif self.soort == "Uitgebreid":
            self.zin = self.onderwerp + " " + self.werkwoord + " " + self.koppelwoord + " " + self.lijdend_voorwerp + "."
        # Expliciet alleen de de eerste letter van de zin Hoodfletter maken zodat andere hoodletters
        # in de zin behouden blijven. Dit is bij capatalize niet zo.
        self.zin = self.zin[:1].upper() + self.zin[1:]
        
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
#Genereer een alinea
def alinea (samenhang = 1, aantalzinnen = 2, thema=None):
    alinea = ""
    if thema is None:
        thema = random.choice(list(woordenlijsten.themas.keys()))
    if samenhang == 0:
        for _ in range(aantalzinnen):
            zin = Volzin(soort="Uitgebreid",thema=thema)
            alinea = alinea + " " + zin.zin

    if samenhang == 1:
        zin1 = Volzin(soort="Uitgebreid",thema=thema)
        alinea = zin1.zin
        for _ in range(aantalzinnen-1):
            onderwerpzin = zin1.lijdend_voorwerp
            zin2 = Volzin(soort="Uitgebreid",onderw=onderwerpzin,thema=zin1.lijdend_voorwerp_thema)
            alinea = alinea + " " + zin2.zin
            zin1=zin2
            
    return alinea
