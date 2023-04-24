# zinnengenerator
import random
import argparse
import TekstNaarSpraak
import zinnengenerator_dictv3 as woordenlijsten
from zinnengenerator_taal import *

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
    mijn_alinea = alinea(int(args.samenhang),int(args.aantal), args.thema)
    print(mijn_alinea)
    if args.sound:
        TekstNaarSpraak.VertelMij(mijn_alinea)
