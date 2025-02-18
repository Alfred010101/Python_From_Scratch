usuarios = [
    ["Alfred", 5],
    ["Diego", 2],
    ["Bety", 9],
    ["Luis", 6]
]

nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

nombres = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(nombres)
