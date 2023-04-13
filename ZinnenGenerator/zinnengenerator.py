# zinnengenerator
import random
# bestand met daarin de dictionaries
#import zinnengenerator_dict.py

def lidwoord():
    lidwoorden = ["de", "het", "een"]
    return random.choice(lidwoorden)

# alternatief
#def lidwoord(zelfstandig_naamwoord):
#    if zelfstandig_naamwoord[0] in ['a', 'e', 'i', 'o', 'u']:
#        return random.choice['het','een']
#    else:
#        return random.choice['de', 'een']


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