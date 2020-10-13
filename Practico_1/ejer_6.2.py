n1 = int(input("ingrese un número: "))
n2 = int(input("ingrese otro número: "))
n3 = int(input("ingrese otro número: "))
min = min(n1, n2, n3)
max = max(n1, n2, n3,)
mid = (n1 + n2 + n3) - min -max
print(min," ", mid, " ", max)
if min == max and max == mid:
    print("los números dados son iguales ")
