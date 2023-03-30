def print_lijst_item(appie):
  if len(appie) > 1:
    print_lijst_item(appie[1:])
  print(appie[0])

print_lijst_item([1,2,3,4,5])