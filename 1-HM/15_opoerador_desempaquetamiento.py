def funtion(a, b, c, d, e, f):
    return a + b + c + d + e + f


datos = [5, 2, 5, 6, 3, 9]
print(funtion(*datos))
print(funtion(*[5, 2, 5, 6, 3, 9]))
# a = {"x": 23, "y": 5}
# b = {"z": 32}
nuv = {**{"x": 23, "y": 5}, **{"z": 32}}
print(nuv)
