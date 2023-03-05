import json
import re
class ExercicioD:
    # Pasta | Data | Nome | Pai | Mãe | Observações
    def writeFile(self, file):
        dicFile = dict()
        dicFile["Processos"] = []
        numberLine = 1
        for line in file:
            if numberLine > 20:
                break
            else:
                expRegex = re.findall(r"[0-9a-zA-Z\s\-\.\,]*\:\:", line)
                dicLine = dict()
                parametros = []
                for item in expRegex:
                    param = item[:-2]
                    parametros.append(param)
                dicLine["Pasta"] = parametros[0]
                dicLine["Data"] = parametros[1]
                dicLine["Nome"] = parametros[2]
                dicLine["Pai"] = parametros[3]
                dicLine["Mae"] = parametros[4]
                dicLine["Observacoes"] = parametros[5]
                dicFile["Processos"].append(dicLine)
                numberLine += 1
        jsonString = json.dumps(dicFile)
        jsonFile = open("data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
