nota_obtenida = int(input("¿Qué nota has obtenido en el examen? "))

if not nota_obtenida in range(0, 11):
    print("¡La nota obtenida debe ser un número entero que se encuentre entre 1 y 10!")
elif nota_obtenida >= 5:
    print("¡Enhorabuena, has aprobado!")
else:
    print("Lo siento, has suspendido. :(")
