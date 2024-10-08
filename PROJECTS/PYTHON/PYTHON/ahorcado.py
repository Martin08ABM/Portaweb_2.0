import time
import random
from time import sleep
import requests
from bs4 import BeautifulSoup

#Lógica del juego
print("VENGA VAMOS A JUGAR AL AHORCADO")
time.sleep(2)
numero_turnos = input("Cuantos turnos quiere?: ")
if numero_turnos > 30:
    print("No se valen tantos intentos")
else:
    print("Te arriesgas he, asi me gusta")

turnos = print("Has elejido " + numero_turnos + " turnos")

lista_palabras = ("amigo", "familia", "amor", "hermano", "casa", "cada", "caca", "hola", "como", "lomo", "batalla", "arriba", "comer", "respirar")
palabras = random.choice(lista_palabras)
conjeturas = ''

while turnos > 0:
    error = 0
    continue
else:
    print("_")
    error = 1
print("\n")

if turnos == 0:
    print("Has ganado :)")

