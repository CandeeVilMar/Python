PAISES = {"0": "EEUU", "380": "Bulgaria", "50": "Inglaterra", 
          "539": "Irlanda", "560": "Portugal", "70": "Noruega",
          "759": "Venezuela", "850": "Cuba", "890": "India"}

def calcular_digito_error(cadena):
    cadena_mod = cadena[::-1]
    digito = 0
    cad = [int(i) for i in cadena_mod]
    for i in range(1, len(cad) + 1):
        if i % 2 != 0:
            digito += cad[i-1] * 3
        else:
            digito += cad[i-1]
    return digito

def calcular_digito_comprobacion(cadena):
    digito_error = calcular_digito_error(cadena)
    if digito_error % 10 == 0:
        digito_comprobacion = 0
    else:
        digito_comprobacion = (10 - (digito_error % 10)) % 10
    return digito_comprobacion

def calcular_pais(cadena):
    cod_pais = ""
    pais = ""
    if len(cadena) == 13:
        cod_pais = cadena[:3]
        if cod_pais in PAISES:
            pais = PAISES[cod_pais]
        elif cod_pais[:2] in PAISES:
            pais = PAISES[cod_pais[:2]]
        elif cod_pais[0] in PAISES:
            pais = PAISES[cod_pais[0]]
    else:
        pais = "Desconocido"
    return pais

def principal():
    while True:
        cadena = input().strip()
        if cadena == "0":
            break
        
        longitud = len(cadena)
        
        if longitud < 8:
            cadena = cadena.zfill(8)
        elif longitud < 13:
            cadena = cadena.zfill(13)
        
        digito_correcto = calcular_digito_comprobacion(cadena)
        digito_control = int(cadena[-1])
        
        if digito_correcto == digito_control:
            resultado = "SI"
            if longitud == 13:
                pais = calcular_pais(cadena)
                resultado += f" {pais}"
        else:
            resultado = "NO"
        
        print(resultado)
    
if __name__ == "__main__":
    principal()