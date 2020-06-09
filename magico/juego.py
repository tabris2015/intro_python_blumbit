from dado import Dado
# juego de dados tiene las siguientes <<reglas>>
# 2-4 jugadores
# en cada turno:
# el jugador lanza los dados

# el juego, termina cuando un jugador llega a 100 puntos

# funcion para verificar el fin del juego
def hay_ganador(dic_jugadores):
    for jugador, puntos in dic_jugadores.items():
        if puntos >= 100:
            return True
    return False
# preguntar el numero de jugadores
n_jugadores = int(input('numero de jugadores (2 a 4)'))
if n_jugadores < 2 or n_jugadores > 4:
    print('numero invalido de jugadores')
    exit()

dic_jugadores = {}
for i in range(n_jugadores):
    dic_jugadores[f'Jugador{i+1}'] = 0

# si los dados son iguales, se suma el numero obtenido al puntaje
# si un dado es 1 se resta el otro dado al puntaje
# si obtienes 3 en los dos dados, lanza de nuevo (sumo el puntaje)
# si obtienes 5 en los dos dados, no se suma el puntaje y pasa al siguiente
dado1 = Dado()
dado2 = Dado()
while not hay_ganador(dic_jugadores):
    # lanza cada jugador y se acumulan los puntos
    for jugador in dic_jugadores:
        input(f'lanza el {jugador}: ')          # pausa para el lanzamiento
        dado1.lanzar()
        dado2.lanzar()
        print(f'resultado: {dado1} , {dado2}')
        # logica del juego
        if dado1 == dado2:
            if dado1.valor == 5:
                # no se suma y pasa al siguiente
                print('pasa al siguiente jugador')
                continue
            if dado1.valor == 3:
                # sumo el puntaje
                print('suma al puntaje')
                dic_jugadores[jugador] += dado1.valor*4
                # lanzar de nuevo
                input('lanzar de nuevo')
                dado1.lanzar()
                dado2.lanzar()
                print(f'resultado: {dado1} , {dado2}')
                if dado1 == dado2:
                    print('suma al puntaje')
                    dic_jugadores[jugador] += dado1.valor*4
            else:
                # sumo el puntaje
                print('suma al puntaje')
                dic_jugadores[jugador] += dado1.valor*4
            
        elif dado1.valor == 1:
            # resto el puntaje 
            print('resta al puntaje')    
            dic_jugadores[jugador] -= dado2.valor
        elif dado2.valor == 1:
            print('resta al puntaje') 
            dic_jugadores[jugador] -= dado1.valor

    print(f'puntajes: {dic_jugadores}')

max_puntos = 0
for jugador, puntos in dic_jugadores.items():
    if puntos > max_puntos:
        max_puntos = puntos

for jugador, puntos in dic_jugadores.items():
    if puntos == max_puntos:
        print(f"GANO {jugador}")
        break