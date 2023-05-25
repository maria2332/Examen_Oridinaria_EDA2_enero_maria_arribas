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
from io import StringIO
from unittest.mock import patch

class PokemonTests(unittest.TestCase):
    def test_clasificacion_agua(self):
        pokemon = Pokemon("Squirtle", "Agua")
        expected_output = "Clasificación del Pokémon Squirtle :\nPS: 100\nAtaque: 80\nDefensa: 90\nAtaque Especial: 70\nDefensa Especial: 80\nVelocidad: 60\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            pokemon.clasificacion()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_clasificacion_fuego(self):
        pokemon = Pokemon("Charizard", "Fuego")
        expected_output = "Clasificación del Pokémon Charizard :\nPS: 90\nAtaque: 85\nDefensa: 70\nAtaque Especial: 90\nDefensa Especial: 75\nVelocidad: 80\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            pokemon.clasificacion()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_clasificacion_tierra(self):
        pokemon = Pokemon("Golem", "Tierra")
        expected_output = "Clasificación del Pokémon Golem :\nPS: 95\nAtaque: 100\nDefensa: 120\nAtaque Especial: 45\nDefensa Especial: 75\nVelocidad: 40\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            pokemon.clasificacion()
            self.assertEqual(fake_output.getvalue(), expected_output)

    # Agrega más pruebas para los otros tipos de Pokémon

    def test_clasificacion_tipo_desconocido(self):
        pokemon = Pokemon("Pikachu", "Eléctrico (desconocido)")
        expected_output = "Tipo de Pokémon no reconocido.\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            pokemon.clasificacion()
            self.assertEqual(fake_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()