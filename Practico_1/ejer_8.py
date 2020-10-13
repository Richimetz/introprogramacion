n1 = int(input("primer número:"))
n2 = int(input("segundo número: "))
suma = 0
for i in range (n1 + 1, n2):
    print(i)
    suma = suma + i
print("la suma es: ", suma)