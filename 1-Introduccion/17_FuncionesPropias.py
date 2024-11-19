def greet(name = "User"):
    print("Hello", name)

def calculo(alto = 10, ancho = 10):
    area = alto * ancho
    perimetro = alto * 2 + ancho * 2
    return area, perimetro

#print("Name :")
#name = input()
#greet(name)

calculo_uno = calculo()
print(calculo_uno)
print("Area", calculo_uno[0])
print("Perimetro", calculo_uno[1])

calculo_dos_a, calculo_dos_b = calculo(15, 5)
print("Area", calculo_dos_a)
print("Perimetro", calculo_dos_b)

calculo_tres_a, calculo_tres_b = calculo(5)
print("Area", calculo_tres_a)
print("Perimetro", calculo_tres_b)