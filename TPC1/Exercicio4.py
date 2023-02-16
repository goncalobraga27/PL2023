class Exercicio4:
    def __init__(self):
        self.resultado=dict() # O resultado vai ser desta forma: FaixaEtária:Valor de Incidência
    def idadeMax (self, dict):
        idadeMax = 0
        for k in dict.keys():
            if ((dict[k])["idade"]) > idadeMax:
                idadeMax = ((dict[k])["idade"])
        return idadeMax
    
    def calcula_Distribuicao_FaixaEtaria(self, dict):
        idadeMaxima = self.idadeMax(dict)
        listaIndices=[] # Esta lista contêm as divisões que foram feitas nos escalões etários
        indL=0
        for i in range(0, idadeMaxima, 5):
            chave = str(i)+"-"+str(i+4)
            listaIndices.insert(indL,chave)
            indL+=1
            self.resultado[chave] = 0
        for k in dict.keys():
            position = int(((dict[k])["idade"])/5)
            valorDic = self.resultado[listaIndices[position]]
            valorDic += 1
            self.resultado[listaIndices[position]] = valorDic
        return self.resultado

