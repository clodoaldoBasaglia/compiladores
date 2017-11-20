# -*- coding: utf-8 -*-

import ply.yacc as yacc
import sys
# import Lexica from Lexica
from lexicanum import tokens


class Tree:
    def __init__(self, type_node, child=[], value=''):
        self.type = type_node
        self.child = child
        self.value = value

    def __str__(self):
        return self.type


########################
# Analisador Sintático #
########################


precedence = (
    ('left', 'IGUAL', 'NEGACAO', 'MENOR_IGUAL', 'MAIOR', 'MAIOR_IGUAL', 'MENOR'),
    ('left', 'SOMA', 'SUBTRACAO'),
    ('left', 'MULTIPLICACAO', 'DIVISAO'))
tokens = tokens


def p_programa(p):
    '''
    programa : lista_declaracoes
                 '''
    p[0] = Tree('programa', [p[1]])


def p_lista_declaracoes(p):
    '''
    lista_declaracoes : lista_declaracoes declaracao
                       | declaracao
    '''
    if (len(p) == 3):
        p[0] = Tree('lista_declaracoes', [p[1], p[2]])
    elif (len(p) == 2):
        p[0] = Tree('lista_declaracoes', [p[1]])


def p_declaracao(p):
    '''
    declaracao : declaracao_variaveis
                | inicializacao_variaveis
                | declaracao_funcao
    '''
    p[0] = Tree('declaracao', [p[1]])


def p_declaracao_variaveis(p):
    '''
    declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis
    '''
    p[0] = Tree('declaracao_variaveis', [p[1], p[3]], p[2])


def p_inicializacao_variaveis(p):
    '''
    inicializacao_variaveis : atribuicao
    '''
    p[0] = Tree('inicializacao_variaveis', [p[1]])


def p_lista_variaveis(p):
    '''
    lista_variaveis : lista_variaveis VIRGULA var
                    | var
    '''
    if (len(p) == 4):
        p[0] = Tree('lista_variaveis', [p[1], p[3]])
    elif (len(p) == 2):
        p[0] = Tree('lista_variaveis', [p[1]])


def p_var(p):
    '''
    var : IDENTIFICADOR
        | IDENTIFICADOR indice
    '''
    if (len(p) == 2):
        p[0] = Tree('var', [], p[1])
    elif (len(p) == 3):
        p[0] = Tree('var', [p[2]], p[1])


def p_indice(p):
    '''
    indice : indice ABRE_COLXETE expressao FECHA_COLXETE
            | ABRE_COLXETE expressao FECHA_COLXETE
    '''
    if (len(p) == 5):
        p[0] = Tree('indice', [p[1], p[3]])
    elif (len(p) == 4):
        p[0] = Tree('indice', [p[2]])


def p_tipo(p):
    '''
    tipo : INTEIRO
    '''
    p[0] = Tree('inteiro', [])


def p_tipo2(p):
    '''
    tipo : FLUTUANTE
    '''
    p[0] = Tree('flutuante', [])


def p_declaracao_funcao(p):
    '''
    declaracao_funcao : tipo cabecalho
                    | cabecalho
    '''
    if len(p) == 3:
        p[0] = Tree('declaracao_funcao', [p[1], p[2]])
    elif len(p) == 2:
        p[0] = Tree('declaracao_funcao', [p[1]])


def p_cabecalho(p):
    '''
    cabecalho : IDENTIFICADOR ABRE_PARENTESES lista_parametros FECHA_PARENTESES corpo FIM
    '''
    p[0] = Tree('cabecalho', [p[3], p[5]], p[1])


def p_lista_parametros(p):
    '''
    lista_parametros : lista_parametros VIRGULA lista_parametros
                        | parametro
                        | vazio
    '''
    if len(p) == 4:
        p[0] = Tree('lista_parametros', [p[1], p[3]])
    elif len(p) == 2:
        p[0] = Tree('lista_parametros', [p[1]])


def p_parametro1(p):
    '''
    parametro : tipo DOIS_PONTOS IDENTIFICADOR
    '''
    p[0] = Tree('parametro', [p[1]], p[3])


def p_parametro2(p):
    '''
    parametro : parametro ABRE_COLXETE FECHA_COLXETE
    '''
    p[0] = Tree('parametro', [p[1]])


def p_corpo(p):
    '''
    corpo : corpo acao
            | vazio
    '''
    if len(p) == 3:
        p[0] = Tree('corpo', [p[1], p[2]])
    elif len(p) == 2:
        p[0] = Tree('corpo', [p[1]])


def p_acao(p):
    '''
    acao : expressao
                | declaracao_variaveis
                | se
                | repita
                | leia
                | escreva
                | retorna
                | error

    '''
    p[0] = Tree('acao', [p[1]])


def p_se(p):
    '''
        se : SE expressao ENTAO corpo FIM
            | SE expressao ENTAO corpo SENAO corpo FIM
    '''
    if len(p) == 6:
        p[0] = Tree('se', [p[2], p[4]])
    elif len(p) == 8:
        p[0] = Tree('se', [p[2], p[4], p[6]])


