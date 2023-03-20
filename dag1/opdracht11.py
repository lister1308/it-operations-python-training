"""
set_a = {1,4,2,8,5,9}
set_b = {8}

in_set_a = set_b in set_a
print(in_set_a)

for cijfer in set_a:
  print(cijfer, end=" ")
print("")
"""
jongensnamen = set (("koos","jaap","francis","sam","robin","pieter"))
meisjesnamen = {"saartje","nora","amber","sam","petra","robin"}

#
print("print alle namen")
print(jongensnamen.union(meisjesnamen))
print("")
#
print("verschil jongens en meisjesnamen")
print(jongensnamen.difference(meisjesnamen))
print("")
#
print("verschil tussen meisjesnamen en jongens")
print(meisjesnamen.difference(jongensnamen))
print("")
# 
print("welke namen zitten in beide")
print(meisjesnamen.intersection(jongensnamen))
print("")
# 
print("Toevoegen jongensnaam")
jongensnamen.add('anne')
print(jongensnamen)
print("")
#
print("Wissen meisjesname")
meisjesnamen.clear()
print("Meisjesnamen",meisjesnamen)