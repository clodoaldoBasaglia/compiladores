from llvmlite import ir

modulo = ir.Module("modulo.bc")
f = open('myMode.ll','w')
f.write(str(modulo))
f.close()
print(modulo)
