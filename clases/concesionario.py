from carro import Carro

# instanciar o crear objeto de tipo Carro
corolla = Carro('corolla', 2015)

corolla.encender()
corolla.apagar()
corolla.acelerar()


hummer = Carro('hummer', 2019)
hummer.encender()
hummer.acelerar()
for i in range(20):
    hummer.acelerar()

hummer.apagar()