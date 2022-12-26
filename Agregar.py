class Agregar:
    def __init__(self):
        pass

    def Agregar(self, lista):
        qe = lista.count("")
        cont = 0
        s = 0 #Percorrendo os elementos da lista para modificar
        while qe > 0:
            if cont == 0:
                indB = lista.index("")
                ui = 0
                lista[ui:indB] = ['\n'.join(lista[ui:indB])]
                x = lista.index("")
                lista.remove(lista[lista.index("")])
                qe -= 1
                s += 1
                cont += 1
            if cont > 0:
                indB = lista.index("")
                lista[s:indB] = ['\n'.join(lista[s:indB])]
                lista.remove(lista[lista.index("")])
                qe -= 1
                s += 1
        return lista
"""
#listaTeste = ["1 Elemento","2 Elemento","3 Elemento","4 Elemento","5 Elemento","6 Elemento","7 Elemento","8 Elemento","9elemento"," "]
listaTeste = ["0","1","2"," ","3"," ","4","5","6"," ","7","8","9"," ",]
#print(Agregar.Agregador(Agregar,listaTeste))
print(Agregar.Agregar(Agregar, listaTeste))
"""
