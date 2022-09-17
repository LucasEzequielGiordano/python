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
# class Vehiculo:
#     _color = None
#     _ruedas = 0
#     _puertas = 0
    
#     def __init__(self, color, ruedas, puertas):
#         self._color = color
#         self._ruedas = ruedas
#         self._puertas = puertas

# class Coche(Vehiculo):
#     _velocidad = 0
#     _cilindrada = 0

#     def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
#         super().__init__(color, ruedas, puertas)
#         self._velocidad = velocidad
#         self._cilindrada = cilindrada

#     def __str__(self):
#         return f'Detalles:\n  color: { self._color }, \n  ruedas: { self._ruedas }, \n  puertas: { self._puertas }, \n  velocidad: { self._velocidad }, \n  cilindrada: { self._cilindrada } \n'

# obj = Coche('Negro', 4, 4, 500, 4)
# print(obj)

# Obtener mediante la class Alumno y los atributos nombre y nota, la nota de los alumnos
class Alumno:
    _nombre = None
    _nota = None

    def __init__ (self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    def notaFinal(self):
        if self._nota >= 6:
            return f'{self._nombre} aprobaste, tu nota final es: {self._nota}'
        else:
            return f'{self._nombre} reprobaste, tu nota final es: {self._nota}'

estudiante = Alumno('Lucas', 4)
print(f'Estudiante: {estudiante._nombre}')
print(f'Nota: {estudiante._nota}')
print(estudiante.notaFinal())