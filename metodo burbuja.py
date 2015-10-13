lista = [5,30,20,10,25,15]
numero = len(lista)
posicion = 0
while (posicion < numero):
    j = posicion
    while (j < numero):
        if(lista[posicion] > lista[j]):
            aux = lista[posicion]
            lista[posicion] = lista[j]
            lista[j] = aux
            print "Proceso del recorrido de la lista ", lista
        j= j+1
    posicion = posicion+1
    print ""
print "Nueva lista ordena:", lista
