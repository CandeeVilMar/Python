#IMPORTO DE RANDOM LAS DOS FUNCIONES QUE NECESITO UTILIZAR
from random import sample
from random import choice

#CONSTANTES
TURNOS = ("jugador 1", "jugador 2")
FICHAS = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6),
          (2,2), (2,3), (2,4), (2,5), (2,6), (3,3), (3,4), (3,5), (3,6), (4,4), (4,5), (4,6), (5,5), (5,6), (6,6)]

#ELIGE LA PRIMERA FICHA Y LUEGO LA BIRRA DE FICHAS
primera_ficha = choice(FICHAS)
FICHAS.remove(primera_ficha)

def reparto_fichas(): #ESTA FUNCIÓN DEVUELVE UNA LISTA DE TUPLAS 
    fichas_jugador = sample(FICHAS, 7)
    for i in fichas_jugador:
        FICHAS.remove(i)
    return fichas_jugador

def imprimir(lista): #ESTA FUNCIÓN IMPRIME EN EL FORMATO INDICADO LAS FICHAS
    for i in lista:
        num1, num2 = i
        print(f'[{num1}|{num2}] ', end="")
    print()
    
def comprobar_insertado(linea, lista_turno): #SI RETORNA FALSO LLAMA A LA FUNCIÓN DE ROBAR FICHA, SINO A LA ADE AÑADIR
    puede = False #Asumo que es falso
    x1, y1 = linea[0]
    x2, y2 = linea[-1]
    ficha = (0,0)
    for i in lista_turno:
        x, y = i
        if (x == x1) or (y == x1) or (x == y2) or (y == y2):
           puede = True
           lista_turno.remove(i)
           break
    if puede:
        ficha = i
    return puede, ficha
    
def aniade_ficha_linea(linea, ficha):
    x1, y1 = linea[0]
    x2, y2 = linea[-1]
    x, y = ficha
    
    #PRIMERO COMPRUEBO SI LA AÑADO EN LA POSICIÓN 0
    if x == x1: #Si la x es igual a la coordenada x1, primero intercambio posiciones y luego la añado
        ficha = y,x
        linea.insert(0, ficha)
    elif y == x1: #Añado directamente
        linea.insert(0, ficha)
    #AQUI SE COMPRUEBA PARA AÑADIR AL FINAL DE LA LISTA
    elif x == y2:
            linea.append(ficha)
    elif y == y2: #Si la y es igual a la coordenada x1, primero intercambio posiciones y luego la añado
        ficha = y,x
        linea.append(ficha)
        
def roba_ficha(): #ESTA FUNCIÓN DEVUELVE UNA FICHA ROBADA DEL MONTÓN
    ficha = choice(FICHAS)
    FICHAS.remove(ficha)
    return ficha

def comrpobar_ganador(turno1, turno2): #SI EL MONTÓN SE QUEDA SIN FICHAS, ESTA FUNCIÓN COMPRUEBA QUIEN ES EL POSIBLE GANADOR
    suma1, suma2 = 0, 0
    if len(turno1) < len(turno2):
        ganador = "Jugador 1"
    elif len(turno1) > len(turno2):
        ganador = "Jugador 2"
    else: #SI TIENEN LA MISMA LONGITUD DESEMPATA POR SUMA
        for jug1, jug2 in zip(turno1, turno2):
            x1, y1 = jug1
            x2, y2 = jug2
            suma1 += x1 + y1
            suma2 += x2 + y2
        if suma1 < suma2:
            ganador = "Jugador 1"
        elif suma1 > suma2:
            ganador = "Jugador 2"
        else:
            ganador = "Empate"
            
    return ganador
    
def jugar(): #FUNCIÓN PRINCIPAL
    turno = choice(TURNOS)
    jugador1 = reparto_fichas()
    jugador2 = reparto_fichas()
    linea = []
    linea.append(primera_ficha)
    
    while True:

        #COMPRUEBO EL TURNO PARA A LA VARIABLE TURNO_ACTUAL DARLE EL VALOR DE LA LISTA DE LAS FICHAS QUE TIENE CADA JUGADOR
        if turno == "jugador 1": 
            turno_actual = jugador1
        else:
            turno_actual = jugador2
        
        print("Linea: ", end="")
        imprimir(linea)
        print("Fichas restantes: ", end="")
        imprimir(FICHAS)
        print(f'Turno del {turno}: ')
        imprimir(turno_actual)
        print()
        
        #LLAMO A LA FUNCION DE COMPROBAR INSERTADO PARA SABER SI PUEDO AÑADIR O NO FICHA
        aniadir, ficha = comprobar_insertado(linea, turno_actual)
        
        if aniadir:
            aniade_ficha_linea(linea, ficha)
        else:
            print("No hay movimientos válidos. Robando ficha...")
            ficha = roba_ficha()
            num1, num2 = ficha
            turno_actual.append(ficha)
            print(f'{turno} roba una ficha: [{num1}|{num2}]')
            aniade, ficha = comprobar_insertado(linea, turno_actual)
            if aniade:
                print("La ficha robada se puede jugar")
                aniade_ficha_linea(linea, ficha)
            else:
                print("La ficha robada no se puede jugar")
            print()
                
        #COMPROBAR LAS CONDICIONES POR SI LAS CUMPLE SALIR DEL BUCLE
        if len(FICHAS) == 0:
            print("El juego está bloqueado. ¡No hay más fichas restantes!")
            ganador = comrpobar_ganador(jugador1, jugador2)
            print(f'Ha ganado el {ganador}')
            break
        if len(jugador1) == 0 or len(jugador2) == 0:
            if len(jugador1) == 0:
                print("¡Ha ganado el Jugador 1!")
                break
            else:
                print("¡Ha ganado el Jugador 2!")
                break
        
        #CAMBIO DE TURNOS
        if turno == "jugador 1":
            turno = "jugador 2"
        else:
            turno = "jugador 1"
            
    #ESTÁ FUERA DEL BUCLRE PORQUE O GANE EL JUGADOR1, JUGADOR2 O EL MONTÓN SE QUEDE SIN CARTAS, SE IMPRIME LA LINEA, JUGADOR1 Y JUGADOR2       
    print("Linea: ", end="")
    imprimir(linea)
    print("Fichas Jugador 1: ", end="")
    imprimir(jugador1)
    print("Fichas Jugador 2: ", end="")
    imprimir(jugador2)

if __name__ == "__main__":
    jugar()