# Spelen met woorden
# Wat Python code om alvast aan de slag te kunnen
# Het bestand 'woorden.txt.zip' staat op deze pagina
import random

# gebruik van kleuren op de prompt
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

# bestand met grote hoeveelheid aan woorden, open deze read-only
bestand = "woorden.txt"
bestand_met_woorden = open(bestand, "r") # alleen-lezen van tekst
# lijst_met_woorden = bestand_met_woorden.readlines()
lijst_met_woorden = bestand_met_woorden.read().splitlines()
bestand_met_woorden.close()

# zet een aantal variabelen op hun begin waarde
aantal_woorden = 0 # aantal woorden in de lijst
langestewoord = '' # wat is het langste woord
langstelengte = 0 # wat is de lengte van het langste woord
lijst_met_palindromen = [] # lijst met alle palindromen
alle_woorden = set() # set met alle woorden
alle_omgekeerde_woorden = set() # set met woorden omgekeerd

def verzamel_wat_statistieken():
  global langestewoord, langstelengte, aantal_woorden, alle_woorden
  for woord in lijst_met_woorden:
    # tellen langste woord
    lengte = len(woord)
    if lengte > langstelengte:
      langstelengte = lengte
      langstewoord = woord
  
    # bepalen palindroom
    woord_omgekeerd = ""
    woord_omgekeerd_lijst = reversed(woord)
    for letter in woord_omgekeerd_lijst:
      woord_omgekeerd += letter

    # maken sets
    alle_woorden.add(woord)
    alle_omgekeerde_woorden.add(woord_omgekeerd)

    if woord_omgekeerd == woord:
      lijst_met_palindromen.append(woord) 

    # tellen woorden, maar je kan ook lengte lijst bepalen om zelfde resultaat te krijgen
    aantal_woorden = aantal_woorden + 1

  print(f"Aantal woorden in bestand {bestand} is {bcolors.OKGREEN}{aantal_woorden}{bcolors.ENDC}")
  # langste woord
  print(f"Langste woord is {bcolors.OKGREEN}{langstewoord}{bcolors.ENDC} met lengte {bcolors.OKGREEN}{str(langstelengte)}{bcolors.ENDC}")
  # palindromen gevonden
  print(f"Aantal gevonden palindroom woorden is {bcolors.OKGREEN}{len(lijst_met_palindromen)}{bcolors.ENDC}")
  # vergelijk de 2 sets wat ze gemeenschappelijk hebben
  print(f"Alle woorden die omgekeerd ook bestaan zijn er {bcolors.OKGREEN}{len(alle_omgekeerde_woorden.intersection(alle_woorden))}{bcolors.ENDC}")

def vraag_om_woord():
  # vul een woord in, als deze leeg, return functie False
  mijnwoord = input("\nVul een woord in (leeg om te stoppen): ")
  if mijnwoord == "":
    return False
  # controle of woord voorkomt in de lijst
  if (mijnwoord in alle_woorden):
    print(f"Woord {bcolors.OKGREEN}{mijnwoord}{bcolors.ENDC} zelf is aanwezig in de lijst")
  else:
    print(f"Woord {bcolors.WARNING}{mijnwoord}{bcolors.ENDC} komt niet als volledig woord in lijst")
  # controle of woord voorkomt in de lijst als onderdeel van een ander woord
  print(f"Controleren of je woord {bcolors.OKGREEN}{mijnwoord}{bcolors.ENDC} onderdeel is van een ander woord ", end='') 
  woord_onderdeel = 0
  for woord in alle_woorden:
    if mijnwoord in woord and mijnwoord != woord:
      print(".", end='')
      woord_onderdeel += 1
  if woord_onderdeel > 0:
    print(f"\n{bcolors.OKGREEN}{str(woord_onderdeel)}{bcolors.ENDC} woorden gevonden waar {bcolors.OKGREEN}{mijnwoord}{bcolors.ENDC} onderdeel van is")
  else:
    print(f"\n{bcolors.WARNING}Niet gevonden dat deze ergens onderdeel van is{bcolors.ENDC}")
  # welke woorden kan je maken met letters van het woord
  """
  # zet mijnwoord in set
  set_mijnwoord = set(mijnwoord)
  for woord in alle_woorden:
    set_woord = set(woord)
    if set_woord == set_mijnwoord and len(woord) == len(mijnwoord):
      print(f"{bcolors.OKGREEN}{woord}{bcolors.ENDC} kan worden gemaakt uit {bcolors.OKBLUE}{mijnwoord}{bcolors.ENDC}")
  """
  #  anagrammen, sorted oplossing van Wouter, daarvoor gedaan door eerst zelf naar list te converteren met var_list = list(string) en dan var_list.sort.
  print (f"Zoeken naar anagrammen van het woord {bcolors.OKGREEN}{mijnwoord}{bcolors.ENDC}:")
  for woord in alle_woorden:
    if woord == mijnwoord:
      continue
    if (sorted(woord) == sorted(mijnwoord)):
      print(f"{bcolors.OKGREEN}{woord}{bcolors.ENDC}",end=' ')
  print("")

  """
  input("Druk op ENTER om verder te gaan")
  # wat rijmt er op dit woord?
  rijm_mijnwoord = mijnwoord[-2:]
  print(f"Mijn woord {bcolors.OKBLUE}{mijnwoord}{bcolors.ENDC} rijmt op",end=' ')
  for woord in alle_woorden:
    rijm_woord = woord[-2:]
    if rijm_mijnwoord == rijm_woord:
      print(f"{bcolors.OKGREEN}{woord}{bcolors.ENDC}",end=' ')

  print("")
  """
  return True

def speel_spelletje():
  random_woord = random.choice(list(alle_woorden))
  print(f"\nEr is een woord gekozen die je mag raden. De letters van het woord in alfabetische volgorde zijn: {bcolors.OKGREEN}",end='')
  sorted_random_woord = sorted(random_woord)
  for letter in sorted_random_woord:
    print(letter,end='')

  print(f"{bcolors.ENDC}\nWat is het woord (leeg = hint, tik iets om te raden of stoppen): ",end='')
  raad_woord = input(f"{bcolors.OKCYAN}")

  while raad_woord == '':
    random.shuffle(sorted_random_woord)
    print(f"{bcolors.ENDC}Als je niets tikt probeer ik je te helpen, shuffle woord: {bcolors.OKGREEN}",end='')
    for letter in sorted_random_woord:
      print(letter,end='')
    print(f"{bcolors.ENDC}\nWat is het woord (leeg = hint, tik iets om te raden of stoppen): ",end='')
    raad_woord = input(f"{bcolors.OKCYAN}")

  if raad_woord == random_woord:
    print(f"{bcolors.HEADER}Je hebt het geraden!!!!{bcolors.ENDC}")
  else:
    print(f"{bcolors.WARNING}Helaas, het woord was {bcolors.OKGREEN}{random_woord}{bcolors.ENDC}")

  if (input("Wil je nog een keer spelen (j/n): ") == "j"):
    speel_spelletje()
  else:
    print("Ok. ",end='')

# laat eerst wat info van de lijst zien
verzamel_wat_statistieken()
# loop waarin je woord kan ingeven waar dan wat zaken mee wordt bekeken in de gehele lijst
while vraag_om_woord():
  print("")

wil_je_spelen = input("\nOf wil je nog een spelletje spelen? (j/n): ")
if wil_je_spelen == 'n' or wil_je_spelen == '':
  print("Blijkbaar niet dus. ",end='')
else:
  speel_spelletje()
print("Tot ziens!")