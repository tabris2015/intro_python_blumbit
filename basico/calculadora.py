# calculadora simple
# esta calculadora recibe una operacion de 2 numeros desde teclado
# la entrada debe estar en este formato: <n1> <op> <n2>
# se soportan las siguientes operaciones: 
# multiplicacion: *
# division: /
# suma: +
# resta: -
# los numeros tienen que ser numeros enteros positivos
# ejemplo:
# entrada: '9 - 1'
# salida: '8'

op_validas = ['*', '/', '-', '+']
# recibir la entrada
texto = input('ingrese la operacion: ')
resultado = 0
# validar la entrada
if len(texto.split()) != 3:
    print('ingrese una operacion valida en este formato: <n1> <op> <n2>')
else:
    palabras = texto.split()
    n1_str = palabras[0]
    operador = palabras[1]
    n2_str = palabras[2]  
    # validar los componentes
    if n1_str.isdigit() and n2_str.isdigit() and operador in op_validas:
        n1 = int(n1_str)
        n2 = int(n2_str)
        # realizar la operacion
        if operador == '*':
            resultado = n1 * n2
        elif operador == '/':
            resultado = n1 / n2
        elif operador == '+':
            resultado = n1 + n2
        elif operador == '-':
            resultado = n1 - n2 
        
        # mostrar resultados
        print(f'resultado: {resultado}')
    else:
        print('ingrese solamente numeros enteros y operadores validos')
        