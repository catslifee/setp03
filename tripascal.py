def Tri_pascal(n):
    if n == 0:
        return 1
    else:
        fila = [ ]
        for auxiliar in range(n+1):
            if auxiliar == 0 or auxiliar == n :
                fila = fila + [1]
            else:
                fila = fila + [ Tri_pascal(n-1)[auxiliar-1] + Tri_pascal(n-1)[auxiliar]]
    return fila
