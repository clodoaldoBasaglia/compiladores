from llvmlite import ir
from sintatica import *
from semantica import *
import io

class Generator():
    def __init__(self, code, optz= True, debug=True):
        s = Semantica(code.read())
        self.tree= s.tree
        self.table = s.simbolos
        self.builder=None
        self.modulo = ir.Module("programaModulo.bc")
        self.scope = "global"
        self.func = None
        self.printf= ir.Function(self.modulo, ir.FunctionType(ir.FloatType(), [ir.FloatType()]), "printf_f")
        self.scanf= ir.Function(self.modulo, ir.FunctionType(ir.FloatType(), [ir.FloatType()]), "scanf_f")
        self.inicioGeneracao(self.tree)
        print(self.modulo)
        saida = io.open("saida.txt",mode="w", encoding="utf-8")
        saida.write(str(self.modulo))
        saida.close()

    def inicioGeneracao(self,node):
        print("oi")
    #    if self.tree.type == "programa":
    #        self.programa(self.node.child[0])
    def lista_declaracoes(self, node):
        print("oi declaracao")
        if self.tree.type=="declaracao_variaveis":
            self.declaracao_variaveis(self.node.child[0])
        elif self.tree.type=="inicializacao_variaveis":
            self.inicializacao_variaveis(self.node.child[0])

    def principal(self,node):
        self.func = ir.Function(self.modulo, ir.FunctionType(ir.VoidType(),()),name='main')
        basicBlock = self.func.append_basic_block("entry")
        self.builder = ir.IRBuilder(basicBlock)
        self.scope = "principal"
        self.sequencia_decl(node.child[0])
        self.builder.ret_void()
        self.scope="global"

    def variavelGlobal(self,node):
        tipo = node.child[0].type
        nome = node.child[1].child[0].value
        if tipo == "inteiro":
            varGlobal = ir.GlobalVariable(self.modulo,ir.IntType(32),nome)
            globalVar.initializer = ir.Constant(ir.IntType(32), 0)
            globalVar.linkage = 'common'
        elif tipo =="flutuante":
            varGlobal = ir.GlobalVariable(self.modulo,ir.FloatType(32),nome)
            globalVar.initializer = ir.Constant(ir.FloatType(32), 0)
            globalVar.linkage = 'common'

if __name__=="__main__":
    import sys
    code = io.open(sys.argv[1], mode="r", encoding="utf-8")
    driver = Generator(code)
