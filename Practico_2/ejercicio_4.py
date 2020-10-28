def vocal(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print(letra, "= true")
    else:
        print(letra, "= false")

letra = input("letra: ")
vocal(letra)