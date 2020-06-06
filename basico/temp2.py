# declaracion de la funcion
def convertir_C_a_F(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

# probar la funcion
celsius1 = 15
# res_F = convertir_C_a_F(celsius1)
print(f'{celsius1} grados Celsius son equivalentes a {convertir_C_a_F(celsius1)} grados Fahrenheit')
# X grados Celsius son equivalentes a Y grados Fahrenheit
# print(f’{nombre} tiene {edad} años’)