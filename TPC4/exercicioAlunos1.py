import re
import json
class alunos1:

    def leituraFicheiro(self):
        file = open("alunos.csv", "r")
        return file
    def writeFile(self, file):
        listFile = []
        k = 0
        listaParametros = []
        for line in file:
            if k == 0:
                expRegex = re.findall(r"[0-9a-zA-Z\s\:\{\}\ú]+", line)
                for item in expRegex:
                    if item[-1] == "\n":
                        listaParametros.append(item[:-1])
                    else:
                        listaParametros.append(item)
                k = k+1
            else:
                dicLine = dict()
                expRegexLine = re.findall(r"[0-9a-zA-Z\s\:\{\}\ú\ê\í\â]+", line)
                for i in range(0, 3):
                    if expRegexLine[i][-1] == "\n":
                        dicLine[listaParametros[i]] = expRegexLine[i][:-1]
                    else:
                        dicLine[listaParametros[i]] = expRegexLine[i]
                listFile.append(dicLine)
                k = k+1
        jsonString = json.dumps(listFile)
        jsonFile = open("alunos.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()



