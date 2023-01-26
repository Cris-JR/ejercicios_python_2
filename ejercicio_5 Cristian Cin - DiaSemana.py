dias_de_la_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

dia_elegido = int(input("Escriba el número del día de la semana que quiera conocer: "))

index_final = dia_elegido - 1

if dia_elegido not in range(1, 8):
    print("Debe escribir un número que se encuentre entre el 1 y el 7.")
else:
    print(f"El día N.º {dia_elegido} de la semana es: {dias_de_la_semana[index_final]}.")
