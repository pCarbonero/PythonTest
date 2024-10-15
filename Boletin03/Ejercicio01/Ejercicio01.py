abcdario = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def encriptacion(cadena, clave):
    resul = ""

    for caracter in cadena:
        if caracter == " ":
            resul += " "
        else:
            pos = abcdario.index(caracter)
            resul += abcdario[(pos+clave)%len(abcdario)]
        
    return resul