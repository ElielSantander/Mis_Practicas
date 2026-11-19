from collections import deque
import time

cola_reproduccion = deque()

# Agregar canciones a la cola
cola_reproduccion.append("1, Cuando no era cantante")
cola_reproduccion.append("2, Sicko Mode")
cola_reproduccion.append("3, Rene")

# Mostrar las canciones de espera
print("Canciones de espera:")
for cancion in cola_reproduccion:
    print("_", cancion)

print("iniciando reproduccion")

# El reproductor procesa la cola, canción por canción
while cola_reproduccion:
    cancion_actual = cola_reproduccion.popleft()
    print(f"Sonando ahora: {cancion_actual}")
    time.sleep(1)  # Simula la duración del tema
    print(f"Finalizó: {cancion_actual}")

# Mostrar cuántas canciones quedan en la cola
print(f"Quedan {len(cola_reproduccion)} canciones en la cola")
print("La cola de reproducción ha finalizado")