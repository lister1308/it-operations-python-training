"""
bestandsnaam = 'tekst.txt'
modus = 'x'
f = open(bestandsnaam, modus)
f.write("een nieuwe regel tekst in het bestand")
f.close()
"""

filename = 'test.txt'
linebreak = '\n'

def getItemsFromFile():
    try:
        file = open(filename,"r")
    except:
        return []

    listOfItems = []
    for item in file:
        listOfItems.append(item.strip(linebreak).split(', '))
    file.close()
    return listOfItems

print(getItemsFromFile())
