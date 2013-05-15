def cuenta_palabras(dicc):
    
    
    if(len(dicc)>0):
        palabra, frecuencia = dicc.popitem()
        total = total + frecuencia
        return cuenta_palabras(dicc) + int(total)
    else:
        return (0)