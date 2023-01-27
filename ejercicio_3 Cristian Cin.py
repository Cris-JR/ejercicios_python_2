P1 = float(input("¿Cuánto ha costado el primer artículo? "))
P2 = float(input("¿Cuánto ha costado el segundo artículo? "))
P3 = float(input("¿Cuánto ha costado el tercer artículo? "))

suma = P1 + P2 + P3

print(suma > 300 or P1 > 200 or P2 > 200 or P3 > 200)

print(P1 > 200 >= P2 and P3 <= 200 or
      P1 <= 200 < P2 and P3 <= 200 or
      P1 <= 200 < P3 and P2 <= 200)

print(P1 % 2 == 0 or P2 % 2 == 0 or P3 % 2 == 0)

print(P1 % 5 == 0 and P2 % 5 == 0 and P3 % 5 != 0 or
      P1 % 5 == 0 and P2 % 5 != 0 and P3 % 5 == 0 or
      P1 % 5 != 0 and P2 % 5 == 0 and P3 % 5 == 0)
