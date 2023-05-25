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



# Tests
import unittest

class TestPokemon(unittest.TestCase):
    def test_clasificacion_agua(self):
        pokemon = Pokemon("Squirtle", "Agua")
        expected_output = """Clasificación del Pokémon Squirtle :
PS: 100
Ataque: 80
Defensa: 90
Ataque Especial: 70
Defensa Especial: 80
Velocidad: 60
"""
        with self.assertLogs(level="INFO") as log:
            pokemon.clasificacion()
            self.assertEqual(log.output, [expected_output])

    def test_clasificacion_fuego(self):
        pokemon = Pokemon("Charmander", "Fuego")
        expected_output = """Clasificación del Pokémon Charmander :
PS: 90
Ataque: 85
Defensa: 70
Ataque Especial: 90
Defensa Especial: 75
Velocidad: 80
"""
        with self.assertLogs(level="INFO") as log:
            pokemon.clasificacion()
            self.assertEqual(log.output, [expected_output])

    def test_clasificacion_tierra(self):
        pokemon = Pokemon("Sandshrew", "Tierra")
        expected_output = """Clasificación del Pokémon Sandshrew :
PS: 95
Ataque: 100
Defensa: 120
Ataque Especial: 45
Defensa Especial: 75
Velocidad: 40
"""
        with self.assertLogs(level="INFO") as log:
            pokemon.clasificacion()
            self.assertEqual(log.output, [expected_output])

    def test_clasificacion_electrico(self):
        pokemon = Pokemon("Pikachu", "Eléctrico")
        expected_output = """Clasificación del Pokémon Pikachu :
PS: 80
Ataque: 70
Defensa: 60
Ataque Especial: 110
Defensa Especial: 80
Velocidad: 100
"""
        with self.assertLogs(level="INFO") as log:
            pokemon.clasificacion()
            self.assertEqual(log.output, [expected_output])

    def test_clasificacion_normal(self):
        pokemon = Pokemon("Snorlax", "Normal")
        expected_output = """Clasificación del Pokémon Snorlax :
PS: 70
Ataque: 80
Defensa: 70
Ataque Especial: 80
Defensa Especial: 70
Velocidad: 90
"""
        with self.assertLogs(level="INFO") as log:
            pokemon.clasificacion()
            self.assertEqual(log.output, [expected_output])

    def test_clasificacion_fantasma(self):
        pokemon = Pokemon("Gengar", "Fantasma")
        expected_output = """Clasificación del Pokémon Gengar :
PS: 60
Ataque: 45
Defensa: 50
Ataque Especial: 115
Defensa Especial: 100
Velocidad: 75
"""
        with self.assertLogs(level="INFO") as log:
            pokemon.clasificacion()
            self.assertEqual(log.output, [expected_output])

    def test_clasificacion_desconocido(self):
        pokemon = Pokemon("Unknown", "Desconocido")
        expected_output = "Tipo de Pokémon no reconocido."
        with self.assertLogs(level="INFO") as log:
            pokemon.clasificacion()
            self.assertEqual(log.output, [expected_output])

if __name__ == "__main__":
    unittest.main()
