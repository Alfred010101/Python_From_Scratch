numero_uno = 17
numero_dos = 34
numero_tres = 17

print(numero_uno != numero_dos and numero_tres == numero_uno)

print(10 == numero_dos or 5 == numero_uno)

#Las siguientes operaciones logicas no son lo mismo
print(not 10 == numero_dos or 5 == numero_uno) #(!false or false)

print(10 == numero_dos or not 5 == numero_uno) #(false or !false)

print(not (10 == numero_dos or 5 == numero_uno)) #!(false or false)