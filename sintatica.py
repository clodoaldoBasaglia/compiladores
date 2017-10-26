import ply.yacc as yacc
from lex import token


class Tree:
    def __init__(self, type_node, child=[], value=None):
        self.type = type_node
        self.child = child
        self.value = value

    def __str__(self, level=0):
        ret = "| " * level + repr(self.type) + "\n"
        for child in self.child:
            ret += child.__str__(level + 1)
        return ret


precedence = (('left', 'SOMA', 'SUB'), ('left', 'MULT', 'DIVISAO'))


def p_programa_1(p):
    'programa : principal'
    p[0] = Tree('programa_principal', [p[1]])


def p_programa_2(p):
    'programa : func_loop principal'
    p[0] = Tree('programa_funcao'.[p[1], p[2]])


def p_programa_3(p):
    'programa : declara_var programa'
    p[0] = Tree('programa_varglobal', [p[1], p[2]])
