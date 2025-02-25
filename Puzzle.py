import random

DIMENSION = 3

def generar_tablero_objetivo():
    matriz = []
    contador = 1
    for _ in range(DIMENSION):
        fila = []
        for _ in range(DIMENSION):
            if contador == (DIMENSION ** 2):
                fila.append(" ")
            else:
                fila.append(contador)
                contador += 1
        matriz.append(fila)
    return matriz

def generar_tablero_juego(): #refactorizar generando una lista de nxn con range haciendo un shuffle
    lista = list(range(1, DIMENSION * DIMENSION + 1))
    random.shuffle(lista)
    matriz = []
    contador = 0
    for _ in range(DIMENSION):
        fila = []
        for _ in range(DIMENSION):
            if lista[contador] == (DIMENSION ** 2):
                fila.append(" ")
            else:
                fila.append(lista[contador])
            contador += 1
        matriz.append(fila)
    return matriz

def imprime(matriz):
    for fila in matriz:
        print(("+------" * DIMENSION) + "+")
        print(("|      " * DIMENSION) + "|")
        for columna in fila:
            print(f'|  {columna : >2}  ', end="")
        print("|")
        print(("|      " * DIMENSION) + "|")
    print(("+------" * DIMENSION) + "+")

def buscar_posicion(matriz, valor): #Esta función es llamada en la función de movimientos para buscar el espacio en blanco
    fila = -1
    columna = -1
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if matriz[i][j] == valor:
                fila, columna = i, j
    return fila, columna

def movimientos_posibles(tablero_juego):  # Este método es llamado en imprimir movimientos para saber las posibles opciones
    fila, columna = buscar_posicion(tablero_juego, " ")
    arriba = '' #Arriba
    izq = '' #Izquierda
    abajo = '' #Abajo
    der = '' #Derecha
    
    if fila == DIMENSION - 1:
        arriba = ' '
    else:
        arriba = 'w'
        
    if fila == 0:
        abajo = ' '
    else:
        abajo = 's'
        
    if columna == 0:
        der = ' '
    else:
        der = 'd'
        
    if columna == DIMENSION - 1:
        izq = ' '
    else:
        izq = 'a'
        
    return arriba, izq, abajo, der


def realizar_movimientos(matriz_juego, opcion):  #Esta función realiza el moviiento que el usuario haya elegido en las opciones
    #w--> arriba, a --> izq, d --> der, s --> abajo
    fila, columna = buscar_posicion(matriz_juego, " ")

    if opcion == "w" and fila >= 0:  #ARRIBA
        matriz_juego[fila][columna], matriz_juego[fila + 1][columna] = matriz_juego[fila + 1][columna], matriz_juego[fila][columna]
    elif opcion == "d" and columna > 0:  #derecha
        matriz_juego[fila][columna], matriz_juego[fila][columna - 1] = matriz_juego[fila][columna - 1], matriz_juego[fila][columna]
    elif opcion == "s" and fila <= DIMENSION - 1:  #ABAJO
        matriz_juego[fila][columna], matriz_juego[fila - 1][columna] = matriz_juego[fila - 1][columna], matriz_juego[fila][columna]
    elif opcion == "a" and columna < DIMENSION - 1:  #izquierda
        matriz_juego[fila][columna], matriz_juego[fila][columna + 1] = matriz_juego[fila][columna + 1], matriz_juego[fila][columna]

def distancia_hamming(m_objetivo, m_juego):
    contador = 0
    for i in range(len(m_objetivo)):
        for j in range(len(m_objetivo[0])):
            if m_objetivo[i][j] != m_juego[i][j]:
                contador += 1
    return contador

def juego():
    print("----------------------")
    print("- PUZZLE DESLIZANTE -")
    print("-----------------------")
    print()
    tablero_objetivo = generar_tablero_objetivo()
    tablero_juego = generar_tablero_juego()
    print("Tablero Objetivo")
    print("-------------------")
    imprime(tablero_objetivo)
    print("-------------------------")
    print("Pulse intro para empezar el juego")
    input()
    print("Tablero del Juego")
    imprime(tablero_juego)
    jugadas = 0
    opcion = ""
    while((tablero_juego != tablero_objetivo) or(opcion != "QUIT")):
        if (tablero_juego == tablero_objetivo):
            print("Lo has logrado en: ", jugadas, " intentos")
            break
        elif(opcion == "QUIT"):
            print("Has elegido salir del juego")
            break
        
        arriba, izq, abajo, der = movimientos_posibles(tablero_juego)
        print("Introduzca w,a,s,d o (QUIT) para terminar")
        print("     (", arriba, ")")
        print("(", izq, ") (", abajo, ") (", der, ")") 
        opcion = input()
        realizar_movimientos(tablero_juego, opcion)
        jugadas += 1
        imprime(tablero_juego)

if __name__ == "__main__":
    juego()
    
