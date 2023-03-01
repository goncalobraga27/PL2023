from ExercicioA import ExercicioA
from ExercicioB import ExercicioB
def main():
     exA = ExercicioA()
     exB = ExercicioB()
     # A alínea A pede para determinarmos quantos processos existem por ano (primeiro elemento da data);
     fileA = exA.leituraFicheiro()
     dicionaryA = exA.calculoFreq(fileA)
     print(dicionaryA)
     # A alínea B pede para calcular a frequência  de nomes próprios e apelidos por séculos e apresentar os 5 mais usados
     fileB1 = exA.leituraFicheiro()
     dicAux = exB.calculaFrequenciaSeculos(fileB1)
     fileB2 = exA.leituraFicheiro()
     dicRes = exB.calculaFrequenciaNomes_Apelidos(dicAux, fileB2)



if __name__ == "__main__":
    main()