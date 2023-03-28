# Spelen met woorden
# Wat Python code om alvast aan de slag te kunnen
# Het bestand 'woorden.txt.zip' staat op deze pagina

bestand = "woorden.txt"
bestand_met_woorden = open(bestand, "rt") # alleen-lezen van tekst
# lijst_met_woorden = bestand_met_woorden.readlines()
lijst_met_woorden = bestand_met_woorden.read().splitlines()
bestand_met_woorden.close()

aantal_woorden = 0
langestewoord = ''
langstelengte = 0

for woord in lijst_met_woorden:
  # debug print woord
  #print(woord)
  # tellen langste woord
  lengte = len(woord)
  if lengte > langstelengte:
    langstelengte = lengte
    langstewoord = woord
  
  # bepalen palindroom
  for 

  # tellen woorden, maar je kan ook lengte lijst bepalen om zelfde resultaat te krijgen
  aantal_woorden = aantal_woorden + 1

print(len(lijst_met_woorden))
print(f"Aantal woorden in bestand {bestand} is {aantal_woorden}")
print(f"Langeste woorde is {langstewoord} met lenge {str(langstelengte)}")