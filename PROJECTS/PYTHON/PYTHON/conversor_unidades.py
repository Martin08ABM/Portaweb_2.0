print("DEBE INTRODUCIR EL NÚMERO DE LO QUE QUIERA CONVERTIR")
print("Todos las unidades se convierten a unidades del SI")
seleccionar_unidad = int(input("Que unidad quieres convertir? \n 1.Temperatura \n 2.Longitud \n 3.Tiempo \n 4.Velocidad \n 5.Masa \n 6.Volumen \n 7.Presión \n 8.Área \n Elija una opción  (1, 2, 3, 4, 5, 6, 7, 8): "))

if seleccionar_unidad == 1:
    temperatura = int(input("Que quiere convertir? \n 1.Grados centígrados a grados kelvin \n 2.Grados farenheit a grados kelvin \n Elija una opción (1, 2): "))
    if temperatura == 1:
        grados_centigrados = float(input("Temperatura en ªC: "))
        grados_kelvin = 273.15
        resultado = str(grados_centigrados + grados_kelvin)
        print("El resultado es " + resultado)
    elif temperatura == 2:
        grados_farenheit = float(input("Temperatura en ªF: "))
        grados_kelvin2 = 273.15
        grados_kelvin_resultado = (((grados_farenheit) - 32) * 5/9 + grados_kelvin2)
        print("El resultado es " + grados_kelvin_resultado)
    else:
        print("Selección para convertir la temperatura no válida")

if seleccionar_unidad == 2:
    longitud = int(input("Que quiere convertir? \n 1.Milla a metro \n 2.Pulgada a metro \n 3.Yarda a metro \n 4.Pie a metro \n 5.Milla nautica a metro \n 6.Kilometro a metro \n Elija una opción (1, 2, 3, 4, 5): "))
    if longitud == 1:
        milla = float(input("Longitud en millas: "))
        longitud_millas = 1609.34
        resultado = str(longitud_millas * milla)
        print("El resultado es " + resultado)
    elif longitud == 2:
        pulgada = float(input("Longitud en pulgadas: "))
        longitud_pulgadas = 39.37
        resultado = str(pulgada / longitud_pulgadas)
        print("El resultado es " + resultado)
    elif longitud == 3:
        yarda = float(input("Longitud en yardas: "))
        longitud_yardas = 1.094
        resultado = str(yarda / longitud_yardas)
        print("El resultado es " + resultado)
    elif longitud == 4:
        pie = float(input("Longitud en pies: "))
        longitud_pies = 3.281
        resultado = str(pie / longitud_pies)
        print("EL resultado es " + resultado)
    elif longitud == 5:
        milla_nautica = float(input("Longitud en millas náuticas: "))
        longitud_milla_nautica = 1852
        resultado = str(milla_nautica * longitud_milla_nautica)
        print("El resultado es " + resultado)
    elif longitud == 6:
        kilometro = float(input("Longitud en kilometros: "))
        longitud_km = 1000
        resultado = str(kilometro * longitud_km)
        print("El resultado es " + resultado)
    else:
        print("Selección para convertir no válida")

if seleccionar_unidad == 3:
    tiempo = int(input("Que quiere convertir? \n 1.Minuto a segundo \n 2.Hora a segundos \n 3.Día a segundo \n Elija una opción (1, 2, 3): "))
    if tiempo == 1:
        minuto = float(input("Tiempo en minutos: "))
        tiempo_minuto = 60
        resultado = str(minuto * tiempo_minuto)
        print("El resultado es " + resultado)
    elif tiempo == 2:
        hora = float(input("Tiempo en horas: "))
        tiempo_horas = 3600
        resultado = str(hora * tiempo_horas)
        print("El resultado es " + resultado)
    elif tiempo == 3:
        dia = float(input("Tiempo en días: "))
        tiempo_dias = 86400
        resultado = str(dia * tiempo_dias)
        print("El resultado es " + resultado)
    else:
        print("Selección para convertir no válida")

