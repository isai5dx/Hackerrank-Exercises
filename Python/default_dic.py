from collections import defaultdict

# 1. Inicializamos un diccionario que, por defecto, crea una lista vacía
# si intentamos acceder a una palabra que aún no existe.
d = defaultdict(list)

# 2. Leemos 'n' (cantidad de palabras en Grupo A) y 'm' (Grupo B).
n, m = map(int, input().split())

# 3. Llenado del Grupo A:
# Usamos range(1, n + 1) porque HackerRank pide posiciones basadas en 1.
for i in range(1, n + 1):
    word = input().strip()
    # Guardamos la posición 'i' en la lista correspondiente a esa palabra.
    d[word].append(i)

# 4. Procesamiento del Grupo B:
for _ in range(m):
    word_b = input().strip()
    
    # Verificamos si la palabra existe en nuestro diccionario de posiciones.
    if word_b in d:
        # El asterisco (*) 'desempaqueta' la lista para imprimir los números 
        # separados por espacios en una sola línea.
        print(*d[word_b])
    else:
        # Si la palabra nunca apareció en el Grupo A, imprimimos -1.
        print("-1")
