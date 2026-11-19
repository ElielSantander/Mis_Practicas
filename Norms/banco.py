from collections import deque
import time
cola_turnos = deque()
cola_turnos.append("juano")
cola_turnos.append("Memo farias")
cola_turnos.append("Yordi")

print("Clientes en la fila:")
for turnos in cola_turnos:
    print("-", turnos)

while len(cola_turnos) > 0:
    cliente = cola_turnos.popleft()
    time.sleep(1)
    print("Cliente atendido:", cliente)
    print("Clientes faltantes:", len(cola_turnos))