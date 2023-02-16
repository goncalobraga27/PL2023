class Exercicio3:
    def calculaDist(self, dict):
        x = 0
        y = 0
        resultado = (x, y) # O PAR REPRESENTA O RESULTADO DA FUNÇÃO DA SEGUINTE FORMA : (Número de doentes do sexo Masculino,Número de doentes do sexo Feminino)
        for key in dict.keys():
            if (((dict[key])["sexo"]) == "M") and (((dict[key])["temDoença"]) == 1):
                x += 1
            if (((dict[key])["sexo"]) == "F") and (((dict[key])["temDoença"]) == 1):
                y += 1
        resultado = (x, y)
        return resultado

