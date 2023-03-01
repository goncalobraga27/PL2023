import re
class ExercicioC:
    def calculaFreqGrauParentesco(self, file):
        dic = dict()
        for line in file:
            expRegex = re.findall(r'\,[A-Z]{1}[a-zA-Z\s]*\.\sP', line)
            if expRegex:
                for elem in expRegex:
                    grauParentescoAux = elem[:-3]
                    grauParentesco = grauParentescoAux[1:]
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


