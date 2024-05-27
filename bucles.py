# for i in [1,2,3]:
#     print("Hola")

# for i in ["Java","Javascript","Python"]:
#     print(i, end=" ")
#     #print(i)


#email=False

#Para recorrer un string
# for i in "nicolas.programador@gmail.com":
#     if(i =="@" or i=="."):
#         email=True

# if email==True:
#     print("Email es correcto")
# else:
#     print("El email no es correcto")

#-------------------------------------
# for i in range(5):#hasra el 4
#     print("Hola")

#-------------------------------------
#              desde hasta de cuanto en cuanto
# for i in range(5,50,2):
#     print(f"valor de la variable {i}")

#Longitud de un string
    #len("Nicolas") #Devuelve la longitud, 7

# valido=False

# email=input("Introduce tu email: ")

# for i in range(len(email)):#El numero del range es el len
#      if email[i]=="@":
#          valido=True

# if valido:
#     print("Email correcto")
# else:
#     print("Email incorrecto")

# i = 1

# while i <= 10:
#     print(f"Ejecucion nro {i}")
#     #i = i + 1
#     i += 1

# edad = int(input("Introduce tu edad por favor: "))

# while edad < 5 or edad > 100: #Mientras la condicion sea verdadera
#     print("Has introducido una edad incorrecta")
#     edad = int(input("Introduce tu edad por favor: "))#Lo pide por no poder salir del bucle

# print("Gracias por colaborar. Puedes pasar")
# print(f"Edad del aspirante: {str(edad)}")

import math

print("Programa de cálculo de raiz cuadrada")
numero = int(input("Introduce un número por favor: "))

intentos = 0

while numero < 0:
    print("No se puede hallar la raíz de un número negativo")

    if intentos == 2:
        print("Has consumido demasiados intentos, el programa ha finalizado")
        break;
    
    print("Programa de cálculo de raiz cuadrada")
    numero = int(input("Introduce un número por favor: "))
    if numero < 0:
        intentos = intentos + 1

if intentos<2:    
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))

