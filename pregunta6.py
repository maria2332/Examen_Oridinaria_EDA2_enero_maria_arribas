"""
Pasemos a trabajar en otro ejemplo para fortalecer aún más nuestro pensamiento algorítmico, en este caso el problema de las n-PokéBolas. Este problema consiste en ubicar n Pokémon en una red de gimnasios de tamaño n x n, sin que los mismos se enfrenten. Recuerda que un Pokémon puede moverse de manera horizontal, vertical y diagonal, además podemos ver una solución al problema de los 4 Pokémon. Nótese que una parte importante para resolver un problema es de qué manera representar la solución, para este caso particular usamos un vector de n posiciones (gimnasios) y el valor almacenado representa la fila donde se ubica dicho Pokémon.
Cuando hayas entendido el problema y tengas una solución en mente, desarrolla un algoritmo que permita hallar al menos una solución para distintas cantidades de Pokémon, y luego completa la siguiente tabla.
"""

class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def solve_n_pokeballs(n):
    def is_safe(row, col, node):
        # Verificar si es seguro colocar un Pokémon en la posición (row, col)
        while node:
            if node.value == col or (node.value is not None and abs(node.value - col) == abs(row - len(node.children))):
                return False
            node = node.parent
        return True

    def build_solution(node):
        # Construir la solución a partir del nodo final
        solution = []
        while node:
            solution.insert(0, node.value)
            node = node.parent
        return solution

    def backtrack(row, n, node, solutions):
        if row == n:
            # Se llegó a una solución válida
            solutions.append(build_solution(node))
            return

        for col in range(n):
            if is_safe(row, col, node):
                new_node = Node(col, node)
                node.add_child(new_node)
                backtrack(row + 1, n, new_node, solutions)

    solutions = []
    root = Node(None)
    backtrack(0, n, root, solutions)
    return solutions


# Ejemplo de uso
n = 4
all_solutions = solve_n_pokeballs(n)
unique_solution = all_solutions[0] if all_solutions else []
print(f"Número de soluciones distintas para {n}-PokéBolas: {len(all_solutions)}")
print(f"Una solución: {unique_solution}")
