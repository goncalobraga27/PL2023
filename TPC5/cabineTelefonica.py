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
                return (moeda+"-> Moeda inválida", 0)
            else:
                valida = 0
        return ("Saldo = "+str(saldo)+" euros", 1)


    def maquinaEstados(self):
        estadoTelefone =0 # 0 -> Não está a ser utilizado | 1 -> Caso Contrário
        moedasValidas = ["1c", "2c", "5c", "10c", "20c", "50c", "1e", "2e"]
        while True:
            if estadoTelefone == 0:
                estadoLevantar = input()
                if estadoLevantar == "LEVANTAR":
                    estadoTelefone = 1
                    print("Introduza moedas.")
                    moedasRecebidas = input()
                    msg, estado = self.calculaSaldo(moedasRecebidas, moedasValidas)
                    if estado == 0:
                        print(msg)
                        print("OPERAÇÃO CANCELADA")
                        break
                    else:
                        print(msg)
                        numeroTelefone = input()

