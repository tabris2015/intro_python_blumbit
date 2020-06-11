class Carro():
    # atributos
    modelo = ''
    anho = 0
    gasolina = 100
    esta_encendido = False
    # constructor (inicializa el objeto)
    def __init__(self, modelo, anho):
        self.modelo = modelo
        self.anho = anho
    # metodos
    def encender(self):
        self.esta_encendido = True
        print(f'{self.modelo} encendido')
    
    def apagar(self):
        self.esta_encendido = False
        print(f'{self.modelo} apagado')

    def acelerar(self):
        if self.gasolina > 0: # solo si hay gasolina
            if self.esta_encendido:
                print('brum brum')
                self.gasolina -= 10
            else:
                print('primero encienda el carro')
        else:
            print('gasolina insuficiente')

class Camion(Carro):
    marca = ''