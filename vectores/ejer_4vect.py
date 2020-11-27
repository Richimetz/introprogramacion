num = int(input("Ingrese un número: "))
ns = str(num)
arm =""

xd = len(ns)-1
lol = -1
for pos in range(xd,lol,-1):
    arm=arm+ns[pos]

print (arm)

if (arm == ns):
    print("El número es capicua")
else:
    print("El número no es capicua")

