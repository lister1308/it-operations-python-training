a = input ("Geef een waarde (geen 0) ")

try:
    a = int(a)
    b = 100 / a
    print(b)
except:
    print("Ik zei nog zo, geef een waarde en geen 0!")
finally:
    print("Bedankt voor het meedoen")