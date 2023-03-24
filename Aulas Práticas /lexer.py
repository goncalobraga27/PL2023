from ply.lex import lex
from ply.yacc import yacc
import re

tokens = ('IGUAL', 'ID', 'NUM', 'MENOS', 'MAIS', 'VARIAVEL', 'VEZES', 'DIVIDIR', 'VEZESIGUAL', 'STOP')

t_ignore = ' \t'
t_IGUAL = r'\='
t_ID = r'[a-zA-Z0-9]+'
t_MENOS = r'\-'
t_MAIS = r'\+'
t_VEZES = r'\*'
t_DIVIDIR = r'\/'
t_VEZESIGUAL = r'\*\='
t_STOP = r'STOP'


def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')


def t_VARIAVEL(t):
    r'[a-zA-Z0-9]+'
    t.value = t.value
    return t


def t_error(t):
    print(f'Illegal character {t.value[0]!r} - Na posição {t.lexpos!r}')
    t.lexer.skip(1)


lexer = lex()

while True:
    i = input(">")
    lexer.input(i)
    for tok in lexer:
        print(tok.value)
        print(tok)
