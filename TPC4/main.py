from exercicioAlunos1 import alunos1
from exercicioAlunos2e3 import alunos2e3

def main():
    ex1 = alunos1()
    ex2e3 = alunos2e3()

    file1 = ex1.leituraFicheiro()
    ex1.writeFile(file1)
    file2e3 = ex2e3.leituraFicheiro()
    ex2e3.writeFile(file2e3)

if __name__ == "__main__":
    main()