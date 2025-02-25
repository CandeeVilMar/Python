import random
import os
import time

#CONSTANTES
NUMEROS = ("AS", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
PALOS = ("CORAZONES", "DIAMANTES", "PICAS", "TREBOL")
MOVIMIENTOS = ("IZQUIERDA", "MEDIO", "DERECHA")
REINA = (NUMEROS[11],PALOS[0])
NUMERO_INTERCAMBIO = 20
DELAY = 0.5

def generar_cartas():
    jugada = []

    carta1 = REINA
    jugada.append(carta1)

    contador = 0
    while contador != 2:
        if contador == 2:
            break
        carta = (random.choice(NUMEROS), random.choice(PALOS))
        if carta not in jugada:
            jugada.append(carta)
            contador += 1

    return jugada

def posiciones():
    posicion1 = random.choice(MOVIMIENTOS)
    posicion2 = random.choice(MOVIMIENTOS)
    while posicion1 == posicion2:
        posicion2 = random.choice(MOVIMIENTOS)
        if posicion1 != posicion2:
            break
    return posicion1, posicion2

def imprime_intercambio(pos1, pos2):
        print(f'Intercambiando {pos1} y {pos2}')

def intercambios(lista):

    posicion1, posicion2 = posiciones()

    if (posicion1 == "IZQUIERDA" and posicion2 == "DERECHA"):
        lista[0], lista[2] = lista[2], lista[0]
    elif (posicion1 == "DERECHA" and posicion2 == "IZQUIERDA"):
        lista[2], lista[0] = lista[0], lista[2]
    elif (posicion1 == "MEDIO" and posicion2 == "IZQUIERDA"):
        lista[1], lista[0] = lista[0], lista[1]
    elif (posicion1 == "IZQUIERDA" and posicion2 == "MEDIO"):
        lista[0], lista[1] = lista[1], lista[0]
    elif (posicion1 == "MEDIO" and posicion2 == "DERECHA"):
        lista[1], lista[2] = lista[2], lista[1]
    elif (posicion1 == "DERECHA" and posicion2 == "MEDIO"):
        lista[2], lista[1] = lista[1], lista[2]

    return posicion1, posicion2

def ganador(opcion, mano1):
    gana = False
    if (opcion == "IZQUIERDA" and mano1[0] == REINA) or (opcion == "MEDIO" and mano1[1] == REINA) or (opcion == "DERECHA" and mano1[2] == REINA):
        gana = True
    
    return gana

def juego():
    #En esta función llamo a las demás funciones. Esta es la función principal
    print("----------------------")
    print("Monte de Tres Cartas")
    print("----------------------")

    print("¡Encuentra la dama roja (La reina de corazones)!")
    print("Presta atención en como se mueven las cartas.")
    print("Aquí están las cartas:")

    mano = generar_cartas()
    print(mano)
    
    print(f'Pulsa "enter" cuando estés preparado para empezar...')
    press = input()

    for i in range(NUMERO_INTERCAMBIO):
            posicion1, posicion2 = intercambios(mano)
            imprime_intercambio(posicion1, posicion2)
            time.sleep(DELAY)
    os.system("clear") #cls en windows 
    
   
    reina_corazones_posicion = input("¿Qué carta tiene la reina de Corazones? (IZQUIERDA, MEDIO, DERECHA): ")
    reina_corazones_posicion = reina_corazones_posicion.upper()

    print(mano)
    
    if ganador(reina_corazones_posicion, mano):
        print("Has ganado")
    else:
        print("Has perdido")

    print("¡Gracias por jugar!")


if __name__ == "__main__":
    juego()
    

