user_data = [
    "Luis", 
    23, 
    1997.68,
    True]
print(user_data)

print("Nombre : " + user_data[0])
print("Suedo Actual : " + str(user_data[2]))
print("Ingrese nuevo sueldo")
user_data[2] = float(input())
print("Suedo Actual : " + str(user_data[2]))

print("User : " + (user_data[0])[0] + user_data[0][1])