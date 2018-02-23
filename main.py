from subprocess import call

import FormulaToCNF

dimacs = FormulaToCNF.getDIMACS("(a -> b v c) <-> -b")
print dimacs
file = open("out.cnf", "w")
file.write(dimacs)
file.close()