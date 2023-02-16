from TPC1.Exercicio1e2 import Exercicio1e2
from TPC1.Exercicio3 import Exercicio3
from TPC1.Exercicio4 import Exercicio4
from TPC1.Exercicio5 import Exercicio5
from TPC1.Exercicio6 import Exercicio6
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
        print(table)
    if (int(op)==1):
        dictDataSet = geracaoModelo.geraModelo()
        resultado_Dist_Etaria= idade.calcula_Distribuicao_FaixaEtaria(dictDataSet)
        table = "Faixa Etária->Casos incidentes\n" + tabela.makeTable(resultado_Dist_Etaria)
        print(table)
    if (int(op)==2):
        dictDataSet = geracaoModelo.geraModelo()
        resultado_Dist_Colestrol=colestrol.calcula_Distribuicao_Colestrol(dictDataSet)
        table ="Valores Colestrol->Casos incidentes\n"+tabela.makeTable(resultado_Dist_Colestrol)
        print(table)


if __name__ == "__main__":
        main()