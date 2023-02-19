class Exercicio3:
    def calculaDist(self, dict):
        x = 0
        y = 0
        z = 0
        w = 0
        resultado = (x, y, z, w) # O PAR REPRESENTA O RESULTADO DA FUNÇÃO DA SEGUINTE FORMA : (Número de doentes do sexo Masculino,Número de doentes do sexo Feminino,Número de pessoas s/doença do sexo Masculino,Número de pessoas s/doença do sexo Feminino)
        for key in dict.keys():
            if (((dict[key])["sexo"]) == "M") and (((dict[key])["temDoença"]) == 1):
                x += 1
            if (((dict[key])["sexo"]) == "F") and (((dict[key])["temDoença"]) == 1):
                y += 1
            if (((dict[key])["sexo"]) == "M") and (((dict[key])["temDoença"]) == 0):
                z += 1
            if (((dict[key])["sexo"]) == "F") and (((dict[key])["temDoença"]) == 0):
                w += 1
        resultado = (x, y, z, w)
        return resultado

