n1 = int(input("ingresa un número: "))
divisor = 0
for divisor in range(1, n1 +1):
    if n1 % divisor == 0:
        print(divisor)