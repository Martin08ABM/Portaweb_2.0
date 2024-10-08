import time

print("CALCULADORA DE IMC (Índice de Masa Corporal)")
time.sleep(1)

entrada_kg = float(input("Introduce tu peso en kg: "))
entrada_m = float(input("Introduce tu altura en metros: "))

# Calcular el IMC correctamente
al_cuadrado = entrada_m ** 2
imc = entrada_kg / al_cuadrado

print("Tu IMC es " + str(imc))

if imc < float(18.5):
    print("Estás en bajo peso")
elif imc in range(18.5, 24.9):
    print("Estás en un peso normal")
else:
    print("Estás en sobrepeso")