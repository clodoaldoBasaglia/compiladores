import ply.yacc as yacc
from lexicanum import tokens


class Arvore:
    def __init__(self, type_node, child=[], value=''):
        self.type = type_node
        self.child = child
        self.value = value

    def __str__(self):
        return self.value


class Parser:
    def __init__(self, code):
        self.cont = 0
        self.tokens = tokens
        self.precedence = (
            ('left', 'IGUALDADE', 'NEGACAO', 'MAIOR_IGUAL', 'MAIOR', 'MENOR_IGUAL', 'MENOR'),
            ('left', 'SOMA', 'SUBTRACAO'),
            ('left', 'MULTIPLICACAO', 'DIVISAO'),
        )
        parser = yacc.yacc(debug=False, module=self, optimize=False)
        self.ast = parser.parse(code)

    def p_programa(self,p):
        '''
        programa : lista_declaracoes
        '''
        p[0] = Arvore('programa', [p[1]])

    def p_lista_declaracoes(self,p):
        '''
        lista_declaracoes : lista_declaracoes declaracao
                            | declaracao
        '''
        if (len(p) == 3):
            p[0] = Arvore('lista_declaracoes', [p[1], p[2]])
        elif (len(p) == 2):
            p[0] = Arvore('lista_declaracoes', [p[1]])

    def p_declaraco(self,p):
        '''
        declaracao : declaracao_variaveis
                    | inicializacao_variaveis
                    | declaracao_funcao
        '''
        p[0] = Arvore('declaracao', [p[1]])

    def p_declaracao_variaveis(self,p):
        '''
        declaracao_variaveis : tipo DOISPONTOS lista_variaveis
        '''
        p[0] = Arvore('declaracao_variaveis', [p[1], p[3]], p[2])

    def p_inicializacao_variaveis(self,p):
        '''
        inicializacao_variaveis : atribuicao
        '''
        p[0] = Arvore('inicializacao_variaveis', [p[1]])

    def p_lista_variaveis(self,p):
        '''
        lista_variaveis : lista_variaveis VIRGULA var
                        | var
        '''
        if (len(p) == 4):
            p[0] = Arvore('lista_variaveis', [p[1], p[3]])

        elif (len(p) == 2):
            p[0] = Arvore('lista_variaveis', [p[1]])

    def p_var(self,p):
        '''
        var : IDENTIFICADOR
            | IDENTIFICADOR indice
        '''
        if (len(p) == 2):
            p[0] = Arvore('var', [], p[1])

        elif (len(p) == 3):
            p[0] = Arvore('var', [p[2]], p[1])

    def p_indice(self,p):
        '''
        indice : indice ABRECOL expressao FECHACOL
                | ABRECOL expressao FECHACOL
        '''
        if (len(p) == 5):
            p[0] = Arvore('indice', [p[1], p[3]])
        elif (len(p) == 4):
            p[0] = Arvore('indice', [p[2]])

    def p_tipo(self,p):
        '''
        tipo : INTEIRO
        '''
        p[0] = Arvore('inteiro', [])

    def p_tipo2(self,p):
        '''
        tipo : FLUTUANTE
        '''
        p[0] = Arvore('flutuante', [])

    def p_declaracao_funcao(self,p):
        '''
        declaracao_funcao : tipo cabecalho
                            | cabecalho
        '''
        if len(p) == 3:
            p[0] = Arvore('declaracao_funcao', [p[1], p[2]])
        elif len(p) == 2:
            p[0] = Arvore('declaracao_funcao', [p[1]])

    def p_cabecalho(self,p):
        '''
        cabecalho : IDENTIFICADOR ABREPAR lista_parametros FECHAPAR corpo FIM
        '''
        p[0] = Arvore('cabecalho', [p[3], p[5]], p[1])

    def p_lista_parametros(self,p):
        '''
        lista_parametros : lista_parametros VIRGULA lista_parametros
                            | parametro
                            | vazio
        '''
        if len(p) == 4:
            p[0] = Arvore('lista_parametros', [p[1], p[3]])
        elif len(p) == 2:
            p[0] = Arvore('lista_parametros', [p[1]])

    def p_parametro1(self,p):
        '''
        parametro : tipo DOISPONTOS IDENTIFICADOR
        '''
        p[0] = Arvore('parametro', [p[1]], p[3])

    def p_parametro2(self,p):
        '''
        parametro : parametro ABRECOL FECHACOL
        '''
        p[0] = Arvore('parametro', [p[1]])

    def p_corpo(self,p):
        '''
        corpo : corpo acao
                | vazio
        '''
        if len(p) == 3:
            p[0] = Arvore('corpo', [p[1], p[2]])
        elif len(p) == 2:
            p[0] = Arvore('corpo', [p[1]])

    def p_acao(self,p):
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
        p[0] = Arvore('acao', [p[1]])

    def p_se(self,p):
        '''
        se : SE expressao ENTAO corpo FIM
            | SE expressao ENTAO corpo SENAO corpo FIM
        '''
        if len(p) == 6:
            p[0] = Arvore('se', [p[2], p[4]])
        elif len(p) == 8:
            p[0] = Arvore('se', [p[2], p[4], p[6]])

    def p_repita(self,p):
        '''
        repita : REPITA corpo ATE expressao
        '''
        p[0] = Arvore('repita', [p[2], p[4]])

    def p_atribuicao(self,p):
        '''
        atribuicao : var ATRIBUICAO expressao
        '''
        if len(self,p):
            p[0] = Arvore('atribuicao', [p[1], p[3]])

    def p_leia(self,p):
        '''
        leia : LEIA ABREPAR IDENTIFICADOR FECHAPAR
        '''
        if len(self,p):
            p[0] = Arvore('leia', [], p[3])

    def p_escreva(self,p):
        '''
        escreva : ESCREVA ABREPAR expressao FECHAPAR
        '''
        p[0] = Arvore('escreva', [p[3]])

    def p_retorna(self,p):
        '''
        retorna : RETORNA ABREPAR expressao FECHAPAR
        '''
        p[0] = Arvore('retorna', [p[3]])

    def p_expressao(self,p):
        '''
        expressao : expressao_simples
                    | atribuicao
        '''
        p[0] = Arvore('expressao', [p[1]])

    def p_expressao_simples(self,p):
        '''
        expressao_simples : expressao_aditiva
                            | expressao_simples operador_relacional expressao_aditiva
        '''
        if len(p) == 2:
            p[0] = Arvore('expressao_simples', [p[1]])
        elif len(p) == 4:
            p[0] = Arvore('expressao_simples', [p[1], p[2], p[3]])

    def p_expressao_aditiva(self,p):
        '''
        expressao_aditiva : expressao_multiplicativa
                            | expressao_aditiva operador_multiplicacao expressao_unaria
        '''
        if len(p) == 2:
            p[0] = Arvore('expressao_aditiva', [p[1]])
        elif len(p) == 4:
            p[0] = Arvore('expressao_aditiva', [p[1], p[2], p[3]])

    def p_expressao_multiplicativa(self,p):
        '''
       expressao_multiplicativa : expressao_unaria
                       | expressao_multiplicativa operador_multiplicacao expressao_unaria

        '''
        if len(p) == 2:
            p[0] = Arvore('expressao_multiplicativa', [p[1]])
        elif len(p) == 4:
            p[0] = Arvore('expressao_multiplicativa', [p[1], p[2], p[3]])

    def p_expressao_unaria(self,p):
        '''

        expressao_unaria : fator
                        | operador_soma fator

        '''

        if len(p) == 2:
            p[0] = Arvore('expressao_unaria', [p[1]])
        else:
            p[0] = Arvore('expressao_unaria', [p[1], p[2]])

    def p_operador_relacional(self,p):
        '''
        operador_relacional : MENOR
                            | MAIOR
                            | IGUALDADE
                            | MENORIGUAL
                            | MAIORIGUAL
                            | NEGACAO
        '''

        p[0] = Arvore('operador_relacional', [])

    def p_operador_soma(self,p):
        '''
        operador_soma : SOMA
                | SUBTRACAO
        '''
        p[0] = Arvore('operador_soma', [])

    def p_operador_multiplicacao(self,p):
        '''
        operador_multiplicacao : MULTIPLICACAO
                                | DIVISAO
        '''
        p[0] = Arvore('operador_multiplicacao', [])

    def p_error(self,p):
        if p:
            print("Erro sintático: '%s', linha %d" % (p.value, p.lineno))
            exit(1)
        else:
            yacc.restart()
            print('Erro sintático: definições incompletas!')
            exit(1)


def parse_Arvore(code):
    parser = yacc.yacc(debug=True)
    return parser.parse(code)


if __name__ == '__main__':
    import sys, io
    lista = io.open("saida.txt", mode="r", encoding="utf-8")
    parser = Parser(lista.read())
