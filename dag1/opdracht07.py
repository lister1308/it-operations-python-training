voorbeeld_string = "Mijn huisdier"
voorbeeld_string += " is een "

factor = 5

huisdier = "sidder" + "a" * factor + "l"
voorbeeld_string += huisdier
print (voorbeeld_string)

UPPER=0
for letter in voorbeeld_string:
    #print(letter.upper(), end="")
    if ( UPPER == 0):
        print(letter.upper(), end="")
        UPPER = 1
    else:
        print(letter, end="")
        UPPER = 0

print("")

alfabet = 'abcdefghijklmnopqrstuvwxyz'
hij_komt_voor = 'hij' in alfabet
print ("Komt de reeks 'hij' voor in het alfabet?",hij_komt_voor)

for letter in alfabet:
    print(letter, end=".")
print("")

dier = 'huismus'
print ("de lengte van de",dier,"is",len(dier))
print ("de lengte van de",dier,"is",len('huismus'))

print(f"dit is een {dier}")