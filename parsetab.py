
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftSOMASUBTRACAOleftMULTIPLICACAODIVISAODIVISAO VIRGULA ATRIBUICAO MENOR MAIOR IGUAL MENOR_IGUAL MAIOR_IGUAL ABRE_PARENTESES FECHA_PARENTESES DOIS_PONTOS ID SOMA SUBTRACAO NOVA_LINHA MULTIPLICACAO ABRE_COLXETE FECHA_COLXETE E_LOGICO NEGACAO SE ESCREVA FIM REPITA ATE FLUTUANTE LEIA INTEIRO SENAO ENTAO RETORNA VAZIO PRINCIPALprograma : lista_declaracoes lista_declaracoes : lista_declaracoes declaracao\n                            | declaracaodeclaracao : declaracao_variaveis\n                    | inicializacao_variaveis\n                    | declaracao_funcaodeclaracao_variaveis : tipo DOIS_PONTOS lista_variaveisinicializacao_variaveis : atribuicaolista_variaveis : lista_variaveis VIRGULA var\n                        | varvar : ID\n            | ID indice\n   indice : indice ABRE_COLXETE expressao FECHA_COLXETE\n                | ABRE_COLXETE expressao FECHA_COLXETE\n    tipo : INTEIRO\n    \n    tipo : FLUTUANTE\n    \n    declaracao_funcao : tipo cabecalho\n                        | cabecalho\n    \n    cabecalho : ID ABRE_PARENTESES lista_parametros FECHA_PARENTESES corpo FIM\n    \n    lista_parametros : lista_parametros VIRGULA lista_parametros\n                        | parametro\n                        | vazio\n    \n    parametro : tipo DOIS_PONTOS ID\n    \n    parametro : parametro ABRE_COLXETE FECHA_COLXETE\n    \n    corpo : corpo acao\n            | vazio\n    \n    acao : expressao\n            | declaracao_variaveis\n            | se\n            | repita\n            | leia\n            | escreva\n            | retorna\n            | error\n\n    \n    se : SE expressao ENTAO corpo FIM\n        | SE expressao ENTAO corpo SENAO corpo FIM\n    \n    repita : REPITA corpo ATE expressao\n    \n    atribuicao : var ATRIBUICAO expressao\n    \n    leia : LEIA ABRE_PARENTESES ID FECHA_PARENTESES\n    \n    escreva : ESCREVA ABRE_PARENTESES expressao FECHA_PARENTESES\n    \n    retorna : RETORNA ABRE_PARENTESES expressao FECHA_PARENTESES\n    \n    expressao : expressao_simples\n                | atribuicao\n    \n    expressao_simples : expressao_aditiva\n                        | expressao_simples operador_relacional expressao_aditiva\n    \n    expressao_aditiva : expressao_multiplicativa\n                        | expressao_aditiva operador_multiplicacao expressao_unaria\n    \n   expressao_multiplicativa : expressao_unaria\n                   | expressao_multiplicativa operador_multiplicacao expressao_unaria\n\n    \n    expressao_unaria : fator\n                    | operador_soma fator\n    \n    operador_relacional : MENOR\n                        | MAIOR\n                        | IGUAL\n                        | MENOR_IGUAL\n                        | MAIOR_IGUAL\n                        | NEGACAO\n    \n    operador_soma : SOMA\n            | SUBTRACAO\n    \n    operador_multiplicacao : MULTIPLICACAO\n                            | DIVISAO\n    \n    fator : ABRE_COLXETE  expressao FECHA_COLXETE\n            | var\n            | chamada_funcao\n            | numero\n    \n    numero : INTEIRO\n            | FLUTUANTE\n\n    \n    chamada_funcao : ID ABRE_PARENTESES lista_argumentos FECHA_PARENTESES\n    \n    lista_argumentos : lista_argumentos VIRGULA expressao\n                    | expressao\n                    | vazio\n    \n    vazio :\n    '
    
