import re
class ExercicioC:
    def calculaFreqGrauParentesco(self, file):
        dic = dict()
        for line in file:
            expRegex = re.findall(r'[a-z],([A-Z][a-zA-Z\s]*?)\.( ?P|:)', line)
            if expRegex:
                for elem in expRegex:
                    grauParentesco = elem[0]
                    if grauParentesco not in dic:
                        dic[grauParentesco] = 1
                    else :
                        dic[grauParentesco] += 1
        return dic
    def imprimeFrequenciaParentesco(self, dic):
        resultado = "----Tabela de Parentesco----\n"
        for key in dic:
            resultado += str(key) + " -> " + str(dic[key]) + "\n"
        return  resultado


