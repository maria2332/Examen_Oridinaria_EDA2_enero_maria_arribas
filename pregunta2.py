"""
Crea una clase llamada Pokemon.py que tenga los atributos nombre y tipo. Crea el constructor de la clase. Añadir en el constructor un print para informar de que el Pokemon se ha creado con éxito. Crear un método llamado clasificacion que clasifique a los Pokemon según su tipo de la siguiente manera:
los PS, el Ataque, la Defensa, el Ataque Especial, la Defensa Especial y la Velocidad.

Experimentación
Crea una lista con un numero arbitrario de objetos tipo Pokemon. Recorre los elementos de la lista, y prueba a ejecutar el método clasificacion de cada objeto que has creado.
"""

class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        print("¡Se ha creado exitosamente un Pokémon llamado", self.nombre, "de tipo", self.tipo, "!")

    def clasificacion(self):
        if self.tipo == 'Agua':
            print("Clasificación del Pokémon", self.nombre, ":")
            print("PS: 100")
            print("Ataque: 80")
            print("Defensa: 90")
            print("Ataque Especial: 70")
            print("Defensa Especial: 80")
            print("Velocidad: 60")
        elif self.tipo == 'Fuego':
            print("Clasificación del Pokémon", self.nombre, ":")
            print("PS: 90")
            print("Ataque: 85")
            print("Defensa: 70")
            print("Ataque Especial: 90")
            print("Defensa Especial: 75")
            print("Velocidad: 80")
        elif self.tipo == 'Tierra':
            print("Clasificación del Pokémon", self.nombre, ":")
            print("PS: 95")
            print("Ataque: 100")
            print("Defensa: 120")
            print("Ataque Especial: 45")
            print("Defensa Especial: 75")
            print("Velocidad: 40")
        elif self.tipo == 'Eléctrico':
            print("Clasificación del Pokémon", self.nombre, ":")
            print("PS: 80")
            print("Ataque: 70")
            print("Defensa: 60")
            print("Ataque Especial: 110")
            print("Defensa Especial: 80")
            print("Velocidad: 100")
        elif self.tipo == 'Normal':
            print("Clasificación del Pokémon", self.nombre, ":")
            print("PS: 70")
            print("Ataque: 80")
            print("Defensa: 70")
            print("Ataque Especial: 80")
            print("Defensa Especial: 70")
            print("Velocidad: 90")
        elif self.tipo == 'Fantasma':
            print("Clasificación del Pokémon", self.nombre, ":")
            print("PS: 60")
            print("Ataque: 45")
            print("Defensa: 50")
            print("Ataque Especial: 115")
            print("Defensa Especial: 100")
            print("Velocidad: 75")
        else:
            print("Tipo de Pokémon no reconocido.")

# Ejemplo de uso:
pikachu = Pokemon("Pikachu", "Eléctrico")
pikachu.clasificacion()


# Crear una lista de Pokémon
pokemons = [
    Pokemon("Pikachu", "Eléctrico"),
    Pokemon("Charizard", "Fuego"),
    Pokemon("Blastoise", "Agua"),
    Pokemon("Sandslash", "Tierra"),
    Pokemon("Gengar", "Fantasma")
]

# Recorrer la lista y ejecutar el método clasificacion() de cada Pokémon
for pokemon in pokemons:
    pokemon.clasificacion()


# Tests

def test_clasificacion_agua():
    pikachu = Pokemon("Pikachu", "Agua")
    pikachu.clasificacion()

def test_clasificacion_fuego():
    charizard = Pokemon("Charizard", "Fuego")
    charizard.clasificacion()

def test_clasificacion_tierra():
    sandslash = Pokemon("Sandslash", "Tierra")
    sandslash.clasificacion()

def test_clasificacion_electrico():
    pikachu = Pokemon("Pikachu", "Eléctrico")
    pikachu.clasificacion()

def test_clasificacion_normal():
    normal_pokemon = Pokemon("Normalmon", "Normal")
    normal_pokemon.clasificacion()

def test_clasificacion_fantasma():
    gengar = Pokemon("Gengar", "Fantasma")
    gengar.clasificacion()

def test_clasificacion_desconocido():
    unknown_pokemon = Pokemon("Unknownmon", "Desconocido")
    unknown_pokemon.clasificacion()

def test_clasificacion_lista_pokemons():
    pokemons = [
        Pokemon("Pikachu", "Eléctrico"),
        Pokemon("Charizard", "Fuego"),
        Pokemon("Blastoise", "Agua"),
        Pokemon("Sandslash", "Tierra"),
        Pokemon("Gengar", "Fantasma")
    ]

    for pokemon in pokemons:
        pokemon.clasificacion()

# Ejecutar los tests
test_clasificacion_agua()
test_clasificacion_fuego()
test_clasificacion_tierra()
test_clasificacion_electrico()
test_clasificacion_normal()
test_clasificacion_fantasma()
test_clasificacion_desconocido()
test_clasificacion_lista_pokemons()
