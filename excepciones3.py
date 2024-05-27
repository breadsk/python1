import math

def calculaRaiz(num1):

    #if num1<0:
        #raise ValueError("El número no puede ser negativo")
    #else:
    return math.sqrt(num1)
    
op1 = (int(input("Introduce un número:   ")))

try:
    print(calculaRaiz(op1))

except ValueError as ErrorDeNumeroNegativo:

    #print("Error po loco")
    print(ErrorDeNumeroNegativo)

print("Programa terminado")