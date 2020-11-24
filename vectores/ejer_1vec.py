n = int(input("número que quieres sacar el factorial: "))
FACT = []
for i in range (1,20+1):
    sust = str(i) + "!"
    FACT.append(sust)
print(FACT)

lol = 1
while n > 1:
    lol = n * lol
    n = n-1
    print("el factrial de", n, "es", lol)