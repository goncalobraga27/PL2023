from ply.lex import lex
from ply.yacc import yacc
import re
inComentario = 0
inComentarioS = 0
# Dicionário que contém todas as palavras reservadas da nossa gramática
reserved = {
    "iComML": "op_iComML",
    "fComML": "op_fComML",
    "nCom":  "op_nCom",
    "funcao": "op_function",
    "while": "op_while",
    "program": "op_program",
    "for": "op_for",
    "print": "op_print",
    "int": "int",
    "double": "double",
    "float": "float",
    "string": "string",
}
# Lista que contém os tokens existentes na gramática a ser definida

tokens = [
    # Operadores Matemáticos
    'op_mais',  # +
    'op_menos',  # -
    'op_vezes',  # *
    'op_dividir',  # /
    'op_igual',  # =
    # Operadores Matemáticos de Comparação
    'op_igualIgual',  # ==
    'op_maior',  # >
    'op_menor',  # <
    'op_maiorIgual',  # >=
    'op_menorIgual',  # <=
    'op_diferente',  # !=
    # Operadores de Chavetas, Listas e Parêntesis
    'op_abreChaveta',  # }
    'op_fechaChaveta',  # {
    'op_abreLista',  # [
    'op_fechaLista',  # ]
    'op_abreParentesis',  # )
    'op_fechaParentesis',  # (
    'op_doisPontoFinal',  # ..
    # Operadores de execução
    'op_doisPontos',  # :
    'op_pontoVirgula',  # ;
    'op_virgula',  # ,
    'op_ponto',  # .
    # Operadores de tipos e atribuição
    'variavel',  # variavel (Ex: res)
    'array',  # array (Ex: a[5])
    # Operadores para ignorar no input recebido
    'ignore',  # \s\t
    'newline'
]+list(reserved.values())
# Regex para tokens mais simples
# Operadores dos comentários
t_op_iComML = r"\/\*"
t_op_fComML = r"\*\/"
t_op_nCom = r"//"
# Operadores de funções
t_op_function = r"function"
t_op_while = r"while"
t_op_program = r"program"
t_op_for = r"for"
t_op_print = r"print"
# Operadores Matemáticos
t_op_mais = r"\+"
t_op_menos = r"-"
t_op_vezes = r"\*"
t_op_dividir = r"/"
t_op_igual = r"="

t_op_igualIgual = r"=="
t_op_maior = r">"
t_op_menor = r"<"
t_op_maiorIgual = r">="
t_op_menorIgual = r"<="
t_op_diferente = r"!="

t_op_abreChaveta = r"{"
t_op_fechaChaveta = r"}"
t_op_abreLista = r"\["
t_op_fechaLista = r"\]"
t_op_abreParentesis = r"\("
t_op_fechaParentesis = r"\)"
t_op_doisPontoFinal = r"\.\."

t_op_doisPontos = r":"
t_op_pontoVirgula = r";"
t_op_virgula = r","
t_op_ponto = r"."

t_ignore = ' \t'


# Regex para tokens mais complexos
def t_newline(t):
    r"""\\n"""
    t.lexer.lineno += t.value.count('\n')
    return t
def t_string(t):
    r'[a-zA-Z]+'
    t.value = t.value
    return t
def t_inteiro(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_double(t):
    r'(\d*\.\d+)|(\d+\.\d*)'
    t.value = float(t.value)
    return t
def t_VARIAVEL(t):
    r'[a-zA-Z0-9]+'
    t.value = t.value
    return t

def t_error(t):
    print(f'Illegal character {t.value[0]!r} - Na posição {t.lexpos!r}')
    t.lexer.skip(1)

lexer = lex()

while True:
    i = input("")
    lexer.input(i)
    for tok in lexer:
        if tok.value == '/*':
            inComentario = 1
            print(tok.value)
            print(tok)
        elif tok.value == '*/':
            inComentario = 0
            print(tok.value)
            print(tok)
        elif tok.value == '//':
            inComentarioS = 1
            print(tok.value)
            print(tok)
        elif tok.value == '\\n' and inComentarioS == 1:
            inComentarioS = 0
        else:
            if inComentario == 1 or inComentarioS == 1:
                pass
            elif tok.value != '\\n':
                print(tok.value)
                print(tok)

