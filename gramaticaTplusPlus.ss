programa ::= lista_declaracoes

lista_declaracoes ::= lista_declaracoes declaracao
			| declaracao

declaracao ::= declaracao_variaveis
		|inicializacao_variaveis
		|declaracao_funcao
declaracao_variaveis ::=tipo ":" lista_variaveis
iniciazacao_variaveis ::= atribuicao
lista_variaveis := lista_variaveis "," var
		|var
var::= ID
	|ID indice
indice::=indice"["expressao"]"
	|"["expressao"]"

tipo::=INTEIRO
	|FLUTUANTE
declaracao_funcao::= tipo cabelcalho
		|cabecalho

cabecalho::= ID "("lista_parametros")" corpo FIM

lista_parametros::=lista_parametros","parametro
		|parametro
		|vazio
parametro::=tipo":"ID
	|parametro "[""]"
corpo::=corpo acao
	|vazio
acao::= expressao
	|declaracao_variaveis
	|se
	|repita
	|leia
	|escreva
	|retorna
	|erro
se::= SE expressao ENTAO corpo fim
	|SE expressao ENTAO corpo SENAO corpo FIM
repita::=REPTIA corpo ATE expressao
atribuicao::=var":="expressao
leia::= LEIA "("ID")"
escreva::= ESCREVA"("expressao")"
retorna::=RETORNA"("expressao")"
expressao::= expressao_simples
	|atribuicao
expressao_simples::= expressao_aditiva
	|expressao_simples operador_relacional expressao_aditiva
expressao_aditiva::= expressao_multiplicativa
	|expressao_aditiva operador_soma expressao_multiplicativa
expressao_multiplicativa e
