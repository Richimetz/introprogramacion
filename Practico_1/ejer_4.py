numero = int(input("escribe la cantidad de veces deseada:"))
for i in range(0, abs(numero)+1):
    if numero > 0:
        print(2**i)
    else:
        print(2**-i)
