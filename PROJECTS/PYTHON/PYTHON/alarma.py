import datetime
import time

hora_alarma = input("A que hora quiere que suene la alarma? ")
hora_actual = datetime.datetime.now().strftime('%H:%H')

def verificar_hora (hora_actual, hora_alarma):
    if hora_actual == hora_alarma:
        print('Ya es la hora')

while hora_alarma != hora_actual:
    print("Todavía no es la hora de la alarma")

    if hora_alarma == hora_actual:
        print("Ya es la hora!!!!")