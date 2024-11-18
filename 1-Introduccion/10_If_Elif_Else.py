print("Ingresa tu edad : ")
edad = int(input())

if edad >= 18 and edad < 60:
    print("Eres mayor")
elif edad >= 60:
    print("Eres un adulto mayor")
else:
    print("Eres un bebe")

print("Fin")