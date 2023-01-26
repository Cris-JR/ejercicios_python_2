import datetime

dNac = int(input("¿En qué día naciste? "))
mNac = int(input("¿En qué mes naciste? "))
aNac = int(input("¿En qué año naciste? "))

dAct = datetime.date.today().day
mAct = datetime.date.today().month
aAct = datetime.date.today().year

expected_age = aAct - aNac
real_age = None

if mAct >= mNac and dAct >= dNac:
    real_age = expected_age
else:
    real_age = expected_age - 1

if dAct == dNac and mAct == mNac:
    print("¡Feliz Cumpleaños! :D")
    print(f"Tienes {real_age} años.")
elif expected_age == real_age:
    print("¡Ya has cumplido años este año! ¡Feliz cumpleaños atrasado!")
    print(f"Tienes {real_age} años.")
elif expected_age != real_age:
    print("Aún no has cumplido años este año.")
    print(f"Tienes {real_age} años.")
