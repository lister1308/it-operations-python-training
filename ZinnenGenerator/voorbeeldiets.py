# chatgpt ondersteuning

import random

data = {
    "voorwerpen": {
        "lidwoorden": ["het", "een"],
        "zelfstandig_naamwoorden": ["glas", "pen", "netwerkkabel"],
        "werkwoorden": ["ligt", "staat", "hangt"],
        "koppelwoorden": ["op", "in", "voor", "onder"],
        "bijvoeglijk_naamwoorden": ["blauwe", "grote", "volle"],
    },
    "meubels": {
        "lidwoorden": ["de", "het", "een"],
        "zelfstandig_naamwoorden": ["tafel", "stoel", "kapstok"],
        "werkwoorden": ["staat", "hangt", "ligt"],
        "koppelwoorden": ["op", "onder"],
        "bijvoeglijk_naamwoorden": ["grote", "ronde", "hoge"],
    }
}

def lidwoord(thema=None):
    if thema and thema in data:
        return random.choice(data[thema]["lidwoorden"])
    return random.choice([item for sublist in data.values() for item in sublist["lidwoorden"]])

def zelfstandig_naamwoord(thema=None):
    if thema and thema in data:
        return random.choice(data[thema]["zelfstandig_naamwoorden"])
    return random.choice([item for sublist in data.values() for item in sublist["zelfstandig_naamwoorden"]])

def werkwoord(thema=None):
    if thema and thema in data:
        return random.choice(data[thema]["werkwoorden"])
    return random.choice([item for sublist in data.values() for item in sublist["werkwoorden"]])

def koppelwoord():
    return random.choice([item for sublist in data.values() for item in sublist["koppelwoorden"]])

def bijvoegelijk_naamwoord(thema=None):
    if thema and thema in data:
        return random.choice(data[thema]["bijvoeglijk_naamwoorden"])
    return random.choice([item for sublist in data.values() for item in sublist["bijvoeglijk_naamwoorden"]])

def lijdend_voorwerp(thema=None, onderwerp=None):
    if onderwerp is None:
        onderwerp = zelfstandig_naamwoord(thema)
    return onderwerp

def volzin(thema=None):
    onderwerp = f"{lidwoord(thema)} {zelfstandig_naamwoord(thema)}"
    werkwoord_1 = werkwoord(thema)
    bijv_nw = bijvoegelijk_naamwoord(thema)
    koppelw = koppelwoord()
    lijd_vo = lijdend_voorwerp(thema, onderwerp)

    if random.choice([True, False]):
        zin = f"{onderwerp} {werkwoord_1}."
    else:
        zin = f"{onderwerp} {werkwoord_1} {koppelw} {lijd_vo}."

    if random.choice([True, False]):
        zin = f"{bijv_nw} {zin}"

    return zin

def alinea(samenhang=0, thema=None):
    zinnen = [volzin(thema)]

    while samen
