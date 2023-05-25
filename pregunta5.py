"""
Problema de los movimientos de un Abra en una red de Pokémon

Si se parte de la ruta 1, Abra puede teletransportarse a las rutas 6 y 8 (dos teletransportes); si se sale de la ruta 2, Abra puede llegar a las rutas 7 y 9 (dos teletransportes más); iniciando desde la ruta 3, se puede arribar a las rutas 4 y 8 (se suman nuevamente dos); si se arranca desde la ruta 4, las posibilidades son las rutas 3, 9 y 0 (ahora se acumulan tres teletransportes); pero si la posición inicial es la ruta 5, Abra no puede teletransportarse a ningún lugar dado que no hay teletransportes válidos.

Sin embargo, aún restan varias posibilidades más para seguir probando; desde la ruta 6 se pueden alcanzar las rutas 1, 7 y 0 (nuevamente se agregan tres más); por su parte desde la ruta 7 se puede mover a Abra hasta las rutas 2 y 6 (la cantidad se incrementa en dos); si se toma la ruta 8 como inicio, se pueden alcanzar las rutas 1 y 3 (se adicionan dos teletransportes); si se posiciona a Abra en la ruta 9, las opciones para teletransportarse son las rutas 2 y 4 (nuevamente se tienen dos teletransportes); y por último, si se sale desde la ruta 0, los teletransportes válidos son hacia las rutas 4 y 6 (se suman los últimos dos). En total, se pueden realizar veinte teletransportes válidos con Abra.

Ahora, diseña un algoritmo que permita calcular cuántos posibles teletransportes válidos puede realizar Abra, recibiendo como entrada la cantidad de teletransportes a realizar desde el inicio, partiendo de todas las rutas. Por ejemplo, como mostramos anteriormente, si la cantidad de teletransportes es uno, la cantidad de teletransportes válidos son veinte. Pero si la cantidad de teletransportes son dos y se sale de la ruta 1, se puede ir hasta las rutas 6 y 8 (un teletransporte), a continuación, a partir de la ruta 6 hasta las rutas 1, 7 y 0 (dos teletransportes de Abra), luego se sigue desde la ruta 8 hasta las rutas 1 y 3 (para alcanzar los dos teletransportes de Abra). En resumen, se tienen cinco posibles teletransportes válidos partiendo desde la ruta 1 (1-6-1, 1-6-7, 1-6-0, 1-8-1 y 1-8-3) a estos se deben sumar todos los teletransportes que resulten de partir de las demás rutas. En total, la cantidad de posibles teletransportes válidos para dos teletransportes son 46. Una vez desarrollado el algoritmo, completa la siguiente tabla.
"""

# Definición de la clase Nodo
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = []

    def agregar_vecino(self, nodo):
        self.vecinos.append(nodo)

# Función para calcular la cantidad de posibles teletransportes válidos para una cantidad de movimientos dada
def calcular_posibilidades_teletransporte(movimientos):
    # Crear los nodos correspondientes a las rutas
    rutas = [Nodo(i) for i in range(10)]

    # Establecer las conexiones entre los nodos según las reglas dadas
    rutas[1].agregar_vecino(rutas[6])
    rutas[1].agregar_vecino(rutas[8])
    rutas[2].agregar_vecino(rutas[7])
    rutas[2].agregar_vecino(rutas[9])
    rutas[3].agregar_vecino(rutas[4])
    rutas[3].agregar_vecino(rutas[8])
    rutas[4].agregar_vecino(rutas[3])
    rutas[4].agregar_vecino(rutas[9])
    rutas[4].agregar_vecino(rutas[0])
    rutas[6].agregar_vecino(rutas[1])
    rutas[6].agregar_vecino(rutas[7])
    rutas[6].agregar_vecino(rutas[0])
    rutas[7].agregar_vecino(rutas[2])
    rutas[7].agregar_vecino(rutas[6])
    rutas[8].agregar_vecino(rutas[1])
    rutas[8].agregar_vecino(rutas[3])
    rutas[9].agregar_vecino(rutas[2])
    rutas[9].agregar_vecino(rutas[4])
    rutas[0].agregar_vecino(rutas[4])
    rutas[0].agregar_vecino(rutas[6])

    # Función recursiva para calcular las posibilidades válidas desde un nodo dado
    def calcular_posibilidades_recursivo(nodo, movimientos):
        if movimientos == 0:
            return 1
        
        posibilidades = 0
        for vecino in nodo.vecinos:
            posibilidades += calcular_posibilidades_recursivo(vecino, movimientos - 1)
        
        return posibilidades

    # Calcular las posibilidades válidas para cada ruta
    posibilidades = []
    for ruta in rutas:
        posibilidades.append(calcular_posibilidades_recursivo(ruta, movimientos))

    return posibilidades

# Calcular las posibilidades válidas para diferentes cantidades de movimientos
cantidades_movimientos = [1, 2, 3, 5, 8, 10, 15, 18, 21, 23, 32]
for movimientos in cantidades_movimientos:
    posibilidades = calcular_posibilidades_teletransporte(movimientos)
    print(f"Cantidad de movimientos: {movimientos}")
    print(f"Posibilidades válidas: {posibilidades}")
    print(f"Total de posibilidades: {sum(posibilidades)}")