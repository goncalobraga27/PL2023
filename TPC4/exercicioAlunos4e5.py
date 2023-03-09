import re
import json
class alunos4e5:
    def leituraFicheiro(self):
        file = open("alunos5.csv", "r")
        return file
    def writeFile(self, file):
        listFile = []
        k = 0
        listaParametros = []
        for line in file:
            if k == 0:
                expRegex = re.findall(r"[a-zA-Z\s\:\ú]+", line)
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
                        expRegexLista1 = re.findall(r"\:\:sum$", listaParametros[4])
                        expRegexLista2 = re.findall(r"\:\:media$", listaParametros[4])
                        if len(expRegexLista1) != 0:
                            if expRegexLista1[0][2:] == "sum":
                                notas = []
                                for k in range(3, len(expRegexLine)):
                                    if expRegexLine[k][-1] == "\n":
                                        if (expRegexLine[k][:-1]) != '':
                                            notas.append(int(expRegexLine[k][:-1]))
                                    else:
                                        notas.append(int(expRegexLine[k]))
                                resultado = 0
                                for item in notas:
                                    resultado += item
                            dicLine["Notas"] = resultado
                        if len(expRegexLista2) != 0:
                            if expRegexLista2[0][2:] == "media":
                                notas = []
                                for k in range(3, len(expRegexLine)):
                                    if expRegexLine[k][-1] == "\n":
                                        if (expRegexLine[k][:-1]) != '':
                                            notas.append(int(expRegexLine[k][:-1]))
                                    else:
                                        notas.append(int(expRegexLine[k]))
                                somatorio = 0
                                for item in notas:
                                    somatorio += item
                            dicLine["Notas"] = somatorio / len(notas)
                    else:
                        dicLine[listaParametros[i]] = expRegexLine[i]
                listFile.append(dicLine)
                k = k + 1
        jsonString = json.dumps(listFile, ensure_ascii=False)
        jsonFile = open("alunos4e5.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

