#a la hora de generar los numeros no se tienen que repetir horizontalmente, verticalmente, y en el cuadrado
import random

def num_ran():
    numero_aleatorio = random.randint(1, 9)
    return numero_aleatorio


lista1 = list()
lista2 = list()
lista3 = list()
lista4 = list()
lista5 = list()
lista6 = list()
lista8 = list()
lista9 = list()

cubo1 = list()
cubo2 = list()
cubo3 = list()

cubo4 = list()
cubo5 = list()
cubo6 = list()

cubo7 = list()
cubo8 = list()
cubo9 = list()

for x in range(9):
    lista1.append(num_ran())




print(lista1)