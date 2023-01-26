nota_actitud = float(input("¿Qué nota de actitud ha obtenido? "))
nota_teoria = float(input("¿Qué nota de teoría ha obtenido? "))
nota_practicas = float(input("¿Qué nota ha obtenido en las prácticas? "))

nota_final = None
if nota_teoria < 3.5 or nota_practicas < 3.5:
    nota_final = 2
else:
    nota_final = 0.3 * nota_practicas + 0.6 * nota_teoria + 0.1 * nota_actitud

print(nota_final)
