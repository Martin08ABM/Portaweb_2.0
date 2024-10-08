import random
import time

print("ADIVINA EL NÚMERO")
time.sleep(0.5)
print("Los números van entre 0 y 10")
time.sleep(0.5)
print("Tienes 10 intentos")
time.sleep(0.5)

numero = random.randint(0, 10)
intentos_restantes = 10

while intentos_restantes > 0:
    entrada_numero = int(input("Dime el número: "))
    
    if entrada_numero > 10:
        print("Que el máximo es 10, atontao :|")
        continue
    elif entrada_numero < 0:
        print("Que el mínimo es 0, como tus notas ;)")
        continue

    if entrada_numero == numero:
        print("¡Has adivinado el número, GENIO!")
        break
    elif entrada_numero < numero:
        print("Te has quedado corto, vuelve a intentarlo.")
    else:
        print("Te has pasado, vuelve a intentarlo.")

    intentos_restantes -= 1
    print(f"Te quedan {intentos_restantes} intentos.")

if intentos_restantes == 0:
    print(f"NO lo has adivinado, el número era: {numero}")