def p_repita(p):
    '''
        repita : REPITA corpo ATE expressao
    '''
    p[0] = Tree('repita', [p[2], p[4]])


def p_atribuicao(p):
    '''
        atribuicao : var ATRIBUICAO expressao
    '''
    if len(p):
        p[0] = Tree('atribuicao', [p[1], p[3]])


def p_leia(p):
    '''
        leia : LEIA ABRE_PARENTESES IDENTIFICADOR FECHA_PARENTESES
    '''
    if len(p):
        p[0] = Tree('leia', [], p[3])


def p_escreva(p):
    '''
        escreva : ESCREVA ABRE_PARENTESES expressao FECHA_PARENTESES
    '''
    p[0] = Tree('escreva', [p[3]])


def p_retorna(p):
    '''
        retorna : RETORNA ABRE_PARENTESES expressao FECHA_PARENTESES
    '''
    p[0] = Tree('retorna', [p[3]])


def p_expressao(p):
    '''
        expressao : expressao_simples
                    | atribuicao
    '''
    p[0] = Tree('expressao', [p[1]])


def p_expressao_simples(p):
    '''
        expressao_simples : expressao_aditiva
                            | expressao_simples operador_relacional expressao_aditiva
    '''
    if len(p) == 2:
        p[0] = Tree('expressao_simples', [p[1]])
    elif len(p) == 4:
        p[0] = Tree('expressao_simples', [p[1], p[2], p[3]])


def p_expressao_aditiva(p):
    '''
        expressao_aditiva : expressao_multiplicativa
                            | expressao_aditiva operador_multiplicacao expressao_unaria
    '''
    if len(p) == 2:
        p[0] = Tree('expressao_aditiva', [p[1]])
    elif len(p) == 4:
        p[0] = Tree('expressao_aditiva', [p[1], p[2], p[3]])


def p_expressao_multiplicativa(p):
    '''
       expressao_multiplicativa : expressao_unaria
                       | expressao_multiplicativa operador_multiplicacao expressao_unaria

    '''
    if len(p) == 2:
        p[0] = Tree('expressao_multiplicativa', [p[1]])
    elif len(p) == 4:
        p[0] = Tree('expressao_multiplicativa', [p[1], p[2], p[3]])


def p_expressao_unaria(p):
    '''

        expressao_unaria : fator
                        | operador_soma fator

    '''
    if len(p) == 2:
        p[0] = Tree('expressao_unaria', [p[1]])
    else:
        p[0] = Tree('expressao_unaria', [p[1], p[2]])


def p_operador_relacional(p):
    '''
        operador_relacional : MENOR
                            | MAIOR
                            | IGUAL
                            | MENOR_IGUAL
                            | MAIOR_IGUAL
                            | NEGACAO
    '''
    p[0] = Tree('operador_relacional', [])


def p_operador_soma(p):
    '''
        operador_soma : SOMA
                | SUBTRACAO
    '''
    p[0] = Tree('operador_soma', [])


def p_operador_multiplicacao(p):
    '''
        operador_multiplicacao : MULTIPLICACAO
                                | DIVISAO
    '''
    p[0] = Tree('operador_multiplicacao', [])


def p_fator(p):
    '''
        fator : ABRE_COLXETE  expressao FECHA_COLXETE
                | var
                | chamada_funcao
                | numero
    '''
    if len(p) == 4:
        p[0] = Tree('fator', [p[2]])
    else:
        p[0] = Tree('fator', [p[1]])


def p_numero(p):
    '''
        numero : INTEIRO
                | FLUTUANTE
    '''
    p[0] = Tree('numero', [])


def p_chamada_funcao(p):
    '''
        chamada_funcao : IDENTIFICADOR ABRE_PARENTESES lista_argumentos FECHA_PARENTESES
    '''
    p[0] = Tree('chamada_funcao', [p[3]], p[1])


def p_lista_argumentos(p):
    '''
        lista_argumentos : lista_argumentos VIRGULA expressao
                        | expressao
                        | vazio
    '''
    if len(p) == 4:
        p[0] = Tree('lista_argumentos', [p[1], p[3]])
    else:
        p[0] = Tree('lista_argumentos', [p[1]])


def p_vazio(p):
    '''
        vazio :
    '''


def p_error(p):
    if p:
        print(p)
        print("Erro sintático: '%s', linha %d" % (p.value, p.lineno))
        exit(1)
    else:
        yacc.restart()
        print('Erro sintático: definições incompletas!')
        exit(1)


def printar(self):
    self.g.view()


def mostra_tree(node, w, i):
    if node != None:
        value1 = node.type + str(i)
        i = i + 1
        for son in node.child:
            w.edge(value1, str(son) + str(i))
            mostra_tree(son, w, i)


if __name__ == '__main__':
    import sys, io

    parser = yacc.yacc(debug=True)
    lista = io.open("saida.txt", mode="r", encoding="utf-8")
    # print(lista.read())
    print(parser.parse(lista.read()))  # parser = Parser(lista.read())
