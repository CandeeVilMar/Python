import random
from time import sleep

MIN_CARTON = 100
MAX_CARTON = 200
NUM_PEQUENIO = 1
NUM_MAXIMO = 90
TACHADO = 'X'
NUMERO_BOLAS_CARTON = 15
INTERVALO = 0.8
ANCHURA = 5
ALTURA = 3

def generar_numeros_serie(cantidad): #FUNCIÓN LLAMADA EN LA FUNCIÓN DE GENERAR CARTONES
    lista_ordenada = []
    for i in range(cantidad):
        lista_ordenada.append(random.randint(MIN_CARTON, MAX_CARTON))
    sorted(lista_ordenada)
    return lista_ordenada

def generar_lista(): #GENERA LA LISTA DE LOS NÚMEROS ENTRE 1 Y 90
    numeros = [int(i) for i in range(NUM_PEQUENIO, NUM_MAXIMO + 1)]
    return numeros

def generar_numeros_cartones():
    numeros = generar_lista()
    numeros_carton = random.sample(numeros, NUMERO_BOLAS_CARTON)
    numeros_carton.sort()
    matriz = []
    indice = 0
    for x in range(ALTURA):
        fila = []
        for y in range(ANCHURA):
            fila.append(numeros_carton[indice])
            indice += 1
        matriz.append(fila)
    
    return matriz

def generar_cartones(cantidad):
    cartones = [] #LISTA DONDE SE VA AGUARDAR LOS DICCIONARIOS
    serie = generar_numeros_serie(cantidad)
    for i in range(cantidad):
        carton = {}
        carton["Serie"] = serie[i]
        carton["Numeros"] = generar_numeros_cartones()
        cartones.append(carton)
    return cartones

def imprimir(cartones):
    for carton in cartones:
        print(f"Serie: {carton['Serie']}")
        print("----------------")
        for fila in carton['Numeros']:
            print(" ".join(f"{num:2}" for num in fila))
        print()

def generar_bombo():
    bombo = generar_lista()
    random.shuffle(bombo)
    return bombo

def sacar_bola(bombo):
    bola = bombo.pop(0)
    return bola

def tachado(cartones, bola):
    for carton in cartones:
        num_carton = carton.get('Numeros')
        
        for c in range(ANCHURA):
            for f in range(ALTURA):
                if (num_carton[f][c] == bola):
                    num_carton[f][c] = TACHADO
                    break
    return cartones

def comprobar_linea(cartones):
    linea = False
    serie = None
    for carton in cartones:
        serie = carton["Serie"]
        num_carton = carton["Numeros"]
        for fila in num_carton:
            todos_tachados = True
            for num in fila:
                if num != TACHADO:
                    todos_tachados = False
                    break
            if todos_tachados:
                linea = True
                break
        if linea:
            break
    return linea, serie


def comprobar_bingo(cartones):
    bingo = False
    serie = None
    for carton in cartones:
        serie = carton["Serie"]
        num_carton = carton["Numeros"]
        bingo = True
        for fila in num_carton:
            for num in fila:
                if num != TACHADO:
                    bingo = False
                    break
            if not bingo:
                break
        if bingo:
            break
    return bingo, serie


def jugar():
    cantidad = int(input("Introduzca el número de jugadores: "))
    cartones = generar_cartones(cantidad)
    bombo = generar_bombo()
    bolas = []
    bingo = False
    linea_cantada = False

    while True:
        bola = sacar_bola(bombo)
        bolas.append(bola)
        print("Bolas jugadas:",str(bolas).replace("[", "").replace("]", ""))
        print()
        cartones = tachado(cartones, bola)
        imprimir(cartones)
        
        if not linea_cantada:
            linea, serie = comprobar_linea(cartones)
            if linea:
                linea_cantada = True
                print("Línea! Cartón Serie:", serie)
                print()
        
        bingo, serie = comprobar_bingo(cartones)
        if bingo:
            print("Bingo! Cartón Serie: ",serie)
            break

        sleep(INTERVALO)


if __name__ == "__main__":
    jugar()

