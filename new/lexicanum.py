import ply.lex as lex
import io


class Lexicanum:
    def __init__(self):
        self.lexer = lex.lex(debug=False, module=self)

    palavrasReservadas = {
        'se': 'SE',
        'então': 'ENTAO',
        'senão': 'SENAO',
        'fim': 'FIM',
        'flutuante': 'FLUTUANTE',
        'inteiro': 'INTEIRO',
        'vazio': 'VAZIO',
        'até': 'ATE',
        'repita': 'REPITA',
        'leia': 'LEIA',
        'escreva': 'ESCREVA',
        'principal': 'PRINCIPAL',
        'retorna': 'RETORNA'
    }
    tokens = ['DIVISAO', 'VIRGULA', 'ATRIBUICAO', 'MENOR', 'MAIOR', 'IGUAL', 'MENOR_IGUAL', 'MAIOR_IGUAL',
              'ABRE_PARENTESES', 'FECHA_PARENTESES', 'DOIS_PONTOS', 'SOMA', 'SUBTRACAO', 'NOVA_LINHA', 'OU_LOGICO',
              'MULTIPLICACAO', 'ABRE_COLXETE', 'FECHA_COLXETE', 'IDENTIFICADOR', 'E_LOGICO', 'NEGACAO'] + list(
        palavrasReservadas.values())
    t_SOMA = r'\+'
    t_SUBTRACAO = r'-'
    t_MULTIPLICACAO = r'\*'
    t_DIVISAO = r'\/'
    t_IGUAL = r'\='
    t_ABRE_PARENTESES = r'\('
    t_FECHA_PARENTESES = r'\)'
    t_VIRGULA = r'\,'
    t_MENOR = r'\<'
    t_MAIOR = r'\>'
    t_ATRIBUICAO = r':\='
    t_MENOR_IGUAL = r'<='
    t_MAIOR_IGUAL = r'>='
    t_DOIS_PONTOS = r':'
    t_ABRE_COLXETE = r'\['
    t_FECHA_COLXETE = r'\]'
    t_E_LOGICO = r'&&'
    t_NEGACAO = r'!'
    t_OU_LOGICO = r'\|\|'

    def t_IDENTIFICADOR(self, t):
        r'[a-zA-Zà-ú][0-9a-zà-úA-Z]*'
        t.type = self.palavrasReservadas.get(t.value, 'IDENTIFICADOR')
        return t

    def t_FLUTUANTE(self, t):
        r'[0-9]+(\.[0-9]+)(e(\+|\-)?(\d+))?'
        t.value = float(t.value)
        return t

    def t_INTEIRO(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_COMENTARIO(self, t):
        r'{[^\{^\}]*}'
        for x in range(1, len(t.value)):
            if t.value[x] == "\n":
                t.lexer.lineno += 1
        pass

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        t.type = "NOVA_LINHA"
        return t

    # Ignora tabs e espacos
    t_ignore = ' \t'

    # Erro
    def t_error(self, t):
        print("Erro '%s', linha %d" % (t.value[0], t.lineno))
        print(type(t.value))
        exit(0)

    def test(self, code):
        saida = io.open("saida.txt", mode="w", encoding="utf-8")
        lex.input(code)
        while True:
            t = lex.token()
            if not t:
                break
            print(t)
            saida.write(str(t) + "\n")
        saida.close()

if __name__ == '__main__':
    import sys

    # Para compilar no terminal
    # codigo = io.open(sys.argv[1], mode="r", encoding="utf-8")
    # para compilar no PyCharm
    codigo = io.open("../testes/multiplicavetor.tpp", mode="r", encoding="utf-8")
    lexico = Lexicanum()
    lexico.test(codigo.read())
