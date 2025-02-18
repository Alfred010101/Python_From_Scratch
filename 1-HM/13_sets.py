primero = {1, 2, 3, 4, 5, 6}
primero.remove(1)
primero.add(7)

print(primero)

segundo = [1, 3, 6, 8, 10]
segundo = set(segundo)

print(segundo)

# union
print(segundo | primero)

# interseccion
print(primero & segundo)

# diferencia
print(primero - segundo)
print(segundo - primero)

# diferencia simetrica
print(primero ^ segundo)

if 5 in segundo:
    print("true")
else:
    print("false")
