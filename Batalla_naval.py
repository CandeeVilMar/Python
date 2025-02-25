from random import choice

DIMENSION = 10

def generar_tablero():
    matriz = []
    for _ in range(DIMENSION):
        fila = []
        for _ in range(DIMENSION):
            fila.append(" ")
        matriz.append(fila)
    return matriz

def agregar_barcos(lista, tablero): #Agrega los barcos a las posiciones dadas en la tupla en el tablero correspondiente
    for elemento in lista:
        fila, columna = elemento
        tablero[fila][columna] = "B"

def generar_diccionario(tablero):
    diccionario = {}
    diccionario["mi tablero"] = tablero
    diccionario["tablero oponente"] = generar_tablero()
    return diccionario

def imprimir(dic):
    tablero = dic["mi tablero"]
    tablero_vista = dic["tablero oponente"]
    
    numeros_arriba = "    " + " ".join(f"{i:^3}" for i in range(DIMENSION)) + "       " + " ".join(f"{i:^3}" for i in range(DIMENSION))
    print(numeros_arriba)

    for i, (fila1, fila2) in enumerate(zip(tablero, tablero_vista)):
        if i == 0:
            print("   +" + "---+" * DIMENSION + "     +" + "---+" * DIMENSION)
        print(f"{i: >2} |" + "|".join(f" {columna1} " for columna1 in fila1) + f"|   {i: >2} |" + "|".join(f" {columna2} " for columna2 in fila2) + "|")
        print("   +" + "---+" * DIMENSION + "     +" + "---+" * DIMENSION)

def turnos_ataque(fila, columna, dic1, dic2): #DIC2 ES EL DICCIONARIO DEL JUGADOR CONTRARIO
    tablero_vista = dic1["tablero oponente"]
    tablero_contrario = dic2["mi tablero"]
    if tablero_contrario[fila][columna] == " ":
        tablero_contrario[fila][columna] = "O"
        tablero_vista[fila][columna] = "O"
    elif tablero_contrario[fila][columna] == "B":
        tablero_contrario[fila][columna] = "X"
        tablero_vista[fila][columna] = "X"

def comprobar_ganador(dic):
    tablero = dic["mi tablero"]
    ganar = True
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if tablero[i][j] == "B":
                ganar = False
                break
    return ganar

def jugar(): #Función principal
    print("------------------------------")
    print("|        BATALLA NAVAL       |")
    print("------------------------------")

    tablero_1 = generar_tablero()
    tablero_2 = generar_tablero()
 
    barcos_jugador1 = [(1, 4), (1, 5), (1, 6), (1, 7), (3, 2), (4, 2), (5, 2), (7, 1), (7, 2)]
    barcos_jugador2 = [(0, 1), (0, 2), (0, 3), (0, 4), (2, 5), (2, 6), (4, 7), (4, 8), (4, 9)]

    agregar_barcos(barcos_jugador1, tablero_1)
    agregar_barcos(barcos_jugador2, tablero_2)

    jugador1 = generar_diccionario(tablero_1)
    jugador2 = generar_diccionario(tablero_2)

    turno = choice(["Jugador 1", "Jugador 2"])
    jugadas = 0
    gana = False

    while not gana:
        print(f"\n{turno}")

        if turno == "Jugador 1":
            jugador_actual = jugador1
            jugador_oponente = jugador2
        else:
            jugador_actual = jugador2
            jugador_oponente = jugador1

        imprimir(jugador_actual)
        fila, columna = input("Introduzca la posición: ").split(",")
        fila  = int(fila)
        columna = int(columna)
        turnos_ataque(fila, columna, jugador_actual, jugador_oponente)

        if gana:
            print(f'Ha ganado {turno}')
            break
        
        #SE CAMBIA DE TURNO SI GANA ES FALSO
        if turno == "Jugador 1":
            turno = "Jugador 2"
        else:
            turno = "Jugador 1"
        jugadas += 1

if __name__ == "__main__":
    jugar()