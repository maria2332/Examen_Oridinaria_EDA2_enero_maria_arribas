"""El Profesor Oak le encarga desarrollar los algoritmos para organizar los Pokemon cumpliendo con las siguientes demandas:

Deberá generar 800 Pokemon siguiendo el formato del primer ejercicio contemplando los siguientes tipos:
Agua, Fuego, Tierra, Electrico, Normal, Fantasma y los niveles generados de manera aleatoria;
Deberá cargar los Pokemon generados en dos tablas hash encadenadas, en la primera se deberá agrupar de acuerdo con los tres últimos dígitos del nivel y en la segunda a partir de las iniciales del tipo;
Determinar si el Pokemon Fantasma de nivel 187 está cargado para poder quitarlo porque es un traidor desertor.
Ahora obtenga todos los Pokemon terminados en 78 para asignarlos a una misión de asalto y a los terminados en 37 para una misión de exploración;
Ahora obtenga los Pokemon de tipo Tierra para que custodien al Profesor Oak en una misión de exploración al Bosque Verdanturf y los de tipo Fuego para una misión de exterminación en Cueva Lava."""

import random

class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        print("¡Se ha creado exitosamente un Pokémon llamado", self.nombre, "de tipo", self.tipo, "y nivel", self.nivel, "!")

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

# Generar 800 Pokémon
tipos = ['Agua', 'Fuego', 'Tierra', 'Eléctrico', 'Normal', 'Fantasma']
niveles = [random.randint(1, 1000) for _ in range(800)]
pokemon_list = []
for i in range(800):
    tipo = random.choice(tipos)
    nivel = niveles[i]
    nombre = tipo.capitalize() + str(i+1)
    pokemon = Pokemon(nombre, tipo, nivel)
    pokemon_list.append(pokemon)

# Cargar los Pokémon en las tablas hash
tabla_nivel = {}
tabla_tipo = {}
for pokemon in pokemon_list:
    ultimos_digitos = str(pokemon.nivel)[-3:]
    if ultimos_digitos not in tabla_nivel:
        tabla_nivel[ultimos_digitos] = []
    tabla_nivel[ultimos_digitos].append(pokemon)

    inicial_tipo = pokemon.tipo[0]
    if inicial_tipo not in tabla_tipo:
        tabla_tipo[inicial_tipo] = []
    tabla_tipo[inicial_tipo].append(pokemon)

# Determinar si el Pokémon Fantasma de nivel 187 está cargado
fantasma_187 = None
for pokemon in tabla_tipo.get('F'):
    if pokemon.tipo == 'Fantasma' and pokemon.nivel == 187:
        fantasma_187 = pokemon
        break

if fantasma_187 is not None:
    print("El Pokémon Fantasma de nivel 187 está cargado.")
    # Quitar el Pokémon Fantasma de nivel 187 de la tabla_tipo
    tabla_tipo['F'].remove(fantasma_187)
else:
    print("El Pokémon Fantasma de nivel 187 no está cargado.")

# Obtener todos los Pokémon terminados en 78 para la misión de asalto
mision_asalto = []
for pokemon in pokemon_list:
    if str(pokemon.nivel)[-2:] == '78':
        mision_asalto.append(pokemon)

# Obtener todos los Pokémon terminados en 37 para la misión de exploración
mision_exploracion = []
for pokemon in pokemon_list:
    if str(pokemon.nivel)[-2:] == '37':
        mision_exploracion.append(pokemon)

# Obtener los Pokémon de tipo Tierra para la misión de exploración al Bosque Verdanturf
mision_bosque = []
for pokemon in tabla_tipo.get('T'):
    mision_bosque.append(pokemon)

# Obtener los Pokémon de tipo Fuego para la misión de exterminación en Cueva Lava
mision_cueva = []
for pokemon in tabla_tipo.get('F'):
    mision_cueva.append(pokemon)
