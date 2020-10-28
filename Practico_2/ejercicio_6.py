def palindromo(palabra):
    long = len(palabra)
    long = long - 1
    inv = ""
    for indice in range(long, -1, -1):
        inv = inv + palabra[indice]
    if inv == palabra:
        print(palabra, "= true")
    else:
        print(palabra, "= false")
palabra = input("Escriba una frase ")
palindromo(palabra)