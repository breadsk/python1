def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicacion(num1,num2):
    return num1*num2

def division(num1,num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        return "Operación errónea"

while True:
    try:
        opt1 = int(input("Introduce el primer número: "))
        opt2 = int(input("Introduce el segundo número: "))
        break;
    except ValueError:
        print("Valores introducidos no son correctos. Inténtalo de nuevo")

operacion = input("Introduce la operacion a realizar (suma,resta,multiplicacion,division): ")

if operacion=="suma":
    print(suma(opt1,opt2))
elif operacion == "resta":
    print(resta(opt1,opt2))
elif operacion == "multiplicacion":
    print(multiplicacion(opt1,opt2))
elif operacion == "division":
    print(division(opt1,opt2))
else:
    print("Operacion no contemplada")

print("Operación ejecutada. Continuación de ejecución del programa")