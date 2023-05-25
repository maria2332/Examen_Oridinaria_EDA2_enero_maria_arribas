"""
Ash Ketchum, líder del equipo de entrenadores Pokemon, tiene dificultades para transmitir los mensajes al Centro Pokemon, dado que los mismos son muy largos y los satélites espías del Equipo Rocket los interceptan, en un lapso muy corto desde que se transmiten. Por lo cual, nos solicita desarrollar un algoritmo que permita comprimir los mensajes para enviarlos más rápido y no puedan ser interceptados. Contemplando los siguientes requerimientos, implementar un algoritmo que pueda crear un árbol de Huffman a partir de la siguiente tabla y desarrollar las funciones para comprimir y descomprimir un mensaje.

Símbolo	Frecuencia
T	0.15
O	0.15
A	0.12
E	0.10
H	0.09
S	0.07
P	0.07
M	0.07
N	0.06
C	0.06
D	0.05
Z	0.04
K	0.03
,	0.03
"""

class HuffmanNode:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

def build_huffman_tree(frequencies):
    nodes = [HuffmanNode(symbol, freq) for symbol, freq in frequencies.items()]
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = HuffmanNode(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        nodes.append(parent)
    return nodes[0]

def generate_huffman_codes(root):
    codes = {}

    def traverse(node, code):
        if node.symbol:
            codes[node.symbol] = code
        else:
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')

    traverse(root, '')
    return codes

def compress_message(message, codes):
    compressed = ''
    for symbol in message:
        compressed += codes[symbol]
    return compressed

def decompress_message(compressed, root):
    decompressed = ''
    current_node = root
    for bit in compressed:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.symbol:
            decompressed += current_node.symbol
            current_node = root
    return decompressed

# Tabla de frecuencias
frequencies = {
    'T': 0.15,
    'O': 0.15,
    'A': 0.12,
    'E': 0.10,
    'H': 0.09,
    'S': 0.07,
    'P': 0.07,
    'M': 0.07,
    'N': 0.06,
    'C': 0.06,
    'D': 0.05,
    'Z': 0.04,
    'K': 0.03,
    ',': 0.03
}

# Construir el árbol de Huffman
root = build_huffman_tree(frequencies)

# Generar códigos de compresión
codes = generate_huffman_codes(root)

# Comprimir un mensaje
message = "TOAST, TOAST!"
compressed_message = compress_message(message, codes)
print("Mensaje comprimido:", compressed_message)

# Descomprimir un mensaje
decompressed_message = decompress_message(compressed_message, root)
print("Mensaje descomprimido:", decompressed_message)
