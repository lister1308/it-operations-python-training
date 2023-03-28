dieren = {"kat","hond","slang","varken","koe","paard"}
while True:
    dier = input("Voer een dier in, of geen <enter> om af te sluiten: ")
    if len(dier) == 0:
        print("Ok, tot ziens")
        break
    if dier in dieren:
        print(f"Uw invoer is {len(dier)} lang.")
    else:
        print(f"Volgens mij is {dier} bij mij niet bekend als dier!")