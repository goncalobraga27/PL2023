import re
import json
class alunos2e3:
    def leituraFicheiro(self):
        file = open("alunos3.csv", "r")
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
                    if item[-1] != "\n" and item != "":
                        listaParametros.append(item)
                k = k+1
            else:
                dicLine = dict()
                expRegexLine = re.findall(r"[0-9a-zA-Z\s\:\{\}\ú\ê\í\â]+", line)
                for i in range(0, 4):
                    if expRegexLine[i][-1] == "\n":
                        dicLine[listaParametros[i]] = expRegexLine[i][:-1]
                    elif i == 3:
                        notas = []
                        for k in range(3, len(expRegexLine)):
                            if expRegexLine[k][-1] == "\n":
                                if (expRegexLine[k][:-1]) != '':
                                    notas.append(int(expRegexLine[k][:-1]))
                            else:
                                notas.append(int(expRegexLine[k]))

                        dicLine["Notas"] = notas
                    else:
                        dicLine[listaParametros[i]] = expRegexLine[i]
                listFile.append(dicLine)
                k = k + 1
        jsonString = json.dumps(listFile, ensure_ascii=False)
        jsonFile = open("alunos2e3.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

