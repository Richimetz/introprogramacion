consumo = float(input("ingrese el consumo: "))
if consumo <= 100:
    print("deberá pagar 1.00 bs/m3")
elif consumo > 100 or consumo <= 499:
    print("deberá pagar 1,20 bs/m3")
elif consumo >= 500 or consumo <= 999:
    print(" deberá pagar 1,50 bs/m3 ")
elif consumo >= 1000:
    print("deberá pagar 2,00, bs/m3 ")
