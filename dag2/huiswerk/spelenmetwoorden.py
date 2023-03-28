from prettytable import PrettyTable
# Spelen met woorden
# Wat Python code om alvast aan de slag te kunnen
# Het bestand 'woorden.txt.zip' staat op deze pagina

bestand = "woorden.txt"
bestand_met_woorden = open(bestand, "r") # alleen-lezen van tekst
# lijst_met_woorden = bestand_met_woorden.readlines()
lijst_met_woorden = bestand_met_woorden.read().splitlines()
bestand_met_woorden.close()

aantal_woorden = 0
langestewoord = ''
langstelengte = 0
lijst_met_palindromen = []
alle_woorden = set()
alle_omgekeerde_woorden = set()

def verzamel_wat_statistieken():
  global langestewoord, langstelengte, aantal_woorden, alle_woorden
  for woord in lijst_met_woorden:
    # debug print woord
    #print(woord)
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
      #print(f"Palindroom gevonden: {woord}")
      lijst_met_palindromen.append(woord) 

    # tellen woorden, maar je kan ook lengte lijst bepalen om zelfde resultaat te krijgen
    aantal_woorden = aantal_woorden + 1

  print(f"Aantal woorden in bestand {bestand} is {aantal_woorden}")
  # langste woord
  print(f"Langste woord is {langstewoord} met lengte {str(langstelengte)}")
  # palindromen gevonden
  print(f"Aantal gevonden palindroom woorden is {len(lijst_met_palindromen)}")
  # vergelijk de 2 sets wat ze gemeenschappelijk hebben
  print(f"Alle woorden die omgekeerd ook bestaan zijn er {len(alle_omgekeerde_woorden.intersection(alle_woorden))}")

def vraag_om_woord():
  mijnwoord = input("Vul een woord in: ")
  if (mijnwoord in alle_woorden):
    print(f"Woord {mijnwoord} is aanwezig in de lijst")
  else:
    print(f"Kan woord {mijnwoord} niet vinden in de lijst!")


verzamel_wat_statistieken()
vraag_om_woord()