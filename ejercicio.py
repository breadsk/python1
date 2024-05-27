def funcion_recorrer_lista(lista):
    total = 0
    cadenas = []

    for arreglo in arreglos:
        if arreglo.isdigit():
            total += int(arreglo)
        else:
            cadenas.append(arreglo)

    print("La suma total de los números es:", total)
    print("Los elementos que son strings son:")
    for cadena in cadenas:
        print(cadena)


arreglos = ['2', 'CASA', 'PRUEBA', '9', '-1']

funcion_recorrer_lista(arreglos)