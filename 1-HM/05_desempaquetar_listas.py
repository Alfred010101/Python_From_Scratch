numeros = list(range(1,6))

uno, dos, tres, cuatro, cinco = numeros

primero, *resto = numeros

first, *medio, last = numeros
print(uno, dos, tres, cuatro, cinco)
print(primero, resto)
print(first, medio, last)