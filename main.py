from subprocess import call

import FormulaToCNF
#insert here any propositional logic formula
dimacs = FormulaToCNF.getDIMACS("(a -> b v c) <-> -b")
print dimacs
file = open("out.cnf", "w")
file.write(dimacs)
file.close()
