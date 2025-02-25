from random import choice

PALABRAS = ["casa", "perro", "gato", "cielo", "árbol", "niño", "agua", "fuego",
    "tierra", "viento", "sol", "luna", "estrella", "camino", "mar",
    "montaña", "flor", "río", "libro", "amigo", "música", "nube",
    "pájaro", "ciudad", "jardín", "planta", "arena", "roca", "lago",
    "bosque", "fuego", "noche", "día", "verde", "azul", "rojo", "amarillo",
    "blanco", "negro", "gris"]

palabra_secreta = choice(PALABRAS)

def palabra_juego():
    lista = ["-" for i in range(len(palabra_secreta))]
    return lista

def imprimir(lista):
    for letra in lista:
        print(letra, end=" ")
    print()

def comprobar_letra(letra, lista):
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            lista[i] = letra

def comprobar_palabra(letra):
    bandera = False
    if letra == palabra_secreta:
        bandera = True
    return bandera

def jugar(): #Función principal

    print("-------------------------")
    print("|        AHORCADO       |")
    print("-------------------------")
    print()

    palabra_progreso = palabra_juego()
    intentos = 0
    turno = choice(["Jugador 1", "Jugador 2"])

    while True:
        
        print(turno)
        letra = input("Ingresa una letra o una palabra a adivinar: ")
        intentos += 1
        
        if len(letra) == 1:
            comprobar_letra(letra, palabra_progreso)
            print(f'Intento {intentos}: ' , end="")
            imprimir(palabra_progreso)

        palabra_jugada = "".join(palabra_progreso)
        

        if (palabra_secreta == palabra_jugada) or (letra == palabra_secreta):
            print(f'Ha ganado el {turno} en : {intentos}')
            break
        else:
            if turno == "Jugador 1":
                turno = "Jugador 2"
            else:
                turno = "Jugador 1"

if __name__ == "__main__":
    jugar()
