punto = {"x": 25, "y": 50}
print(punto)

print(punto["x"])
print(punto["y"])

punto["z"] = 45
print(punto)

if "algo" in punto:
    print("si esta")
else:
    print("no existe")

print(punto.get("algo mas", "no existe"))

del punto["z"]
del (punto["y"])
print(punto)

punto["y"] = 45

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for key, value in punto.items():
    print(key, value)


usuarios = [
    {"id": 1, "nombre": "J"},
    {"id": 2, "nombre": "Alfred"},
    {"id": 3, "nombre": "Arista"}
]

for usuario in usuarios:
    print(usuario["nombre"])
