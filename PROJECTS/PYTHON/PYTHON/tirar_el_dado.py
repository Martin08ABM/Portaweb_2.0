import random

moneda_dado = input("Que quieres hacer? \n 1. Tirar un dado \n 2.Tirar una moneda \n Elije (1, 2): ")

if moneda_dado == '1':
    caras_dado = random.randint(1, 6)
    print("El número es " + str(caras_dado))
elif moneda_dado == '2':
    caras_moneda = random.choice(["Cara", "Cruz"])
    print("Te ha tocado " + caras_moneda)
else:
    print("La entrada que has hecho, es incorrecta. Introduce 1 o 2 para que funcione.")