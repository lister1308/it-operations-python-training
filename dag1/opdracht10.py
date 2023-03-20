auto = ("Tesla", "80D", "rood", "2017", "8-LKP-89")

for kenmerk in auto:
    print(kenmerk)
print("-"*100)
mijn_films = []
mijn_films.append(("And Now for Something Completely Different","UK",1971))
mijn_films.append(("Monty Python and the Holy Grail","UK",1975))
mijn_films.append(("Monty Python's Life of Brian","UK",1979))
mijn_films.append(("Monty Python Live at the Hollywood Bowl","USA",1982))
mijn_films.append(("Monty Python's The Meaning of Life","UK",1983))
mijn_films.append(("Monty Python Live (Mostly)","UK",2014))

print(len(mijn_films))
mijn_films.sort()

for een_film in mijn_films:
  if een_film[1] == "UK":
    print(een_film[0])