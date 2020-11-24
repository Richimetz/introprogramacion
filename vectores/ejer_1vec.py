def impAsteriscos(numero):
    print("Para:",numero)
    for i in range(1,numero+1):
        print("*",end="")
    print("")


for n in range(1,21):
    impAsteriscos(n)