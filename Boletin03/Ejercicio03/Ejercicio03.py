def codigoCorrecto(codigo):
    cadena = codigo
    esCorrecto = False   
    res = 0


    if (len(cadena) > 13):
        esCorrecto = False
    else:
        while(len(cadena)>0 and len(cadena)<8):
            cadena = "0" + cadena
        
        while (len(cadena)>8 and len(cadena)<13):
            cadena = "0" + cadena

        num = int(cadena)
        # obtenemos el último número para sumarlo al final
        aux = int(num%10)
        # eliminamos el último número para continuar con la comprobación
        num = int(num/10)
        
        for digito in range(1,len(cadena)+1):
            if (digito%2 != 0):
                res += int((num%10)*3)
            else:
                res += int(num%10)
            num = int(num/10)

        if ((res+aux)%10 == 0):
            esCorrecto = True

    return esCorrecto
        


















# numC = "6583952"
# nume: int = 6583952
# res: int = 0
# contador = 1

# for num in numC:
#     if contador%2 != 0:
#         res+=int((nume%10)*3)
#     else:
#         res+=int(nume%10)
#     contador+=1
#     nume = int(nume/10)

# print(res)
# print(res+1)