# Este ejercicio ha sido realizado mediante el uso de "diccionarios".
# Estos diccionarios han sido empleados para guardar la altura y talla de cada persona,
# para después realizar las operaciones necesarias.
# A pesar de ser algo extenso, resulta bastante sencillo de entender al asociar
# ciertas características a cada persona antes de compararlas.

persona_1 = {
    "altura": int(input("¿Cuál es la altura (cm) de la 1ᵃ persona? ")),
    "talla": int(input("¿Qué talla de zapatos usa la 1ᵃ persona? "))
}

persona_2 = {
    "altura": int(input("¿Cuál es la altura (cm) de la 2ᵃ persona? ")),
    "talla": int(input("¿Qué talla de zapatos usa la 2ᵃ persona? "))
}

persona_3 = {
    "altura": int(input("¿Cuál es la altura (cm) de la 3ᵃ persona? ")),
    "talla": int(input("¿Qué talla de zapatos usa la 3ᵃ persona? "))
}

print((persona_1["altura"] and persona_2["altura"] and persona_3["altura"]) > 165)

print((persona_1["talla"] and persona_2["talla"] and persona_3["talla"]) <= 44)

rango_tallas = range(40, 45)
print(persona_1["talla"] and persona_2["talla"] and persona_3["talla"] in rango_tallas)

print((persona_1["altura"] > 180 and persona_1["talla"] < 40) or
      (persona_2["altura"] > 180 and persona_2["talla"] < 40) or
      (persona_3["altura"] > 180 and persona_3["talla"] < 40))

