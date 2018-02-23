from antlr4 import *
from gramLexer import gramLexer
from gramParser import gramParser
from TransformListener import TransformListener
from Formula import Formula

def getCNF(string):
    file = open("data.tmp", "w")
    file.write(string)
    file.close()
    input = FileStream("data.tmp")
    lexer = gramLexer(input)
    stream = CommonTokenStream(lexer)
    parser = gramParser(stream)
    transformer = TransformListener()
    parser.addParseListener(transformer)
    parser.form()

    return transformer.getFormula().getClauses()

# header = true to include DIMACS header
# autoIdf = true to auto assign identifiers from 1 to number of variables
# note if autoIdf = false, variables names must be numbers
def getDIMACS(string,header=True,autoIdf=True):
    clauses = getCNF(string)
    result = ""
    if header:
        result = "p cnf " + str(Formula.idfCount) + " " + str(len(clauses)) + "\n"
    for clause in clauses:
        s = ""
        for literal in clause:
            s += literal.getIdf(autoIdf) + " "
        result += s + "0\n"
    return result
