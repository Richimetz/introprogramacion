p1 = str(input("ingrese una palabra:"))
p2 = str(input("ingrese otra palabra: "))
longp1 = len(p1)
longp2 = len(p2)
if longp1 < longp2:
    print(p1, "tiene", "(", longp2 - longp1, ")", "letras menos que ", p2)
elif longp1 > longp2:
    print(p1, "tiene", "(", longp1 - longp2, ")","letras mas que", p2)
else:
    print("las palabras", p1,  "y", p2,  "tienen la misma cantidad de letras")
