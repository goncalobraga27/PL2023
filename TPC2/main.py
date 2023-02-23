from Exercicio1 import Exercicio1
from Exercicio2 import Exercicio2
from Exercicio3 import Exercicio3
def main():
        ex1 = Exercicio1()
        ex2 = Exercicio2()
        ex3 = Exercicio3()

        resultadoExercicio1 = ex1.readFicheiro()
        print(resultadoExercicio1)
        resultadoExercicio2 = ex2.readTerminal()
        print(resultadoExercicio2)
        resultadoExercicio3 = ex3.On_Off_equal()
        print(f"O resultado da pergunta 3 é "+str(resultadoExercicio3))
if __name__ == "__main__":
        main()