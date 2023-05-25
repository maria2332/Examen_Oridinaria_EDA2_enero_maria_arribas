"""
Crea una clase llamada Pokeball.py que tenga los atributos peso, nombre, precio y fecha de fabricación. Crea el constructor de la clase. Añade en el constructor un print para informar de que la Pokeball se ha creado con éxito.
Crea el método str para visualizar por pantalla la información de las Pokeballs.

Experimentación 
Crea algunas Pokeballs. Prueba a mostrar los datos de algunas Pokeballs ordenadas por su fecha de fabricación y a modificar algún valor, por ejemplo, prueba a modificar el precio de una de las Pokeballs.
"""

class Pokeball:
    def __init__(self, peso, nombre, precio, fecha_fabricacion):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_fabricacion = fecha_fabricacion
        print("¡Se ha creado exitosamente una Pokeball llamada", self.nombre, "!")

    def __str__(self):
        return f"Información de la Pokeball:\nNombre: {self.nombre}\nPeso: {self.peso} gramos\nPrecio: ${self.precio}\nFecha de fabricación: {self.fecha_fabricacion}"

# Ejemplo de uso
pokeball1 = Pokeball(100, "Superball", 200, "10/05/2023")
print(pokeball1)


from datetime import datetime

class Pokeball:
    def __init__(self, peso, nombre, precio, fecha_fabricacion):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_fabricacion = fecha_fabricacion
        print("¡Se ha creado exitosamente una Pokeball llamada", self.nombre, "!")

    def __str__(self):
        return f"Información de la Pokeball:\nNombre: {self.nombre}\nPeso: {self.peso} gramos\nPrecio: ${self.precio}\nFecha de fabricación: {self.fecha_fabricacion}"

# Crear algunas Pokeballs
pokeball1 = Pokeball(100, "Superball", 200, datetime(2023, 5, 10))
pokeball2 = Pokeball(80, "Ultraball", 300, datetime(2023, 4, 20))
pokeball3 = Pokeball(120, "Masterball", 500, datetime(2023, 6, 5))

# Mostrar los datos de las Pokeballs ordenadas por fecha de fabricación
pokeballs = [pokeball1, pokeball2, pokeball3]
pokeballs_sorted = sorted(pokeballs, key=lambda x: x.fecha_fabricacion)
for pokeball in pokeballs_sorted:
    print(pokeball)

# Modificar el precio de una Pokeball
pokeball2.precio = 350
print("Precio modificado de la Ultraball:", pokeball2.precio)


# Test

import unittest
from datetime import datetime

class TestPokeball(unittest.TestCase):
    def test_pokeball_str(self):
        pokeball = Pokeball(100, "Superball", 200, "10/05/2023")
        expected_output = "Información de la Pokeball:\nNombre: Superball\nPeso: 100 gramos\nPrecio: $200\nFecha de fabricación: 10/05/2023"
        self.assertEqual(str(pokeball), expected_output)

    def test_pokeball_sort(self):
        pokeball1 = Pokeball(100, "Superball", 200, datetime(2023, 5, 10))
        pokeball2 = Pokeball(80, "Ultraball", 300, datetime(2023, 4, 20))
        pokeball3 = Pokeball(120, "Masterball", 500, datetime(2023, 6, 5))

        pokeballs = [pokeball1, pokeball2, pokeball3]
        expected_order = [pokeball2, pokeball1, pokeball3]

        sorted_pokeballs = sorted(pokeballs, key=lambda x: x.fecha_fabricacion)
        self.assertEqual(sorted_pokeballs, expected_order)

    def test_modify_pokeball_price(self):
        pokeball = Pokeball(80, "Ultraball", 300, datetime(2023, 4, 20))
        pokeball.precio = 350
        self.assertEqual(pokeball.precio, 350)

if __name__ == "__main__":
    unittest.main()