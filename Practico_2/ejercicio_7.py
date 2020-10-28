def generar_n_caracteres(nc, caracter):
    C = (caracter*nc)
    print(C)

caracter = input("caracter: ")
n = int(input("número de repeticiones: "))
generar_n_caracteres(n, caracter)