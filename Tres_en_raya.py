from random import choice
JUGADOR_X = 'X'
JUGADOR_O = 'O'

def generar_tablero():
    tableroero = {1:" ", 2:" ", 3:" ",
               4:" ", 5:" ", 6:" ",
               7:" ", 8:" ", 9:" "}
    
    return tableroero

def movimiento(pos, tablero, turno):
    if tablero.get(pos) == " ":
        tablero[pos] = turno

def imprimir_tableroero(tablero):
    print(f'{tablero[1]} | {tablero[2]} | {tablero[3]}')
    print(f'---------')
    print(f'{tablero[4]} | {tablero[5]} | {tablero[6]}')
    print(f'---------')
    print(f'{tablero[7]} | {tablero[8]} | {tablero[9]}')


def comprobar(tablero):
    ganador = False
    if (tablero[1] == tablero[2] == tablero[3] != " ") or \
        (tablero[4] == tablero[5] == tablero[6] != " ") or \
        (tablero[7] == tablero[8] == tablero[9] != " ") or \
        (tablero[1] == tablero[4] == tablero[4] != " ") or \
        (tablero[2] == tablero[5] == tablero[8] != " ") or \
        (tablero[3] == tablero[6] == tablero[9] != " ") or \
        (tablero[1] == tablero[5] == tablero[9] != " ") or \
        (tablero[3] == tablero[5] == tablero[7] != " "):
        ganador = True
    return ganador

def jugar():
    print("---------------------------")
    print("     TRES EN RAYA          ")
    print("---------------------------")
    print()

    tablero = generar_tablero()
    imprimir_tableroero(tablero)
    print()
    contador = 1
    gana = False
    turno = choice([JUGADOR_X,JUGADOR_O])
    
    while True:
        
        while True:
            posicion = int(input(f'{turno}: Intoduzca la posición: '))
            
            if posicion < 1 or posicion > 9:
                print("Posición inválida")
            elif tablero[posicion] != " ":
                print("Posición ocupada")
            else:
                contador += 1
                break

        movimiento(posicion, tablero, turno)
        imprimir_tableroero(tablero)
        

        if contador >= 5:
            gana = comprobar(tablero)
            if gana:
                print(f'Ha ganado {turno}')
                break
            elif contador == 9:
                print("Empate")
                break

        if turno == JUGADOR_X:
            turno = JUGADOR_O
        else:
            turno = JUGADOR_X

        
if __name__ == "__main__":
    jugar()