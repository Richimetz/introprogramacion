edad = int(input("edad: "))
estatura= float(input("estatura(m): "))
peso = float(input("peso(kg): "))
indice = peso/(estatura**2)
if indice < 22.00:
    if edad < 45:
        print("factor de riesgo bajo")
    else:
        print("factor de riesgo medio")
if indice >= 22.00:
    if edad < 45:
        print("factor de riesgo medio")
    else:
        print("factor de riesgo alto")