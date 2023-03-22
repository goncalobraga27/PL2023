import re
class cabine:
    def calculaSaldo(self, moedas, moedasValidas):
        saldo = 0.0
        valida = 0
        expRegex = re.search(r"(\d+(c|e)\,|\d+(c|e))+", moedas)
        moedasLidas = expRegex.group().split(",")
        for moeda in moedasLidas:
            for moedaPadrao in moedasValidas:
                if moeda == moedaPadrao:
                    valida = 1
                    if moeda == "1c":
                        saldo += 0.01
                    elif moeda == "2c":
                        saldo += 0.02
                    elif moeda == "5c":
                        saldo += 0.05
                    elif moeda == "10c":
                        saldo += 0.10
                    elif moeda == "20c":
                        saldo += 0.20
                    elif moeda == "50c":
                        saldo += 0.50
                    elif moeda == "1e":
                        saldo += 1.0
                    elif moeda == "2e":
                        saldo += 2.0
            if valida == 0:
                return (moeda+"-> Moeda inválida", 0, 0)
            else:
                valida = 0
        return ("Saldo acrescentado = "+str(saldo)+" euros", 1, saldo)
    def validaNumero(self, saldo, numeroTelemovel):
        expRegex = re.search(r"\d+", numeroTelemovel)
        numero = expRegex.group()
        first3Numbers = numero[0:3]
        first2Numbers = numero[0:2]
        firstNumber = numero[0]
        if first3Numbers == "601" or first3Numbers == "641":
            return "CHAMADA BLOQUEADA", saldo, 1
        if first2Numbers == "00" and saldo >= 1.5:
            return "CHAMADA EFETUADA", saldo - 1.5, 1
        if firstNumber == "00" and saldo >= 0.25:
            return "CHAMADA EFETUADA", saldo - 0.25, 1
        if first3Numbers == "800":
            return "CHAMADA EFETUADA", saldo, 1
        if first3Numbers == "808" and saldo >= 0.10:
            return "CHAMADA EFETUADA", saldo-0.10, 1
        return "CHAMADA CANCELADA POR SALDO INSUFICIENTE", saldo, 0
    def maquinaEstados(self):
        estadoTelefone = 0 # 0 -> Não está a ser utilizado | 1 -> Caso Contrário
        moedasValidas = ["1c", "2c", "5c", "10c", "20c", "50c", "1e", "2e"]
        saldoTotal = 0.0
        while True:
            if estadoTelefone == 0:
                estadoLevantar = input()
                if estadoLevantar == "LEVANTAR":
                    estadoTelefone = 1
                    print("Introduza moedas.")
                    moedasRecebidas = input()
                    if moedasRecebidas == "ABORTAR":
                        print("Devolvidos: " + str(saldoTotal) + "euros;Volte Sempre!")
                        break
                    msg, estado, saldo = self.calculaSaldo(moedasRecebidas, moedasValidas)
                    saldoTotal += saldo
                    if estado == 0:
                        print("Saldo= "+str(saldoTotal))
                        print("OPERAÇÃO CANCELADA")
                        break
                    else:
                        print("Saldo= " + str(saldoTotal))
                        numeroTelefone = input()
                        while numeroTelefone != 'POUSAR' and numeroTelefone != 'ABORTAR':
                            msg, saldo, numeroValido = self.validaNumero(saldoTotal, numeroTelefone)
                            saldoTotal = saldo
                            while numeroValido != 1:
                                print("Introduza moedas.")
                                moedasRecebidas = input()
                                if moedasRecebidas == "ABORTAR":
                                    print("Devolvidos: " + str(saldoTotal) + "euros;Volte Sempre!")
                                    break
                                msg, estado, saldo = self.calculaSaldo(moedasRecebidas, moedasValidas)
                                saldoTotal += saldo
                                if estado == 0:
                                    print("Saldo= " + str(saldoTotal))
                                    print("OPERAÇÃO CANCELADA")
                                    break
                                else:
                                    print("Saldo= " + str(saldoTotal))
                                    numeroTelefone = input()
                                    if numeroTelefone == "ABORTAR":
                                        print("Devolvidos: " + str(saldoTotal) + "euros;Volte Sempre!")
                                        break
                                    msg, saldo, numeroValido = self.validaNumero(saldoTotal, numeroTelefone)
                                    saldoTotal = saldo
                            print(msg + " Saldo= " + str(saldoTotal))
                            numeroTelefone = input()
                        if numeroTelefone == "POUSAR":
                            print("Troco: " + str(saldoTotal) + ";Volte Sempre!")
                            break
                        elif numeroTelefone == "ABORTAR":
                            print("Devolvidos: " + str(saldoTotal) + "euros;Volte Sempre!")
                            break
                elif estadoLevantar == "ABORTAR":
                    print("Devolvidos: " + str(saldoTotal) + "euros;Volte Sempre!")
                    break

