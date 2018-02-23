import FormulaToCNF
#insert here any propositional logic formula
dimacs = FormulaToCNF.getDIMACS("(1 -> 2)",False,False)
print dimacs
file = open("out.cnf", "w")
file.write(dimacs)
file.close()
