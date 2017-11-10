import ply.yacc as yacc
from lexicanum import tokens


class Arvore:
    def __init__(self, type_node, child=[], value=''):
        self.type = type_node
        self.child = child
        self.value = value

    def __str__(self):
        return self.value


tokens = tokens
precedence = (
    ('left', 'IGUALDADE', 'NEGACAO', 'MAIOR_IGUAL', 'MAIOR', 'MENOR_IGUAL', 'MENOR'),
    ('left', 'SOMA', 'SUBTRACAO'),
    ('left', 'MULTIPLICACAO', 'DIVISAO'),
)


def p_programa(p):
    '''
    programa : lista_declaracoes
    '''
    p[0] = Arvore('programa', [p[1]])


def p_lista_declaracoes(p):
    '''
    	 	lista_declaracoes : lista_declaracoes declaracao
    	 						| declaracao
    	 	'''
    if (len(p) == 3):
        p[0] = Arvore('lista_declaracoes', [p[1], p[2]])
    elif (len(p) == 2):
        p[0] = Arvore('lista_declaracoes', [p[1]])


def p_declaraco(p):
    '''
    	 	declaracao : declaracao_variaveis
    	 				| inicializacao_variaveis
    					| declaracao_funcao
    	 	'''
    p[0] = Arvore('declaracao', [p[1]])


def p_declaracao_variaveis(p):
    '''
    		declaracao_variaveis : tipo DOISPONTOS lista_variaveis
    	 	'''
    p[0] = Arvore('declaracao_variaveis', [p[1], p[3]], p[2])


def p_inicializacao_variaveis(p):
    '''
    	 	inicializacao_variaveis : atribuicao
    	 	'''
    p[0] = Arvore('inicializacao_variaveis', [p[1]])


def p_lista_variaveis(p):
    '''
    	 	lista_variaveis : lista_variaveis VIRGULA var
    	 	 	 	 		| var
    		'''
    if (len(p) == 4):
        p[0] = Arvore('lista_variaveis', [p[1], p[3]])

    elif (len(p) == 2):
        p[0] = Arvore('lista_variaveis', [p[1]])


def p_var(p):
    '''
    		var : IDENTIFICADOR
    			| IDENTIFICADOR indice
    		'''
    if (len(p) == 2):
        p[0] = Arvore('var', [], p[1])

    elif (len(p) == 3):
        p[0] = Arvore('var', [p[2]], p[1])


def p_error(p):
    if p:
        print("Erro sintático: '%s', linha %d" % (p.value, p.lineno))
        exit(1)
    else:
        yacc.restart()
        print('Erro sintático: definições incompletas!')
        exit(1)


def parse_tree(code):
    parser = yacc.yacc(debug=True)
    return parser.parse(code)


if __name__ == '__main__':
    import sys, io

    lista = io.open("saida.txt", mode="r", encoding="utf-8")
    parser = yacc.yacc(debug='True')
    print(parser.parse(lista.read()))
