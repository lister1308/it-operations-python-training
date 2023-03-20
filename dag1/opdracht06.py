assert True
# assert False
#assert False, "Er is iets fout gegaan"
#assert 3 * 4 == 13, " Fout berekening"
#print ("iets")

def product(factor1, factor2):
  resultaat = factor1 * factor2
  return resultaat

print("Unittest van 'product'")
assert product(9, 3) == 27, "Berekening van 'product' bevat een fout"
assert product(0, 0) == 0, "Fout bij berekenen 0 waarde"
assert product(1000, 1000) == 100000, "Fout bij berekenen grote waarde"
print("Alles is goed gegaan")
