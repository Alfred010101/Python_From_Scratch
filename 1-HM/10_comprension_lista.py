usuarios = [
    ["Alfred", 5],
    ["Diego", 2],
    ["Bety", 9],
    ["Luis", 6]
]

# transformacion
nombres = [usuario[0] for usuario in usuarios]
print(nombres)

# filtrar
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)

# transformacion y filtrar
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)
