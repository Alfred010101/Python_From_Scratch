pila = []
pila.append(43)
pila.append(3)
pila.append(4)
pila.append(34)
print(pila)
ultimo = pila.pop()
print(ultimo)
print(pila)
pila.pop()
pila.pop()
pila.pop()
if not pila:
    print("pila vacia")
