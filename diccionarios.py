# midiccionario = {
#     "Alemania":"Berlin",
#     "Francia":"Paris",
#     "Reino Unido":"Londre",
#     "España":"Madrid"
# }

# #Accediento a la clave obtenemos el valor
# print(midiccionario["Francia"])
# print(midiccionario)

# midiccionario["Italia"] = "Lisboa"
# print(midiccionario)

# midiccionario["Italia"]="Roma"
# print(midiccionario)

# del midiccionario["España"]
# print(midiccionario)

# midiccionario = {"Alemania":"Berlin",23:"jordan","mosqueteros":3}
# print(midiccionario)

# milista = ["españa","francia","inglaterra","alemania"]
# midiccionario = {milista[0]:"Madrid",milista[1]:"paris",milista[2]:"londres",milista[3]:"berlin"}
# print(midiccionario["francia"])

#midiccionario = {23:"jordan","nombre":"michael","equipo":"chicago","anillos":[1991,1992,1993,1996,1997,1998]}
#print(midiccionario["equipo"])
#print(midiccionario["anillos"])
midiccionario = {23:"jordan","nombre":"michael","equipo":"chicago","anillos":{"temporadas": [1991,1992,1993,1996,1997,1998]}}

#print(midiccionario.keys())
#print(midiccionario.values())
print(len(midiccionario))
#print(type(midiccionario))
#print(midiccionario["anillos"])


#keys nos devuelve las claves de un diccionario
#values nos devuelve los valores de un diccionario
#length nos devuelve el largo de un diccionario