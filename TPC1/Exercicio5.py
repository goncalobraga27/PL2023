class Exercicio5:
    def __init__(self):
        self.resultado = dict()  # O resultado vai ser desta forma: Faixa do Colestrol:Valor de Incidência do colestrol

    def colestrolMax(self, dict):
        colestrolMax = 0
        for k in dict.keys():
            if ((dict[k])["colestrol"]) > colestrolMax:
                colestrolMax = ((dict[k])["colestrol"])
        return colestrolMax

    def calcula_Distribuicao_Colestrol(self, dict):
        colestrolMaximo = self.colestrolMax(dict)
        listaIndices = []  # Esta lista contêm as divisões que foram feitas nos escalões etários
        indL = 0
        for i in range(0, colestrolMaximo, 10):
            chave = str(i) + "-" + str(i + 9)
            listaIndices.insert(indL, chave)
            indL += 1
            self.resultado[chave] = 0
        for k in dict.keys():
            position = int(((dict[k])["colestrol"]) / 10)
            valorDic = self.resultado[listaIndices[position]]
            valorDic += 1
            self.resultado[listaIndices[position]] = valorDic
        return self.resultado

