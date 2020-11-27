def calFact(numero):
    f = 1
    for i in range (1,numero+1):
        f =f*i
    return f



for n in range (1,21):
    print("El factorial para de ",n ," es:")
    f = calFact(n)
    print(f)