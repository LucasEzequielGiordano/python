# IMC
# peso = int(input("¿cuál es tu peso? "))
# estatura = float(input("¿cuál es tu altura?"))
# imc = peso / (estatura  ** 2)
# print("Tu índice de masa corporal es: ", imc) 

# Orden al reves
# lista = []
# for numero in range(1, 101):
#     lista.append(numero)
#     ordenInverso = sorted(lista, reverse=True)
# print(ordenInverso)

# Funcion años bisiestos
def bisiesto():
    year = int(input('Ingresa un año para saber si es bisiesto: '))

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return f'{year} es un año bisiesto'
    else:
        return f'{year} no es un año bisiesto'

print(bisiesto())