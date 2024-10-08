from random import sample

numeros = "0123456789"
letras = "abcdefghijklmnñopqrstuvwxyz"
letras_mayusculas = letras.upper()
simbolos = "&/$=%·()"

def generador_contraseñas(longitud):
    secuencia = letras + numeros + simbolos + letras_mayusculas + numeros + simbolos
    contrasña_largo = sample(secuencia, longitud)
    resultado_contraseña = "".join(contrasña_largo)

    return resultado_contraseña

contraseña = generador_contraseñas(12)

print("La contraseña es: " + contraseña)