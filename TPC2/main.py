from Exercicio1 import Exercicio1
from Exercicio2 import Exercicio2
def main():
        ex1 = Exercicio1()
        ex2 = Exercicio2()
        resultadoExercicio1 = ex1.readFicheiro()
        print(resultadoExercicio1)
        ex2.readTerminal()
if __name__ == "__main__":
        main()