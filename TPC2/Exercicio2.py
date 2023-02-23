class Exercicio2:

    def readTerminal(self):
        str = input("Insira os dados:")
        numberList = []
        lastChar = ""
        size = len(str)
        i = 1
        for c in str:
            if lastChar == "":
                if c == "0" or c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or c == "6" or c == "7" or c == "8" or c == "9":
                    lastChar += c
            else:
                if (c == "0" or c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or c == "6" or c == "7" or c == "8" or c == "9") and (lastChar[-1] == "0" or lastChar[-1] == "1" or lastChar[-1] == "2" or lastChar[-1] == "3" or lastChar[-1] == "4" or lastChar[-1] == "5" or lastChar[-1] == "6" or lastChar[-1] == "7" or lastChar[-1] == "8" or lastChar[-1] == "9"):
                    if i == size:
                        lastChar += c
                        numberList.append(int(lastChar))
                    else:
                        lastChar += c
                if (c != "0" and c != "1" and c != "2" and c != "3" and c != "4" and c != "5" and c != "6" and c != "7" and c != "8" and c != "9") and (lastChar[-1] == "0" or lastChar[-1] == "1" or lastChar[-1] == "2" or lastChar[-1] == "3" or lastChar[-1] == "4" or lastChar[-1] == "5" or lastChar[-1] == "6" or lastChar[-1] == "7" or lastChar[-1] == "8" or lastChar[-1] == "9"):
                    numberList.append(int(lastChar))
                    lastChar = ""
            i += 1
        print(numberList)
        resultado = 0
        for number in numberList:
            resultado += number

        return resultado