"""
Eres uno de los líderes de gimnasio (Gym Leader) de una importante organización Pokémon internacional. Uno de los altos miembros del Alto Mando te informa que el Campeón de la Liga Pokémon ha viajado desde EEUU a Barcelona y ha convocado un torneo de alto nivel para esta tarde a las 19:30 en Barcelona. Han consultado la lista de vuelos desde Madrid (donde estás tú) y han llegado a la conclusión de que tienes que tomar un vuelo que parte de Madrid dentro de 2 horas y cierra su facturación 20 minutos antes.
¿Qué duración mínima tiene la misión? ¿Llega el líder a facturar a tiempo dentro de los 100 minutos disponibles? Si no es así, revisa las dependencias, seguro que estás indicando relaciones basadas en las restricciones de los recursos.
Coloca primero la ruta crítica y sus recursos necesarios. A continuación, coloca y reajusta el resto de las actividades dentro de su holgura y define quién hará qué actividad.

Ahora que tienes una lista de tareas y sus respectivas duraciones, necesitas decidir el camino más corto para completarlas todas. Considera cada tarea como un nodo y la duración como el peso de la arista que conecta las tareas. Algunas tareas deben completarse antes que otras, lo que implica que los nodos no están todos conectados entre sí.
Determinar la secuencia óptima de tareas. Recuerda que estos algoritmos son útiles para encontrar el árbol de expansión mínima en un grafo, lo que en este caso representaría la secuencia de tareas con el tiempo total mínimo.
¿Cuál algoritmo elegirías en este caso y por qué? Desarrolla y describe el proceso que utilizarías para aplicar este algoritmo al conjunto de tareas.
"""

class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.dependencies = []

    def add_dependency(self, task):
        self.dependencies.append(task)


# Crear instancias de las tareas
A = Task('A', 20)
B = Task('B', 5)
C = Task('C', 40)
D = Task('D', 10)
E = Task('E', 5)
F = Task('F', 10)
G = Task('G', 20)
H = Task('H', 25)
I = Task('I', 35)
J = Task('J', 25)
K = Task('K', 15)
L = Task('L', 5)
M = Task('M', 25)

# Definir las dependencias entre las tareas
A.add_dependency(D)
A.add_dependency(E)

B.add_dependency(C)
B.add_dependency(H)

C.add_dependency(G)

D.add_dependency(F)

E.add_dependency(F)
E.add_dependency(I)

G.add_dependency(H)

I.add_dependency(J)

J.add_dependency(K)

K.add_dependency(L)

L.add_dependency(M)

# Función para calcular la duración mínima de la misión
def calcular_duracion_minima():
    # Inicializar duraciones mínimas
    duraciones_minimas = {task: 0 for task in [A, B, C, D, E, F, G, H, I, J, K, L, M]}

    # Recorrer las tareas en orden topológico
    for task in [A, B, C, D, E, F, G, H, I, J, K, L, M]:
        for dependency in task.dependencies:
            duraciones_minimas[task] = max(duraciones_minimas[task], duraciones_minimas[dependency] + dependency.duration)

    # Calcular duración mínima total
    duracion_minima_total = max(duraciones_minimas.values())

    return duracion_minima_total

# Calcular duración mínima de la misión
duracion_minima = calcular_duracion_minima()

print("Duración mínima de la misión:", duracion_minima)

# Verificar si el líder llega a facturar a tiempo dentro de los 100 minutos disponibles
llega_a_facturar = duracion_minima <= 100

if llega_a_facturar:
    print("El líder llega a facturar a tiempo.")
else:
    print("El líder no llega a facturar a tiempo.")



# Función para encontrar la secuencia óptima de tareas utilizando el algoritmo de Dijkstra
def encontrar_secuencia_optima(tareas):
    # Crear una lista de nodos no visitados y establecer la distancia inicial de todos los nodos excepto el nodo fuente en infinito
    nodos_no_visitados = tareas.copy()
    distancias = {tarea: float('inf') for tarea in tareas}
    distancias[tareas[0]] = 0

    while nodos_no_visitados:
        # Seleccionar el nodo con la distancia más corta entre los nodos no visitados
        nodo_actual = min(nodos_no_visitados, key=lambda x: distancias[x])

        # Marcar el nodo actual como visitado
        nodos_no_visitados.remove(nodo_actual)

        # Actualizar las distancias de los nodos adyacentes
        for tarea_siguiente in nodo_actual.dependencies:
            nueva_distancia = distancias[nodo_actual] + tarea_siguiente.duration
            if nueva_distancia < distancias[tarea_siguiente]:
                distancias[tarea_siguiente] = nueva_distancia

    # Reconstruir la secuencia óptima de tareas
    secuencia_optima = sorted(distancias, key=lambda x: distancias[x])

    return secuencia_optima

# Obtener la secuencia óptima de tareas
secuencia_optima = encontrar_secuencia_optima([A, B, C, D, E, F, G, H, I, J, K, L, M])

# Imprimir la secuencia óptima de tareas
for tarea in secuencia_optima:
    print(tarea.name)