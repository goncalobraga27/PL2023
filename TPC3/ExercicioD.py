import json
import re
class ExercicioD:
    def writeFile(self, file):
        dicFile = dict()
        dicFile["Processos"] = []
        numberLine = 1
        for line in file:
            if numberLine > 20:
                break
            else:
                dicLine = dict()
                dicLine["id"] = str(numberLine)
                dicLine["linha"] = line
                dicFile["Processos"].append(dicLine)
                numberLine += 1
        jsonString = json.dumps(dicFile)
        jsonFile = open("data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
