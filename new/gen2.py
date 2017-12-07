from parser import *
from llvmlite import ir
from semantica import *
import io

class Generator():
    def __init__(self, code, optz=True, debug=True):
        s = Semantica(code.read())
        s.raiz()

        self.tree = s.tree
        self.table = s.simbolos
        self.builder = None
        self.modulo = ir.Module("programaModulo.bc")
        self.scope = "global"
        self.func = None
        self.var = None
        self.printf = ir.Function(self.modulo, ir.FunctionType(ir.FloatType(), [ir.FloatType()]), "printf_f")
        self.scanf = ir.Function(self.modulo, ir.FunctionType(ir.FloatType(), [ir.FloatType()]), "scanf_f")
        self.inicioGeneracao(self.tree)
        # print(self.printf_f)
        print(self.modulo)
        f = io.open("saida.txt", mode="r", encoding="utf-8")
        f.write(str(self.modulo))
        f.close()


    def inicioGeneracao(self, node):
        print("oi")
        if self.tree.type == "programa":
            self.principal(self.tree.child[0])


    def lista_declaracoes(self, node):
        print("oi declaracao")
        if self.tree.type == "declaracao_variaveis":
            self.var(self.node.child[0])
        elif self.tree.type == "inicializacao_variaveis":
            self.var(self.node.child[0])


    def principal(self, node):
        self.func = ir.Function(self.modulo, ir.FunctionType(ir.VoidType(), ()), name='main')
        basicBlock = self.func.append_basic_block("entry")
        self.builder = ir.IRBuilder(basicBlock)
        self.scope = "principal"
        self.var(self.node.child[0])
        self.builder.ret_void()
        self.scope = "global"


    def variavelGlobal(self, node):
        tipo = node.child[0].type
        nome = node.child[1].child[0].value
        if tipo == "inteiro":
            varGlobal = ir.GlobalVariable(self.modulo, ir.IntType(32), nome)
            globalVar.initializer = ir.Constant(ir.IntType(32), 0)
            globalVar.linkage = 'common'
        elif tipo == "flutuante":
            varGlobal = ir.GlobalVariable(self.modulo, ir.FloatType(32), nome)
            globalVar.initializer = ir.Constant(ir.FloatType(32), 0)
            globalVar.linkage = 'common'


    def variavelDecl(self, no):
        if(self.scope == "global"): #se e global entao declara global variavel
            if(self.simbolos["global" + "." + no.value]["tipo"] == "inteiro"):
                self.simbolos[self.scope + "." + no.value]["valor"] = ir.GlobalVariable(self.modulo, ir.IntType(32),self.scope + "." + no.value)

            else:
                self.simbolos[self.scope + "." + no.value]["valor"] = ir.GlobalVariable(self.modulo, ir.FloatType(), self.scope + "." + no.value)

        else:#nao e variavel global
            if(self.simbolos[self.scope + "." + no.value]["tipo"] == "inteiro"):
                self.simbolos[self.scope + "." + no.value]["valor"] = self.builder.alloca(ir.IntType(32), self.scope+"."+no.value)
            else:
                self.simbolos[self.scope + "." + no.value]["valor"] = self.builder.alloca(ir.FloatType(), self.scope+"."+no.value)



if __name__ == "__main__":
    import sys

    code = io.open(sys.argv[1], mode="r", encoding="utf-8")
    driver = Generator(code)
