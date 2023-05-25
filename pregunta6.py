"""
Pasemos a trabajar en otro ejemplo para fortalecer aún más nuestro pensamiento algorítmico, en este caso el problema de las n-PokéBolas. Este problema consiste en ubicar n Pokémon en una red de gimnasios de tamaño n x n, sin que los mismos se enfrenten. Recuerda que un Pokémon puede moverse de manera horizontal, vertical y diagonal, además podemos ver una solución al problema de los 4 Pokémon. Nótese que una parte importante para resolver un problema es de qué manera representar la solución, para este caso particular usamos un vector de n posiciones (gimnasios) y el valor almacenado representa la fila donde se ubica dicho Pokémon.
Cuando hayas entendido el problema y tengas una solución en mente, desarrolla un algoritmo que permita hallar al menos una solución para distintas cantidades de Pokémon, y luego completa la siguiente tabla.
"""

class PokeballNode:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.next = None

def is_safe(pokeball, row, col):
    # Verificar si es seguro colocar una PokéBola en la posición (row, col)

    # Verificar si hay alguna PokéBola en la misma columna o diagonal
    current = pokeball
    while current:
        if current.col == col or abs(current.row - row) == abs(current.col - col):
            return False
        current = current.next

    return True

def place_pokeballs(n):
    solutions = []
    stack = []

    def backtrack(row):
        # Caso base: se han colocado todas las PokéBolas
        if row == n:
            pokeball = stack[0]
            solution = []
            while pokeball:
                solution.append(pokeball.row)
                pokeball = pokeball.next
            solutions.append(solution)
            return

        for col in range(n):
            if is_safe(stack[-1], row, col):
                new_pokeball = PokeballNode(row, col)
                stack.append(new_pokeball)
                backtrack(row + 1)
                stack.pop()

    # Iniciar la búsqueda desde la primera fila
    for col in range(n):
        first_pokeball = PokeballNode(0, col)
        stack.append(first_pokeball)
        backtrack(1)
        stack.pop()

    return solutions

# Calcular las soluciones para distintas cantidades de Pokémon
table = []
for n in range(1, 16):
    solutions = place_pokeballs(n)
    all_solutions = len(solutions)
    one_solution = solutions[0] if solutions else "-"
    table.append((n, all_solutions, one_solution))

# Imprimir la tabla de resultados
print("n-pokeballs\tSoluciones distintas\tTodas las soluciones\tUna solución")
for n, all_solutions, one_solution in table:
    print(f"{n}\t\t{all_solutions}\t\t\t\t{one_solution}")