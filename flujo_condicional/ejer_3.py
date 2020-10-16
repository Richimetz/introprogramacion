partidos= "Partidos disponibles: Comunidad Ciudadana y MAS "
print(partidos)
voto = input("Escriba el partido de preferencia:")
p1 = "Comunidad Ciudadana"
p2 = "MAS"
if voto == p1:
    print("Usted votó por: ", "(", p1,")", )
elif voto == p2:
    print("usted votó por: ", "(", p2 ,")",)
else:
    print("voto inválido")