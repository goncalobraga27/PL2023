from Exercicio1e2 import Exercicio1e2
from Exercicio3 import Exercicio3
from Exercicio4 import Exercicio4
from Exercicio5 import Exercicio5
from Exercicio6 import Exercicio6
from matplotlib import pyplot as plt
def main():
    geracaoModelo = Exercicio1e2()
    calculaDistribuicao = Exercicio3()
    idade= Exercicio4()
    colestrol=Exercicio5()
    tabela= Exercicio6()

    print("1-Cálculo da incidência pela faixa etária")
    print("2-Cálculo da incidência pelos valores do colestrol")
    print("3-Cálculo da incidência por sexo")
    op = input('Insira uma opção:')
    if(int(op)==3):
        dictDataSet = geracaoModelo.geraModelo()
        resultadoDist = calculaDistribuicao.calculaDist(dictDataSet)
        table = "Sexo-> Casos incidentes\n"+"Masculino->"+str(resultadoDist[0])+"\n"+"Feminino->"+str(resultadoDist[1])+"\n"
        table1 = "Sexo-> Sem Casos incidentes\n"+"Masculino->"+str(resultadoDist[2])+"\n"+"Feminino->"+str(resultadoDist[3])+"\n"
        print(table+table1)

        x_values = ["Masculino c/Doença", "Feminino c/Doença", "Masculino s/Doença", "Feminino s/Doença"]
        y_values = [resultadoDist[0], resultadoDist[1],resultadoDist[2],resultadoDist[3]]
        plt.plot(x_values, y_values)
        plt.show()
    if (int(op)==1):
        dictDataSet = geracaoModelo.geraModelo()
        resultado_Dist_Etaria= idade.calcula_Distribuicao_FaixaEtaria(dictDataSet)
        table = "Faixa Etária->Casos incidentes\n" + tabela.makeTable(resultado_Dist_Etaria)
        print(table)
        x_values = resultado_Dist_Etaria.keys()
        y_values = []
        for k in resultado_Dist_Etaria.keys():
            y_values.append(resultado_Dist_Etaria[k])
        plt.plot(x_values, y_values)
        plt.show()
    if (int(op)==2):
        dictDataSet = geracaoModelo.geraModelo()
        resultado_Dist_Colestrol=colestrol.calcula_Distribuicao_Colestrol(dictDataSet)
        table ="Valores Colestrol->Casos incidentes\n"+tabela.makeTable(resultado_Dist_Colestrol)
        print(table)
        x_values = resultado_Dist_Colestrol.keys()
        y_values = []
        for k in resultado_Dist_Colestrol.keys():
            y_values.append(resultado_Dist_Colestrol[k])
        plt.plot(x_values, y_values)
        plt.show()


if __name__ == "__main__":
        main()