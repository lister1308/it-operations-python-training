"""
while True:
  dier = input("Voer een dier in, of geef  om af te sluiten: ")
  if len(dier) == 0:
    print("Ok, tot ziens")
    break
  print("Uw invoer is", len(dier), "lang")
"""
a = input("Geef een waarde (geen 0) ")

try:
  a = int(a)
  b = 100 / a
  print(b)
except:
  print("Ik zei nog zo: geen 0")
finally:
  print("Bedankt voor het meedoen")