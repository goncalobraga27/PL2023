from ExercicioA import ExercicioA
from ExercicioB import ExercicioB
from ExercicioC import ExercicioC
from ExercicioD import ExercicioD
def main():
     exA = ExercicioA()
     exB = ExercicioB()
     exC = ExercicioC()
     exD = ExercicioD()
     # A alínea A pede para determinarmos quantos processos existem por ano (primeiro elemento da data);
     fileA = exA.leituraFicheiro()
     dicionaryA = exA.calculoFreq(fileA)
     resultadoA = exA.imprimeResultado(dicionaryA)
     print(resultadoA)
     # A alínea B pede para calcular a frequência  de nomes próprios e apelidos por séculos e apresentar os 5 mais usados
     fileB1 = exA.leituraFicheiro()
     dicAux = exB.calculaFrequenciaSeculos(fileB1)
     fileB2 = exA.leituraFicheiro()
     dicResB = exB.calculaFrequenciaNomes_Apelidos(dicAux, fileB2)
     resultadoB = exB.calculaResultadoNomes(dicResB)
     print(resultadoB)
     # A alínea C pede para calcular a frequência dos vários tipos de relação: irmão, sobrinho, etc.;
     fileC1 = exA.leituraFicheiro()
     dicResC = exC.calculaFreqGrauParentesco(fileC1)
     resultadoC = exC.imprimeFrequenciaParentesco(dicResC)
     print(resultadoC)
     # A alínea D pede para converter os 20 primeiros registos num novo ficheiro de output mas em formato Json.
     fileD1 = exA.leituraFicheiro()
     exD.writeFile(fileD1)




if __name__ == "__main__":
    main()