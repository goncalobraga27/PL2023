class Exercicio3:
    def On_Off_equal(self):
        file = open("text.txt")
        numberList = []
        leituraAtivada = 0
        lastChar = ""
        on = ""
        off = ""
        for line in file:
            size = len(line)
            i = 1
            for c in line:
                if leituraAtivada == 0:
                    if (c == "o" or c == "O") and on == "":
                        on += c
                        i += 1
                    elif (c == "n" or c == "N") and (on == "o" or on == "O"):
                        on += c
                        i += 1
                        leituraAtivada = 1
                        off = ""
                    else:
                        on = ""
                        off = ""
                        i += 1
                else:
                    if c == "=":
                        resultado = 0
                        for number in numberList:
                            resultado += number
                        return resultado
                    elif c == "o" or c == "O" or c == "f" or c == "F":
                        if (c == "o" or c == "O") and off == "":
                            off += c
                            i += 1
                        if (c == "f" or c == "F") and (off == "o" or off == "O"):
                            off += c
                            i += 1
                        if (c == "F" or c == "f") and (off == "of" or off == "OF" or off == "Of" or off == "oF"):
                            off += c
                            i += 1
                            leituraAtivada = 0
                            on = ""
                    else:
                        on = ""
                        off = ""
                        if lastChar == "":
                            if c == "0" or c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or c == "6" or c == "7" or c == "8" or c == "9":
                                lastChar += c
                        else:
                            if (
                                    c == "0" or c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or c == "6" or c == "7" or c == "8" or c == "9") and (
                                    lastChar[-1] == "0" or lastChar[-1] == "1" or lastChar[-1] == "2" or lastChar[
                                -1] == "3" or lastChar[-1] == "4" or lastChar[-1] == "5" or lastChar[-1] == "6" or
                                    lastChar[-1] == "7" or lastChar[-1] == "8" or lastChar[-1] == "9"):
                                if i == size:
                                    lastChar += c
                                    numberList.append(int(lastChar))
                                else:
                                    lastChar += c
                            if (
                                    c != "0" and c != "1" and c != "2" and c != "3" and c != "4" and c != "5" and c != "6" and c != "7" and c != "8" and c != "9") and (
                                    lastChar[-1] == "0" or lastChar[-1] == "1" or lastChar[-1] == "2" or lastChar[
                                -1] == "3" or lastChar[-1] == "4" or lastChar[-1] == "5" or lastChar[-1] == "6" or
                                    lastChar[-1] == "7" or lastChar[-1] == "8" or lastChar[-1] == "9"):
                                numberList.append(int(lastChar))
                                lastChar = ""
                        i += 1
