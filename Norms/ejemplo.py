from collections import deque
import time

cola_estudiantes = deque()

cola_estudiantes.append("Carlos")
cola_estudiantes.append("Maria")
cola_estudiantes.append("Pedro")
cola_estudiantes.append("Ana")

print("Estudiantes en la fila:")

for estudiante in cola_estudiantes:
    print("-", estudiante)

print("\nIniciando entrega de tareas...")

while len(cola_estudiantes) > 0:
    estudiante = cola_estudiantes.popleft()
    time.sleep(1)
    print("Tarea recibida de:", estudiante)
    print("Estudiantes faltantes:", len(cola_estudiantes))

print("\nTodos los estudiantes entregaron su tarea.")