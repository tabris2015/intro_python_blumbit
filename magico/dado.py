import random
class Dado():
    # constructor __init__()
    def __init__(self, lados=6):
        self.lados = lados
        self.valor = 0
        
    def lanzar(self):
        # print('lanzando...')
        self.valor = random.randrange(1, self.lados + 1)
        return self.valor

    # operador de suma '+'
    def __add__(self, otro):
        return self.valor + otro.valor
    
    # representacion del objeto
    def __repr__(self):
        return f'<{self.valor}>'

    # comparador de igualdad '=='
    def __eq__(self, otro):
        return self.valor == otro.valor
    
    # comparador de desigualdad '!='
    def __ne__(self, otro):
        return self.valor == otro.valor
