class Exercicio1e2:

    def __init__(self):
        #Dicionário que modela o dataSet fornecido
        self.dictGeral = dict()    # TIPO DO DICIONÁRIO => chave:{"idade":valor,"sexo":valor,"tensão":valor,"colestrol":valor,"batimento":valor,"temDoença":valor}

    def geraModelo(self):
        identifier = 0
        file = open("myheart.csv") #LEITURA DO FICHEIRO myheart.csv
        listaParametros = []
        for line in file:
            #Dicionário mais particular de cada linha
            dictParticular = dict()
            listaParametros = line.split(',')
            if (identifier!=0):
                dictParticular["idade"]=int(listaParametros[0])
                dictParticular["sexo"]=listaParametros[1]
                dictParticular["tensão"]=int(listaParametros[2])                   #PREENCHIMENTO DO MODELO EM MEMÓRIA
                dictParticular["colestrol"]=int(listaParametros[3])
                dictParticular["batimento"]=int(listaParametros[4])
                dictParticular["temDoença"]=int(listaParametros[5])
                self.dictGeral[identifier]=dictParticular
            identifier += 1
        return self.dictGeral

