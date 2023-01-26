print("Este programa se encargará de resolver una ecuación del tipo ax + b = 0")
a = int(input("Inserte el valor de a: "))
b = int(input("Inserte el valor de b: "))

solution = None
if a != 0:
    solution = -b/a
    print(f"La solución es: {solution}")
elif a == 0 and b != 0:
    print("Solución imposible.")
elif a == 0 and b == 0:
    print("Solución indeterminada.")
