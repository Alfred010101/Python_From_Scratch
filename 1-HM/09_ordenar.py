numeros = [3, 6, 5, 2, 8, 32, 24, 76, 9, 0, 24, 65, 64]
numeros.sort()
print(numeros)

num = sorted(numeros, reverse=True)
print(num)

numeros.sort(reverse=True)
print(numeros)

usuarios = [
    ["Ab", 5],
    ["Hc", 2],
    ["Bd", 9],
    ["Zr", 6]
]


def ordenar(elem):
    return elem[1]


usuarios.sort()
print(usuarios)
usuarios.sort(key=lambda elemento: elemento[1], reverse=True)
print(usuarios)
