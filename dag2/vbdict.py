configuratie = {
    "processor":"Intel i7 Keylane",
    "memory":"16GB Kingstond DDR5",
    "ssd":"512 GB"
}

print(configuratie["processor"])

configuratie.update({"processor":"Intel Core i7-8565U"})
print(configuratie.get("processor"))

print(configuratie)
print(configuratie.keys())
print(configuratie.values()) 
print(configuratie.items())

print("In een computer zit het volgende:")
for key,value in configuratie.items():
    print(f"Een {key} van het type {value}")
