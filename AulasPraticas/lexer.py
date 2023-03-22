from ply.lex import lex
from ply.yacc import yacc
import re
# Definição dos tokens que são admissíveis
tokens = ('PLUS', 'MINUS', 'TIMES', 'NAME', 'NUMBER', 'TIMESEQUAL')
# Definição dos tokens que são para ignorar
t_ignore = '\t'
# Definição das regex para capturar os tokens admissíveis
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_NAME = r'[a-zA-Z]*'
t_TIMESEQUAL = r'\*\='
# Definição da função daquilo que faz quando recebe um número
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
# Definição da função daquilo que faz quando aparece um newline
def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
# Definição da função daquilo que faz quando recebe um token proibido
def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)
# Construção do lexer do objeto
lexer = lex()
