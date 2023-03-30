
def Print_lijst_item (l):
    if len(l) > 1:
        Print_lijst_item(l[1:])
    print(l[0])

Print_lijst_item([1,2,3,4,5])