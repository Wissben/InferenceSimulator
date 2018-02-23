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

def getDIMACS(string):
    clauses = getCNF(string)
    result = "p cnf " + str(Formula.idfCount) + " " + str(len(clauses)) + "\n"
    for clause in clauses:
        s = ""
        for literal in clause:
            s += literal.getIdf() + " "
        result += s + "0\n"
    return result
