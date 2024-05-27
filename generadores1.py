

def generaPares(limite):

    num=1

    #miLista = []

    while num <limite:
        #miLista.append(num*2)
        yield num*2
        num+=1

devuelvePares = generaPares(10)

print(next(devuelvePares))


print("Aqui podría ir más código")

print(next(devuelvePares))

# for i in devuelvePares:

#     print(i)