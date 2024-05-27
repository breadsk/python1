

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        #for subElemento in elemento:
        yield from elemento#Hazme un yield desde el primer elemento

ciudades_devueltas = devuelve_ciudades("Santiago","Viña del mar","Villarrica","Castro")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))