datos = ["uno", "dos", "tres", "cuatro", "uno"]

datos.insert(2, "Punto")
datos.append("final")
print(datos)
datos.remove("uno")
datos.pop()
datos.pop(2)
print(datos)
del datos[3]
print(datos)
datos.clear()
print(datos)