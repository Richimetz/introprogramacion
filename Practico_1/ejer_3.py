dividendo = int(input("escriba un dividendo:"))
divisor = int(input("ingrese un divisor: "))
cociente = dividendo // divisor
resto = dividendo % divisor
if dividendo % divisor ==0:
    print("la división es exacta ")
else:
    print("la división no es excta ")
    print("cociente: ", cociente)
    print("resto: ", resto)