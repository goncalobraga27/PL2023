from ply.lex import lex
from ply.yacc import yacc
import re

# Lista que irá ter o resultado do analisador léxico
resultado = []
# Função que põe os tokens na lista de resultados
def adicionaResultado(t, erro):
    resultado.append((t.lineno, t.lexpos, t.type, t.value, erro))
# Dicionário que contém todas as palavras reservadas da nossa gramática
reserved = {
    "iComML": "op_iComML",
    "fComML": "op_fComML",
    "nCom":  "op_nCom",
    "funcao": "function",
    "while": "while",
    "program": "program",
    "for": "for",
    "print": "print",
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
    # Operadores que detetam uma variavel, numero, ‘string’ mal formados
    'variavel_mf',
    'numero_mf',
    'string_mf'
]+list(reserved.values())
# Regex para tokens mais simples
# Operadores dos comentários
t_op_iComML = r'\/\*'
t_op_fComML = r'\*\\'
t_op_nCom = r'\/\/'
# Operadores Matemáticos
t_op_mais = r'\+'
t_op_menos = r'\-'
t_op_vezes = r'\*'
t_op_dividir = r'\/'
t_op_igual = r'\='

t_op_igualIgual = r'\=='
t_op_maior = r'\>'
t_op_menor = r'\<'
t_op_maiorIgual = r'\>='
t_op_menorIgual = r'\<='
t_op_diferente = r'\!='

t_op_abreChaveta = r'\{'
t_op_fechaChaveta = r'\}'
t_op_abreLista = r'\['
t_op_fechaLista = r'\]'
t_op_abreParentesis = r'\('
t_op_fechaParentesis = r'\)'
t_op_doisPontoFinal = r'\.\.'

t_op_doisPontos = r'\:'
t_op_pontoVirgula = r'\;'
t_op_virgula = r'\,'
t_op_ponto = r'\.'

t_ignore = r' \t'


# Regex para tokens mais complexos

def t_string(t):
    r'"[^("|\n)]*"'
    return adicionaResultado(t, f"Nenhum")
def t_string_mf(t):
    r'"[^("|\n?)]*'
    return adicionaResultado(t, f"String encontra-se mal formada")
def t_variavel_mf(t):
    r'([0-9]+[a-z]+)|([@!#$%&*]+[a-z]+)'
    return adicionaResultado(t, f"Variavel encontra-se mal formada")
def t_numero_mf(t):
    r'([0-9]+\.\D*[0-9]*)|([0-9]+\.\D+)'
    return adicionaResultado(t, f"Número encontra-se mal formado")
def t_inteiro(t):
    r'\d+'
    max = (len(t.value))
    if max > 15:
        return adicionaResultado(t, f"Tamanho maior que o suportado")
        t.value = 0
    else:
        t.value = int(t.value)
        return adicionaResultado(t, f"Nenhum")
def t_double(t):
    r'(\d*\.\d+)|(\d+\.\d*)'
    t.value = float(t.value)
    return adicionaResultado(t, f"Nenhum")
def t_variavel(t):
    r'[a-z][a-z_0-9]*'
    max = (len(t.value))
    if max < 20:
        if t.value in reserved:
            t.type = reserved[t.value]
            return  adicionaResultado(t, f"Palavra Reservada")
        else:
            return adicionaResultado(t, f"Nenhum")
    else:
        return adicionaResultado(t, f"Tamanho da variavel maior que o suportado")
def t_new_line(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_error(t):
    return resultado.append((t.lineno, t.lexpos, f'Inválido', t.value, f'Caractere não reconhecido   por esta linguagem'))
    t.lexer.skip(1)

lexer = lex()

