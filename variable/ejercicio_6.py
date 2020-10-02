peso_kg = float(input("ingrese su peso en Kg: "))
altura_m = float(input("ingrese su estatura en metros: "))
IMC = peso_kg / altura_m**2
(mensaje) = f"Tu índie de masa corporal es: {IMC} kgm2"
print(mensaje)
