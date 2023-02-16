class Exercicio6:

    def makeTable(self,dict):
        resultado=""
        for k in dict.keys():
            resultado += k
            resultado +="->"
            resultado +=str(dict[k])+"\n"
        return  resultado