from time import localtime
t = localtime()
año_in = t.tm_year
mes_in = t.tm_mon
día_in = t.tm_mday
año = int(input("Año:"))
mes = int(input("Mes: "))
día = int(input("Día: "))
edad1 = año_in - año
edad2 = mes_in - mes
edad3 = día_in - día
if edad2 < 0:
    print("tienes", (edad2 - 1), "años")
else:
    print("tienes", (edad1), "años")