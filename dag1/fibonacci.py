'''
Opdracht van Tom, Frank, Wouter
Gemaakt op 20-03-2023
'''

def fibonaccilijst(aantal_getallen):
    if aantal_getallen < 0:
        print("FOUT: Getal mag niet negatief zijn!") 
        exit()

    fibonaccireeks = [0.5, 1, 2]
    if (aantal_getallen <4):
        fibonaccireeks = fibonaccireeks[0:(aantal_getallen)]
    else:
        aantal_getallen -= 3   
        while aantal_getallen > 0:
            aantal_getallen -= 1
            fibonaccireeks.append(fibonaccireeks[-2]+fibonaccireeks[-1])
    return(fibonaccireeks)

assert len(fibonaccilijst(50)) == 50, 'Fout: aantal retour waarden klopt niet'
assert fibonaccilijst(0) == [], 'Fout: teruggegeven waarden kloppen niet'
assert fibonaccilijst(1) == [0.5], 'Fout: teruggegeven waarden kloppen niet'
assert fibonaccilijst(2) == [0.5, 1], 'Fout: teruggegeven waarden kloppen niet'
assert fibonaccilijst(3) == [0.5, 1, 2], 'Fout: teruggegeven waarden kloppen niet'
assert fibonaccilijst(4) == [0.5, 1, 2, 3], 'Fout: teruggegeven waarden kloppen niet'
assert fibonaccilijst(5) == [0.5, 1, 2, 3, 5], 'Fout: teruggegeven waarden kloppen niet'
print(fibonaccilijst(-1))
