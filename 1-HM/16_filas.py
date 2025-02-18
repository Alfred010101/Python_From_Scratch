from collections import deque

fila = deque([1, 3, 5, 6, 2, 9])
print(fila)

fila.append(8)
print(fila)
fila.popleft()
print(fila)
