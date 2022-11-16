#Datos de entrada --> Hito individual, hito grupal y nota examen --> notas 
#Datos de entrada --> Indentificadores: Hito individual (i), hito grupal (g) y nota examen (e)
#Datos de salida --> Nota del trimestre --> (i*30) / 100 || (g*20) / 100 || (e*50) / 100

i = int(input("Dime la nota del hito individual: "))
g = int(input("Dime la nota del hito grupal: "))
e = int(input("Dime la nota del examen: "))

notas = ((i*30) / 100) + ((g*20) / 100) + ((e*50) / 100) 

print(f"La nota final es {notas}")

# ------------------------------------------------------------
