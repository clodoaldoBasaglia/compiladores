from llvmlite import ir
from sintatica import *
from semantica import *

class Generator():
    def __init__(self, code, optz= True, debug=True):
        s = Semantica(code.read())
        s.lista_declaracoes(self)
        self.tree=s.tree
        self.table = s.simbolos
        self.builder=None
        self.modulo = ir.Module("programaModulo")
        self.scope = "global"
        self.func = None
        self.printf= ir.Function(self.modulo, ir.FunctionType(ir.FloatType(), [ir.FloatType()]), "printf_f")
        self.scanf= ir.Function(self.modulo, ir.FunctionType(ir.FloatType(), [ir.FloatType()]), "scanf_f")
        self.inicioGeneracao(self.tree)
        print(self.modulo)
    def inicioGeneracao(self,node):
        print("oi")
        if self.tree.type == "programa":
            self.programa(self.tree.child[0])
    def lista_declaracoes(self, node):
        print("oi")


if __name__=="__main__":
    import sys,io
    code = io.open(sys.argv[1], mode="r", encoding="utf-8")
    driver = Generator(code)
