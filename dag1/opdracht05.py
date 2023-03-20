def herkomst(provincie = "Drenthe"):
    print("Ik kom uit", provincie)

def keer(a,b):
    c = a * b
    return c

def wissel(x,y):
    return y,x

herkomst() # Drukt de default provincie af
herkomst("Friesland")
herkomst("Groningen")
herkomst("Limburg")

r = keer(3,6)
print("3 x 6 =",r)

x = 5
y = 6

print ("x="+str(x),"en y="+str(y))
print ("wisselen")

x,y = wissel(x,y)
print ("na wissel")
print ("x="+str(x),"en y="+str(y))