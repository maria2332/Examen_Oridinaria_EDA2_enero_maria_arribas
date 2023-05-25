"""
Copia el ejercicio anterior y realicemos la siguiente modificación:
Junto al método init y clasificacion, sobrescriba el método especial de Python, el método str, que tiene el siguiente formato:
def __str__(self):
return "Lo que quiero mostrar"
Este método nos sirve para imprimir por pantalla la información de un objeto, si tenemos un objeto pokemon1 creado y realizamos print(pokemon1), Python ejecutará el contenido del método str (el método str lo que tiene que hacer es maquetar la información que desea en un string).

Experimentación 
Implementa el método str y haz que muestre el nombre y el tipo del Pokemon. Crea una lista con un numero arbitrario de objetos tipo Pokemon. Recorre los elementos de la lista, y utiliza el método print de esos objetos para visualizar por pantalla la información del str.
"""

class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        print("¡Se ha creado exitosamente un Pokémon llamado", self.nombre, "de tipo", self.tipo, "!")

    def clasificacion(self):
        if self.tipo == 'Agua':
            return "Clasificación del Pokémon " + self.nombre + ":\nPS: 100\nAtaque: 80\nDefensa: 90\nAtaque Especial: 70\nDefensa Especial: 80\nVelocidad: 60"
        elif self.tipo == 'Fuego':
            return "Clasificación del Pokémon " + self.nombre + ":\nPS: 90\nAtaque: 85\nDefensa: 70\nAtaque Especial: 90\nDefensa Especial: 75\nVelocidad: 80"
        elif self.tipo == 'Tierra':
            return "Clasificación del Pokémon " + self.nombre + ":\nPS: 95\nAtaque: 100\nDefensa: 120\nAtaque Especial: 45\nDefensa Especial: 75\nVelocidad: 40"
        elif self.tipo == 'Eléctrico':
            return "Clasificación del Pokémon " + self.nombre + ":\nPS: 80\nAtaque: 70\nDefensa: 60\nAtaque Especial: 110\nDefensa Especial: 80\nVelocidad: 100"
        elif self.tipo == 'Normal':
            return "Clasificación del Pokémon " + self.nombre + ":\nPS: 70\nAtaque: 80\nDefensa: 70\nAtaque Especial: 80\nDefensa Especial: 70\nVelocidad: 90"
        elif self.tipo == 'Fantasma':
            return "Clasificación del Pokémon " + self.nombre + ":\nPS: 60\nAtaque: 45\nDefensa: 50\nAtaque Especial: 115\nDefensa Especial: 100\nVelocidad: 75"
        else:
            return "Tipo de Pokémon no reconocido."

    def __str__(self):
        return "Nombre: " + self.nombre + "\nTipo: " + self.tipo + "\n"


# Test

import unittest

class PokemonTests(unittest.TestCase):
    def test_clasificacion_agua(self):
        pokemon = Pokemon("Squirtle", "Agua")
        clasificacion_esperada = "Clasificación del Pokémon Squirtle:\nPS: 100\nAtaque: 80\nDefensa: 90\nAtaque Especial: 70\nDefensa Especial: 80\nVelocidad: 60"
        self.assertEqual(pokemon.clasificacion(), clasificacion_esperada)

    def test_clasificacion_fuego(self):
        pokemon = Pokemon("Charizard", "Fuego")
        clasificacion_esperada = "Clasificación del Pokémon Charizard:\nPS: 90\nAtaque: 85\nDefensa: 70\nAtaque Especial: 90\nDefensa Especial: 75\nVelocidad: 80"
        self.assertEqual(pokemon.clasificacion(), clasificacion_esperada)

    def test_clasificacion_tierra(self):
        pokemon = Pokemon("Golem", "Tierra")
        clasificacion_esperada = "Clasificación del Pokémon Golem:\nPS: 95\nAtaque: 100\nDefensa: 120\nAtaque Especial: 45\nDefensa Especial: 75\nVelocidad: 40"
        self.assertEqual(pokemon.clasificacion(), clasificacion_esperada)

    # Agrega más pruebas para los otros tipos de Pokémon

    def test_clasificacion_tipo_desconocido(self):
        pokemon = Pokemon("Pikachu", "Eléctrico (desconocido)")
        clasificacion_esperada = "Tipo de Pokémon no reconocido."
        self.assertEqual(pokemon.clasificacion(), clasificacion_esperada)

    def test_str(self):
        pokemon = Pokemon("Bulbasaur", "Planta")
        str_esperado = "Nombre: Bulbasaur\nTipo: Planta\n"
        self.assertEqual(str(pokemon), str_esperado)

if __name__ == '__main__':
    unittest.main()