def calcular_constante_magica(matriz):
    constante_magica = sum(matriz[0])
    return constante_magica

def generar_matriz(dimension, lista):
    cuadrado = []
    for i in range(dimension):
        fila = []
        for j in range(dimension):
            num = lista[i * dimension + j]
            fila.append(num)
        cuadrado.append(fila)

def calcular_esquinas(matriz):
    n = len(matriz)
    suma_esquinas = matriz[0][0] + matriz[0][n - 1] + matriz[n - 1][0] + matriz[n - 1][n - 1]
    return suma_esquinas

def calcular_fila(matriz, indice):
    return sum(matriz[indice])

def calcular_columna(matriz, indice):
    suma_columna = 0
    for i in range(len(matriz)):
        suma_columna += matriz[i][indice]
    return suma_columna

def calcular_diagonales(matriz, constante_magica):
    diagonal_principal = sum(matriz[i][i] for i in range(len(matriz)))
    diagonal_secundaria = sum(matriz[i][len(matriz) - 1 - i] for i in range(len(matriz)))
    return (diagonal_principal == constante_magica) and (diagonal_secundaria == constante_magica)

def calcular_casillas_medias(matriz):
    n = len(matriz)
    mitad = 0
    if n % 2 != 0: #IMPAR
        mitad += matriz[n // 2][0]
        mitad += matriz[0][n // 2]
        mitad += matriz[n // 2][n - 1]
        mitad += matriz[n - 1][n // 2]
    else: #PAR
        mitad += matriz[n // 2][n // 2]
        mitad += matriz[n // 2 - 1][n // 2]
        mitad += matriz[n // 2][n // 2 - 1]
        mitad += matriz[n // 2 - 1][n // 2 - 1]
    return mitad

def comprueba_diabolico(matriz, constante_magica):
    diabolico = True
    for i in range(len(matriz)):
            if calcular_fila(matriz, i) != constante_magica:
                diabolico = False
                break
            if calcular_columna(matriz, i) != constante_magica:
                diabolico = False
    return diabolico

def comprobar_esoterico(matriz, constante_magica_2):
    longitud = len(matriz[0])
    esoterico = True

    if calcular_esquinas(matriz) != constante_magica_2:
        esoterico = False
            
        mitad = calcular_casillas_medias(matriz)
            
        if longitud % 2 != 0:
            if mitad != constante_magica_2:
                esoterico = False
        elif longitud % 2 == 0:
            if mitad != constante_magica_2:
                esoterico = False
                    
        if longitud % 2 != 0 and esoterico:
            if matriz[longitud // 2][longitud // 2] * 4 != constante_magica_2:
                esoterico = False
        elif esoterico:
            centro = 0
            centro += matriz[longitud // 2][longitud // 2]
            centro += matriz[longitud // 2][longitud // 2 - 1]
            centro += matriz[longitud // 2 - 1][longitud // 2]
            centro += matriz[longitud // 2 - 1][longitud // 2 - 1]
            if centro != constante_magica_2:
                esoterico = False
                
    return esoterico

def jugar():
    dimension = -1
    while dimension != 0:
        if dimension == 0:
            break
        
        dimension = int(input())
        numeros = input().split()
        
        cuadrado = generar_matriz(dimension, numeros)
    
        constante_magica = calcular_constante_magica(cuadrado)
        constante_magica_2 = (constante_magica * 4) / dimension
        esoterico = False
        
        diabolico = comprueba_diabolico(cuadrado, constante_magica)
        #SI ES DIABÓILICO LLAMA A COMRPOBAR ESOTÉRICO
        if diabolico:
            esoterico = comprobar_esoterico(cuadrado, constante_magica_2)
                            
        #COMPRUEBA YA PARA DAR EL RESULTADO
        if diabolico and esoterico:
            print("ESOTÉRICO")
        elif diabolico:
            print("DIABÓLICO")
        else:
            print("NO")

if __name__ == "__main__":
    jugar()
