def contarRecorrido(secuencia: str):
    res = 0
    arraySecuencia = secuencia.split()
    try:
        for num in range(0, len(arraySecuencia)):
            arraySecuencia[num] = int(arraySecuencia[num])
    except:
        return "No se pueden convertir caracteres no numericos al tipo int"


    lastNum = arraySecuencia[0]

    if (len(arraySecuencia) == 1):
        res = 1
    else:
        for num in arraySecuencia:
            if lastNum <= num:
                res += num - lastNum
            else:
                res += lastNum - num
            lastNum = num
        
    return res
