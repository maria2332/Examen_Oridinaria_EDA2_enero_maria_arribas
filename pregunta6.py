"""
Pasemos a trabajar en otro ejemplo para fortalecer aún más nuestro pensamiento algorítmico, en este caso el problema de las n-PokéBolas. Este problema consiste en ubicar n Pokémon en una red de gimnasios de tamaño n x n, sin que los mismos se enfrenten. Recuerda que un Pokémon puede moverse de manera horizontal, vertical y diagonal, además podemos ver una solución al problema de los 4 Pokémon. Nótese que una parte importante para resolver un problema es de qué manera representar la solución, para este caso particular usamos un vector de n posiciones (gimnasios) y el valor almacenado representa la fila donde se ubica dicho Pokémon.
Cuando hayas entendido el problema y tengas una solución en mente, desarrolla un algoritmo que permita hallar al menos una solución para distintas cantidades de Pokémon, y luego completa la siguiente tabla.
"""

import random

def solve_n_pokeballs(n):
    solutions = []
    all_solutions = []
    board = [-1] * n

    def is_safe(row, col):
        for i in range(row):
            if (
                board[i] == col
                or board[i] - i == col - row
                or board[i] + i == col + row
            ):
                return False
        return True

    def backtrack(row):
        if row == n:
            solution = board.copy()
            solutions.append(solution)
            all_solutions.append(solution)
        else:
            for col in range(n):
                if is_safe(row, col):
                    board[row] = col
                    backtrack(row + 1)
                    board[row] = -1

    backtrack(0)

    num_solutions = len(solutions)
    num_all_solutions = len(all_solutions)

    if num_solutions > 0:
        random_solution = random.choice(solutions)
    else:
        random_solution = []

    return num_solutions, num_all_solutions, random_solution

print("n-PokéBolas\tSoluciones distintas\tTodas las soluciones\tUna solución")
for n in range(1, 16):
    num_solutions, num_all_solutions, random_solution = solve_n_pokeballs(n)
    print(f"{n}\t\t{num_solutions}\t\t\t{num_all_solutions}\t\t\t\t{random_solution}")