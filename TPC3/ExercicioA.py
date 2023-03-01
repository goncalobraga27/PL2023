import re
class ExercicioA:
    def leituraFicheiro(self):
        file = open("processos.txt", "r")
        return file
    def calculoFreq(self, file):
        dic = dict()
        for line in file:
            expRegex = re.search(r'\:\:[0-9]{4}\-', line)
            if expRegex:
                exp = expRegex.group()
                number = exp[2:6]
                if number in dic:
                    dic[number] += 1
                else:
                    dic[number] = 1
        return dic
    def imprimeResultado(self, dic):
        resultado = ""
        for key in dic:
            resultado += "------Ano:"+str(key)+"------\n"
            resultado += str(dic[key])+"\n"
        return resultado