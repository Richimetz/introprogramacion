import random
def randomvect(lol):
    vect=[]
    for i in range(1,lol+1):
        vect.append(random.randint(1,300))
    return vect

lol=int(input("Ingrese el tamaño del vector: "))
vect2=randomvect(lol)
vect3=[]
print(vect2)
digito=int(input("Ingrese el último dígito a verificar: "))
for pos in range(0,lol):
    valor=vect2[pos]
    residuo=valor%10
    if(residuo==digito):
        vect3.append(valor)
print(vect3)