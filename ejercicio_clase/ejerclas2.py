rango1 = int(input("rango 1: "))
rango2 = int(input("rango 2: "))
vect = []
vect2 = []
vect3 = []
for i in range (rango1,rango2+1):
    vect.append(i)
    vect.reverse
print(vect)
vect2 = [i for i in range(rango1,rango2+1) if i%2==0]
vect2.reverse
print(vect2)
print(sum(vect2))
vect3 = [i for i in range(rango1,rango2+1) if i%2 !=0 ]
vect3.reverse
print(vect3)
print(sum(vect3))