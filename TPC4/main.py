from exercicioAlunos1 import alunos1
from exercicioAlunos2e3 import alunos2e3
from exercicioAlunos4e5 import alunos4e5
def main():
    ex1 = alunos1()
    ex2e3 = alunos2e3()
    ex4e5 = alunos4e5()

    file1 = ex1.leituraFicheiro()
    ex1.writeFile(file1)
    file2e3 = ex2e3.leituraFicheiro()
    ex2e3.writeFile(file2e3)
    file4e5 = ex4e5.leituraFicheiro()
    ex4e5.writeFile(file4e5)

if __name__ == "__main__":
    main()