if seleccionar_unidad == 4:
    velocidad = int(input("Que quiere convertir? \n 1.Km/h a m/s \n 2.Nudo a m/s \n 3.Millas/h a m/s \n Elija una opción (1, 2, 3): "))
    if velocidad == 1:
        kilometro_hora = float(input("Velocidad en km/h: "))
        velocidad_kmh = 3.6
        resultado = str(kilometro_hora / velocidad_kmh)
        print("El resultado es " + resultado)
    elif velocidad == 2:
        nudo = float(input("Velocidad en nudos: "))
        velocidad_nudo = 1.944
        resultado = str(nudo / velocidad_nudo)
        print("El resultado es " + resultado)
    elif velocidad == 3:
        milla_hora = float(input("Velocidad en mi/h: "))
        velocidad_mph = 2.237
        resultado = str(milla_hora / velocidad_mph)
        print("El resultado es " + resultado)
    else:
        print("Selección para convertir no válida")

if seleccionar_unidad == 5:
    masa = int(input("Que quiere convertir? \n 1.Gramo a kg \n 2.Libra a kg \n 3.Onza a kg \n 4.Tonelada a kg \n Elija una opción (1, 2, 3, 4): "))
    if masa == 1:
        gramo = float(input("Peso en gramos: "))
        masa_gramo = 1000
        resultado = str(gramo / masa_gramo)
        print("El resultado es " + resultado)
    elif masa == 2:
        libra = float(input("Peso en libras: "))
        masa_libra = 2.205
        resultado = str(libra / masa_libra)
        print("El resultado es " + resultado)
    elif masa == 3:
        onza = float(input("Peso en onzas: "))
        masa_onza = 35.274
        resultado = str(onza / masa_onza)
        print("El resultado es " + resultado)
    elif masa == 4:
        tonelada = float(input("Peso en toneladas: "))
        masa_tonelada = 1000
        resultado = str(tonelada * masa_tonelada)
        print("El resultado es " + resultado)
    else:
        print("Selección para convertir no válida")

if seleccionar_unidad == 6:
    volumen = int(input("Que quiere convertir? \n 1.Litro a metro cúbico \n 2.Mililitro a metro cúbico \n Elija una opción (1, 2): "))
    if volumen == 1:
        litro = float(input("Volumen en litros: "))
        volumen_litro = 1000
        resultado = str(litro / volumen_litro)
        print("El resultado es " + resultado)
    elif volumen == 2:
        mililitro = float(input("Volumen en mililitros: "))
        volumen_mililitro = 0.000001
        resultado = str(mililitro / volumen_mililitro)
        print("El resultado es " + resultado)
    else:
        print("Selección para convertir no válida")

if seleccionar_unidad == 7:
    presion = float(input("Que quiere covertir? \n 1.Atmósfera a pascal \n 2.Bar a pascal \n 3.Milimetro de mercurio a pascal \n Elija una opción (1, 2, 3): "))
    if presion == 1:
        atmosfera = float(input("Presión en atmosferas: "))
        presion_atmosfera = 101325
        resultado = str(atmosfera * presion_atmosfera)
        print("El resultado es " + resultado)
    elif presion == 2:
        bar = float(input("PResión en bares: "))
        presion_bar = 10000
        resultado = str(bar * presion_bar)
        print("El resultado es " + resultado)
    elif presion == 3:
        milimetro_mercurio = float(input("Presión en milimetros de mercurio: "))
        presion_mmhg = 133.322
        resultado = str(milimetro_mercurio * presion_mmhg)
        print("El resultado es " + resultado)

if seleccionar_unidad == 8:
    area = float(input("Que quiere convertir \n 1.Kilometro cuadrado a metro cuadrado \n 2.Hectárea a metro cuadrado \n Elija una opción (1, 2): "))
    if area == 1:
        km2 = float(input("Área en kilometros cuadrados: "))
        area_km2 = 1000000
        resultado = str(km2 * area_km2)
        print("El resultado es " + resultado)
    elif area == 2:
        hectarea = float(input("Área en hectáreas: "))
        area_hectarea = 10000
        resultado = str(hectarea * area_hectarea)
        print("El resultado es " + resultado)