_lr_action_items = {'DIVISAO':([14,27,28,29,30,37,38,39,40,42,43,60,66,67,70,76,77,78,82,89,101,103,],[-12,-64,-50,-63,-65,64,-66,-11,-67,64,-48,-14,-63,-51,-13,64,-62,-47,-49,-66,-67,-68,]),'MULTIPLICACAO':([14,27,28,29,30,37,38,39,40,42,43,60,66,67,70,76,77,78,82,89,101,103,],[-12,-64,-50,-63,-65,63,-66,-11,-67,63,-48,-14,-63,-51,-13,63,-62,-47,-49,-66,-67,-68,]),'SE':([14,27,28,29,30,32,33,37,38,39,40,42,43,44,45,46,47,50,60,66,67,70,72,73,76,77,78,82,83,86,87,88,89,90,93,94,95,96,99,100,101,103,108,112,115,116,117,118,119,120,121,122,123,],[-12,-64,-50,-63,-65,-42,-43,-44,-66,-11,-67,-46,-48,-10,-11,-7,-38,-72,-14,-63,-51,-13,92,-26,-45,-62,-47,-49,-9,-34,-33,-30,-66,-28,-29,-32,-31,-27,-25,-72,-67,-68,92,-72,-41,-40,92,-39,-37,-35,-72,92,-36,]),'FECHA_PARENTESES':([14,15,23,24,25,27,28,29,30,32,33,37,38,39,40,42,43,47,51,60,65,66,67,70,71,74,75,76,77,78,79,80,81,82,103,109,110,111,113,],[-12,-72,-21,50,-22,-64,-50,-63,-65,-42,-43,-44,-66,-11,-67,-46,-48,-38,-72,-14,-72,-63,-51,-13,-24,-20,-23,-45,-62,-47,103,-70,-71,-49,-68,-69,115,116,118,]),'ATRIBUICAO':([2,7,14,29,39,60,70,],[-11,20,-12,20,-11,-14,-13,]),'ID':([0,1,3,4,5,6,8,9,11,12,13,14,16,17,19,20,21,22,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,62,63,64,65,66,67,68,69,70,72,73,76,77,78,82,83,85,86,87,88,89,90,92,93,94,95,96,99,100,101,102,103,104,105,107,108,112,114,115,116,117,118,119,120,121,122,123,],[2,-6,-3,-5,-8,18,2,-15,-16,-4,-18,-12,39,45,-17,39,-2,39,-64,-50,-63,-65,-59,-42,-43,-58,39,-44,-66,-11,-67,39,-46,-48,-10,-11,-7,-38,-72,75,39,-55,-56,-52,-54,-57,-53,-14,39,-60,-61,39,-63,-51,39,45,-13,39,-26,-45,-62,-47,-49,-9,-19,-34,-33,-30,-66,-28,39,-29,-32,-31,-27,-25,-72,-67,39,-68,39,39,113,39,-72,39,-41,-40,39,-39,-37,-35,-72,39,-36,]),'ABRE_PARENTESES':([2,18,39,84,91,98,],[15,15,65,104,105,107,]),'ENTAO':([14,27,28,29,30,32,33,37,38,39,40,42,43,47,60,66,67,70,76,77,78,82,103,106,],[-12,-64,-50,-63,-65,-42,-43,-44,-66,-11,-67,-46,-48,-38,-14,-63,-51,-13,-45,-62,-47,-49,-68,112,]),'$end':([1,3,4,5,8,10,12,13,14,19,21,27,28,29,30,32,33,37,38,39,40,42,43,44,45,46,47,60,66,67,70,76,77,78,82,83,85,103,],[-6,-3,-5,-8,-1,0,-4,-18,-12,-17,-2,-64,-50,-63,-65,-42,-43,-44,-66,-11,-67,-46,-48,-10,-11,-7,-38,-14,-63,-51,-13,-45,-62,-47,-49,-9,-19,-68,]),'FIM':([14,27,28,29,30,32,33,37,38,39,40,42,43,44,45,46,47,50,60,66,67,70,72,73,76,77,78,82,83,86,87,88,89,90,93,94,95,96,99,101,103,112,115,116,117,118,119,120,121,122,123,],[-12,-64,-50,-63,-65,-42,-43,-44,-66,-11,-67,-46,-48,-10,-11,-7,-38,-72,-14,-63,-51,-13,85,-26,-45,-62,-47,-49,-9,-34,-33,-30,-66,-28,-29,-32,-31,-27,-25,-67,-68,-72,-41,-40,120,-39,-37,-35,-72,123,-36,]),'VIRGULA':([14,15,23,24,25,27,28,29,30,32,33,37,38,39,40,42,43,44,45,46,47,51,60,65,66,67,70,71,74,75,76,77,78,79,80,81,82,83,103,109,],[-12,-72,-21,51,-22,-64,-50,-63,-65,-42,-43,-44,-66,-11,-67,-46,-48,-10,-11,69,-38,-72,-14,-72,-63,-51,-13,-24,51,-23,-45,-62,-47,102,-70,-71,-49,-9,-68,-69,]),'MENOR':([14,27,28,29,30,32,37,38,39,40,42,43,60,66,67,70,76,77,78,82,89,101,103,],[-12,-64,-50,-63,-65,56,-44,-66,-11,-67,-46,-48,-14,-63,-51,-13,-45,-62,-47,-49,-66,-67,-68,]),'SENAO':([14,27,28,29,30,32,33,37,38,39,40,42,43,44,45,46,47,60,66,67,70,73,76,77,78,82,83,86,87,88,89,90,93,94,95,96,99,101,103,112,115,116,117,118,119,120,123,],[-12,-64,-50,-63,-65,-42,-43,-44,-66,-11,-67,-46,-48,-10,-11,-7,-38,-14,-63,-51,-13,-26,-45,-62,-47,-49,-9,-34,-33,-30,-66,-28,-29,-32,-31,-27,-25,-67,-68,-72,-41,-40,121,-39,-37,-35,-36,]),'MAIOR':([14,27,28,29,30,32,37,38,39,40,42,43,60,66,67,70,76,77,78,82,89,101,103,],[-12,-64,-50,-63,-65,59,-44,-66,-11,-67,-46,-48,-14,-63,-51,-13,-45,-62,-47,-49,-66,-67,-68,]),'ATE':([14,27,28,29,30,32,33,37,38,39,40,42,43,44,45,46,47,60,66,67,70,73,76,77,78,82,83,86,87,88,89,90,93,94,95,96,99,100,101,103,108,115,116,118,119,120,123,],[-12,-64,-50,-63,-65,-42,-43,-44,-66,-11,-67,-46,-48,-10,-11,-7,-38,-14,-63,-51,-13,-26,-45,-62,-47,-49,-9,-34,-33,-30,-66,-28,-29,-32,-31,-27,-25,-72,-67,-68,114,-41,-40,-39,-37,-35,-36,]),'SOMA':([14,16,20,22,27,28,29,30,32,33,36,37,38,39,40,42,43,44,45,46,47,50,53,54,55,56,57,58,59,60,62,63,64,65,66,67,68,70,72,73,76,77,78,82,83,86,87,88,89,90,92,93,94,95,96,99,100,101,102,103,104,105,108,112,114,115,116,117,118,119,120,121,122,123,],[-12,35,35,35,-64,-50,-63,-65,-42,-43,35,-44,-66,-11,-67,-46,-48,-10,-11,-7,-38,-72,35,-55,-56,-52,-54,-57,-53,-14,35,-60,-61,35,-63,-51,35,-13,35,-26,-45,-62,-47,-49,-9,-34,-33,-30,-66,-28,35,-29,-32,-31,-27,-25,-72,-67,35,-68,35,35,35,-72,35,-41,-40,35,-39,-37,-35,-72,35,-36,]),'MENOR_IGUAL':([14,27,28,29,30,32,37,38,39,40,42,43,60,66,67,70,76,77,78,82,89,101,103,],[-12,-64,-50,-63,-65,54,-44,-66,-11,-67,-46,-48,-14,-63,-51,-13,-45,-62,-47,-49,-66,-67,-68,]),'FECHA_COLXETE':([14,27,28,29,30,32,33,34,37,38,39,40,42,43,47,48,49,60,61,66,67,70,76,77,78,82,103,],[-12,-64,-50,-63,-65,-42,-43,60,-44,-66,-11,-67,-46,-48,-38,70,71,-14,77,-63,-51,-13,-45,-62,-47,-49,-68,]),'error':([14,27,28,29,30,32,33,37,38,39,40,42,43,44,45,46,47,50,60,66,67,70,72,73,76,77,78,82,83,86,87,88,89,90,93,94,95,96,99,100,101,103,108,112,115,116,117,118,119,120,121,122,123,],[-12,-64,-50,-63,-65,-42,-43,-44,-66,-11,-67,-46,-48,-10,-11,-7,-38,-72,-14,-63,-51,-13,86,-26,-45,-62,-47,-49,-9,-34,-33,-30,-66,-28,-29,-32,-31,-27,-25,-72,-67,-68,86,-72,-41,-40,86,-39,-37,-35,-72,86,-36,]),'RETORNA':([14,27,28,29,30,32,33,37,38,39,40,42,43,44,45,46,47,50,60,66,67,70,72,73,76,77,78,82,83,86,87,88,89,90,93,94,95,96,99,100,101,103,108,112,115,116,117,118,119,120,121,122,123,],[-12,-64,-50,-63,-65,-42,-43,-44,-66,-11,-67,-46,-48,-10,-11,-7,-38,-72,-14,-63,-51,-13,84,-26,-45,-62,-47,-49,-9,-34,-33,-30,-66,-28,-29,-32,-31,-27,-25,-72,-67,-68,84,-72,-41,-40,84,-39,-37,-35,-72,84,-36,]),'LEIA':([14,27,28,29,30,32,33,37,38,39,40,42,43,44,45,46,47,50,60,66,67,70,72,73,76,77,78,82,83,86,87,88,89,90,93,94,95,96,99,100,101,103,108,112,115,116,117,118,119,120,121,122,123,],[-12,-64,-50,-63,-65,-42,-43,-44,-66,-11,-67,-46,-48,-10,-11,-7,-38,-72,-14,-63,-51,-13,98,-26,-45,-62,-47,-49,-9,-34,-33,-30,-66,-28,-29,-32,-31,-27,-25,-72,-67,-68,98,-72,-41,-40,98,-39,-37,-35,-72,98,-36,]),'INTEIRO':([0,1,3,4,5,8,12,13,14,15,16,19,20,21,22,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,50,51,53,54,55,56,57,58,59,60,62,63,64,65,66,67,68,70,72,73,76,77,78,82,83,85,86,87,88,89,90,92,93,94,95,96,99,100,101,102,103,104,105,108,112,114,115,116,117,118,119,120,121,122,123,],[9,-6,-3,-5,-8,9,-4,-18,-12,9,38,-17,38,-2,38,-64,-50,-63,-65,-59,-42,-43,-58,38,-44,-66,-11,-67,38,-46,-48,-10,-11,-7,-38,-72,9,38,-55,-56,-52,-54,-57,-53,-14,38,-60,-61,38,-63,-51,38,-13,89,-26,-45,-62,-47,-49,-9,-19,-34,-33,-30,-66,-28,38,-29,-32,-31,-27,-25,-72,-67,38,-68,38,38,89,-72,38,-41,-40,89,-39,-37,-35,-72,89,-36,]),'IGUAL':([14,27,28,29,30,32,37,38,39,40,42,43,60,66,67,70,76,77,78,82,89,101,103,],[-12,-64,-50,-63,-65,57,-44,-66,-11,-67,-46,-48,-14,-63,-51,-13,-45,-62,-47,-49,-66,-67,-68,]),'NEGACAO':([14,27,28,29,30,32,37,38,39,40,42,43,60,66,67,70,76,77,78,82,89,101,103,],[-12,-64,-50,-63,-65,58,-44,-66,-11,-67,-46,-48,-14,-63,-51,-13,-45,-62,-47,-49,-66,-67,-68,]),'DOIS_PONTOS':([6,9,11,26,89,97,101,],[17,-15,-16,52,-15,17,-16,]),'REPITA':([14,27,28,29,30,32,33,37,38,39,40,42,43,44,45,46,47,50,60,66,67,70,72,73,76,77,78,82,83,86,87,88,89,90,93,94,95,96,99,100,101,103,108,112,115,116,117,118,119,120,121,122,123,],[-12,-64,-50,-63,-65,-42,-43,-44,-66,-11,-67,-46,-48,-10,-11,-7,-38,-72,-14,-63,-51,-13,100,-26,-45,-62,-47,-49,-9,-34,-33,-30,-66,-28,-29,-32,-31,-27,-25,-72,-67,-68,100,-72,-41,-40,100,-39,-37,-35,-72,100,-36,]),'ESCREVA':([14,27,28,29,30,32,33,37,38,39,40,42,43,44,45,46,47,50,60,66,67,70,72,73,76,77,78,82,83,86,87,88,89,90,93,94,95,96,99,100,101,103,108,112,115,116,117,118,119,120,121,122,123,],[-12,-64,-50,-63,-65,-42,-43,-44,-66,-11,-67,-46,-48,-10,-11,-7,-38,-72,-14,-63,-51,-13,91,-26,-45,-62,-47,-49,-9,-34,-33,-30,-66,-28,-29,-32,-31,-27,-25,-72,-67,-68,91,-72,-41,-40,91,-39,-37,-35,-72,91,-36,]),'FLUTUANTE':([0,1,3,4,5,8,12,13,14,15,16,19,20,21,22,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,50,51,53,54,55,56,57,58,59,60,62,63,64,65,66,67,68,70,72,73,76,77,78,82,83,85,86,87,88,89,90,92,93,94,95,96,99,100,101,102,103,104,105,108,112,114,115,116,117,118,119,120,121,122,123,],[11,-6,-3,-5,-8,11,-4,-18,-12,11,40,-17,40,-2,40,-64,-50,-63,-65,-59,-42,-43,-58,40,-44,-66,-11,-67,40,-46,-48,-10,-11,-7,-38,-72,11,40,-55,-56,-52,-54,-57,-53,-14,40,-60,-61,40,-63,-51,40,-13,101,-26,-45,-62,-47,-49,-9,-19,-34,-33,-30,-66,-28,40,-29,-32,-31,-27,-25,-72,-67,40,-68,40,40,101,-72,40,-41,-40,101,-39,-37,-35,-72,101,-36,]),'SUBTRACAO':([14,16,20,22,27,28,29,30,32,33,36,37,38,39,40,42,43,44,45,46,47,50,53,54,55,56,57,58,59,60,62,63,64,65,66,67,68,70,72,73,76,77,78,82,83,86,87,88,89,90,92,93,94,95,96,99,100,101,102,103,104,105,108,112,114,115,116,117,118,119,120,121,122,123,],[-12,31,31,31,-64,-50,-63,-65,-42,-43,31,-44,-66,-11,-67,-46,-48,-10,-11,-7,-38,-72,31,-55,-56,-52,-54,-57,-53,-14,31,-60,-61,31,-63,-51,31,-13,31,-26,-45,-62,-47,-49,-9,-34,-33,-30,-66,-28,31,-29,-32,-31,-27,-25,-72,-67,31,-68,31,31,31,-72,31,-41,-40,31,-39,-37,-35,-72,31,-36,]),'ABRE_COLXETE':([2,14,16,20,22,23,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,50,53,54,55,56,57,58,59,60,62,63,64,65,66,67,68,70,71,72,73,75,76,77,78,82,83,86,87,88,89,90,92,93,94,95,96,99,100,101,102,103,104,105,108,112,114,115,116,117,118,119,120,121,122,123,],[16,22,36,36,36,49,-64,-50,-63,-65,-59,-42,-43,-58,36,-44,-66,16,-67,36,-46,-48,-10,16,-7,-38,-72,36,-55,-56,-52,-54,-57,-53,-14,36,-60,-61,36,-63,-51,36,-13,-24,36,-26,-23,-45,-62,-47,-49,-9,-34,-33,-30,-66,-28,36,-29,-32,-31,-27,-25,-72,-67,36,-68,36,36,36,-72,36,-41,-40,36,-39,-37,-35,-72,36,-36,]),'MAIOR_IGUAL':([14,27,28,29,30,32,37,38,39,40,42,43,60,66,67,70,76,77,78,82,89,101,103,],[-12,-64,-50,-63,-65,55,-44,-66,-11,-67,-46,-48,-14,-63,-51,-13,-45,-62,-47,-49,-66,-67,-68,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracao_funcao':([0,8,],[1,1,]),'chamada_funcao':([16,20,22,36,41,53,62,65,68,72,92,102,104,105,108,114,117,122,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'fator':([16,20,22,36,41,53,62,65,68,72,92,102,104,105,108,114,117,122,],[28,28,28,28,67,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'operador_multiplicacao':([37,42,76,],[62,68,62,]),'escreva':([72,108,117,122,],[94,94,94,94,]),'atribuicao':([0,8,16,20,22,36,65,72,92,102,104,105,108,114,117,122,],[5,5,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'corpo':([50,100,112,121,],[72,108,117,122,]),'operador_relacional':([32,],[53,]),'inicializacao_variaveis':([0,8,],[4,4,]),'numero':([16,20,22,36,41,53,62,65,68,72,92,102,104,105,108,114,117,122,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'leia':([72,108,117,122,],[95,95,95,95,]),'lista_argumentos':([65,],[79,]),'lista_parametros':([15,51,],[24,74,]),'expressao_simples':([16,20,22,36,65,72,92,102,104,105,108,114,117,122,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'declaracao':([0,8,],[3,21,]),'retorna':([72,108,117,122,],[87,87,87,87,]),'vazio':([15,50,51,65,100,112,121,],[25,73,25,81,73,73,73,]),'lista_variaveis':([17,],[46,]),'tipo':([0,8,15,51,72,108,117,122,],[6,6,26,26,97,97,97,97,]),'lista_declaracoes':([0,],[8,]),'var':([0,8,16,17,20,22,36,41,53,62,65,68,69,72,92,102,104,105,108,114,117,122,],[7,7,29,44,29,29,29,66,66,66,29,66,83,29,29,29,29,29,29,29,29,29,]),'expressao':([16,20,22,36,65,72,92,102,104,105,108,114,117,122,],[34,47,48,61,80,96,106,109,110,111,96,119,96,96,]),'repita':([72,108,117,122,],[88,88,88,88,]),'acao':([72,108,117,122,],[99,99,99,99,]),'parametro':([15,51,],[23,23,]),'expressao_aditiva':([16,20,22,36,53,65,72,92,102,104,105,108,114,117,122,],[37,37,37,37,76,37,37,37,37,37,37,37,37,37,37,]),'se':([72,108,117,122,],[93,93,93,93,]),'programa':([0,],[10,]),'operador_soma':([16,20,22,36,53,62,65,68,72,92,102,104,105,108,114,117,122,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'declaracao_variaveis':([0,8,72,108,117,122,],[12,12,90,90,90,90,]),'indice':([2,39,45,],[14,14,14,]),'expressao_multiplicativa':([16,20,22,36,53,65,72,92,102,104,105,108,114,117,122,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'cabecalho':([0,6,8,],[13,19,13,]),'expressao_unaria':([16,20,22,36,53,62,65,68,72,92,102,104,105,108,114,117,122,],[43,43,43,43,43,78,43,82,43,43,43,43,43,43,43,43,43,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaracoes','programa',1,'p_programa_1','sintatica.py',26),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoesl','sintatica.py',31),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoesl','sintatica.py',32),
  ('declaracao -> declaracao_variaveis','declaracao',1,'p_declaracao','sintatica.py',40),
  ('declaracao -> inicializacao_variaveis','declaracao',1,'p_declaracao','sintatica.py',41),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','sintatica.py',42),
  ('declaracao_variaveis -> tipo DOIS_PONTOS lista_variaveis','declaracao_variaveis',3,'p_declaracao_variaveis','sintatica.py',47),
  ('inicializacao_variaveis -> atribuicao','inicializacao_variaveis',1,'p_inicializacao_variaveis','sintatica.py',52),
  ('lista_variaveis -> lista_variaveis VIRGULA var','lista_variaveis',3,'p_lista_variaveis','sintatica.py',57),
  ('lista_variaveis -> var','lista_variaveis',1,'p_lista_variaveis','sintatica.py',58),
  ('var -> ID','var',1,'p_var','sintatica.py',67),
  ('var -> ID indice','var',2,'p_var','sintatica.py',68),
  ('indice -> indice ABRE_COLXETE expressao FECHA_COLXETE','indice',4,'p_indice','sintatica.py',79),
  ('indice -> ABRE_COLXETE expressao FECHA_COLXETE','indice',3,'p_indice','sintatica.py',80),
  ('tipo -> INTEIRO','tipo',1,'p_tipo','sintatica.py',89),
  ('tipo -> FLUTUANTE','tipo',1,'p_tipo2','sintatica.py',97),
  ('declaracao_funcao -> tipo cabecalho','declaracao_funcao',2,'p_declaracao_funcao','sintatica.py',105),
  ('declaracao_funcao -> cabecalho','declaracao_funcao',1,'p_declaracao_funcao','sintatica.py',106),
  ('cabecalho -> ID ABRE_PARENTESES lista_parametros FECHA_PARENTESES corpo FIM','cabecalho',6,'p_cabecalho','sintatica.py',117),
  ('lista_parametros -> lista_parametros VIRGULA lista_parametros','lista_parametros',3,'p_lista_parametros','sintatica.py',125),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros','sintatica.py',126),
  ('lista_parametros -> vazio','lista_parametros',1,'p_lista_parametros','sintatica.py',127),
  ('parametro -> tipo DOIS_PONTOS ID','parametro',3,'p_parametro1','sintatica.py',138),
  ('parametro -> parametro ABRE_COLXETE FECHA_COLXETE','parametro',3,'p_parametro2','sintatica.py',145),
  ('corpo -> corpo acao','corpo',2,'p_corpo','sintatica.py',152),
  ('corpo -> vazio','corpo',1,'p_corpo','sintatica.py',153),
  ('acao -> expressao','acao',1,'p_acao','sintatica.py',163),
  ('acao -> declaracao_variaveis','acao',1,'p_acao','sintatica.py',164),
  ('acao -> se','acao',1,'p_acao','sintatica.py',165),
  ('acao -> repita','acao',1,'p_acao','sintatica.py',166),
  ('acao -> leia','acao',1,'p_acao','sintatica.py',167),
  ('acao -> escreva','acao',1,'p_acao','sintatica.py',168),
  ('acao -> retorna','acao',1,'p_acao','sintatica.py',169),
  ('acao -> error','acao',1,'p_acao','sintatica.py',170),
  ('se -> SE expressao ENTAO corpo FIM','se',5,'p_se','sintatica.py',178),
  ('se -> SE expressao ENTAO corpo SENAO corpo FIM','se',7,'p_se','sintatica.py',179),
  ('repita -> REPITA corpo ATE expressao','repita',4,'p_repita','sintatica.py',189),
  ('atribuicao -> var ATRIBUICAO expressao','atribuicao',3,'p_atribuicao','sintatica.py',196),
  ('leia -> LEIA ABRE_PARENTESES ID FECHA_PARENTESES','leia',4,'p_leia','sintatica.py',204),
  ('escreva -> ESCREVA ABRE_PARENTESES expressao FECHA_PARENTESES','escreva',4,'p_escreva','sintatica.py',212),
  ('retorna -> RETORNA ABRE_PARENTESES expressao FECHA_PARENTESES','retorna',4,'p_retorna','sintatica.py',219),
  ('expressao -> expressao_simples','expressao',1,'p_expressao','sintatica.py',226),
  ('expressao -> atribuicao','expressao',1,'p_expressao','sintatica.py',227),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_expressao_simples','sintatica.py',234),
  ('expressao_simples -> expressao_simples operador_relacional expressao_aditiva','expressao_simples',3,'p_expressao_simples','sintatica.py',235),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_expressao_aditiva','sintatica.py',245),
  ('expressao_aditiva -> expressao_aditiva operador_multiplicacao expressao_unaria','expressao_aditiva',3,'p_expressao_aditiva','sintatica.py',246),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_expressao_multiplicativa','sintatica.py',256),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_expressao_multiplicativa','sintatica.py',257),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_expressao_unaria','sintatica.py',268),
  ('expressao_unaria -> operador_soma fator','expressao_unaria',2,'p_expressao_unaria','sintatica.py',269),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_operador_relacional','sintatica.py',280),
  ('operador_relacional -> MAIOR','operador_relacional',1,'p_operador_relacional','sintatica.py',281),
  ('operador_relacional -> IGUAL','operador_relacional',1,'p_operador_relacional','sintatica.py',282),
  ('operador_relacional -> MENOR_IGUAL','operador_relacional',1,'p_operador_relacional','sintatica.py',283),
  ('operador_relacional -> MAIOR_IGUAL','operador_relacional',1,'p_operador_relacional','sintatica.py',284),
  ('operador_relacional -> NEGACAO','operador_relacional',1,'p_operador_relacional','sintatica.py',285),
  ('operador_soma -> SOMA','operador_soma',1,'p_operador_soma','sintatica.py',293),
  ('operador_soma -> SUBTRACAO','operador_soma',1,'p_operador_soma','sintatica.py',294),
  ('operador_multiplicacao -> MULTIPLICACAO','operador_multiplicacao',1,'p_operador_multiplicacao','sintatica.py',301),
  ('operador_multiplicacao -> DIVISAO','operador_multiplicacao',1,'p_operador_multiplicacao','sintatica.py',302),
  ('fator -> ABRE_COLXETE expressao FECHA_COLXETE','fator',3,'p_fator','sintatica.py',309),
  ('fator -> var','fator',1,'p_fator','sintatica.py',310),
  ('fator -> chamada_funcao','fator',1,'p_fator','sintatica.py',311),
  ('fator -> numero','fator',1,'p_fator','sintatica.py',312),
  ('numero -> INTEIRO','numero',1,'p_numero','sintatica.py',322),
  ('numero -> FLUTUANTE','numero',1,'p_numero','sintatica.py',323),
  ('chamada_funcao -> ID ABRE_PARENTESES lista_argumentos FECHA_PARENTESES','chamada_funcao',4,'p_chamada_funcao','sintatica.py',331),
  ('lista_argumentos -> lista_argumentos VIRGULA expressao','lista_argumentos',3,'p_lista_argumentos','sintatica.py',338),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_lista_argumentos','sintatica.py',339),
  ('lista_argumentos -> vazio','lista_argumentos',1,'p_lista_argumentos','sintatica.py',340),
  ('vazio -> <empty>','vazio',0,'p_vazio','sintatica.py',350),
]