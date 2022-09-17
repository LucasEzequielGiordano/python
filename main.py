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
# def bisiesto():
#     year = int(input('Ingresa un año para saber si es bisiesto: '))
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         return f'{year} es un año bisiesto'
#     else:
#         return f'{year} no es un año bisiesto'
# print(bisiesto())


# Crear utilizando la herencia un coche con sus propiedades y las del Vehiculo
class Vehiculo:
    _color = None
    _ruedas = 0
    _puertas = 0
    
    def __init__(self, color, ruedas, puertas):
        self._color = color
        self._ruedas = ruedas
        self._puertas = puertas

class Coche(Vehiculo):
    _velocidad = 0
    _cilindrada = 0

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self._velocidad = velocidad
        self._cilindrada = cilindrada

    def __str__(self):
        return f'Detalles:\n  color: { self._color }, \n  ruedas: { self._ruedas }, \n  puertas: { self._puertas }, \n  velocidad: { self._velocidad }, \n  cilindrada: { self._cilindrada } \n'

obj = Coche('Negro', 4, 4, 500, 4)
print(obj)