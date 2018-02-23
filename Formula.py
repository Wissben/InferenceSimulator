class Formula:
    # type can be
    # "AND" => P and Q
    # "OR" => P or Q
    # "IMP" => P -> Q
    # "EQ" => P <-> Q
    # "NOT" => not P
    # "L" => literal P
    __type = ""
    __P = None
    __Q = None
    __idf = 0
    idfCount = 0
    idfs = {}

    def __init__(self, t, p, q=None):
        self.__type = t
        self.__P = p
        self.__Q = q
        if t == "L":
            if p not in Formula.idfs:
                Formula.idfCount += 1
                self.__idf = Formula.idfCount
                Formula.idfs[p] = self.__idf
            else:
                self.__idf = Formula.idfs[p]

    def getP(self):
        return self.__P

    def getQ(self):
        return self.__Q

    def isLiteral(self):
        return self.__type == "L"

    def getType(self):
        return self.__type

    def getIdf(self,auto=True):
        if self.isLiteral():
            if auto:
                return str(self.__idf)
            else:
                return self.getP()
        elif self.getType() == "NOT":
            if auto:
                return "-"+str(self.getP().getIdf())
            else:
                return "-"+self.getP().getP()
        else:
            return 0

    @staticmethod
    def Not(formula):
        return Formula("NOT", formula)

    def getClauses(self):
        self.convertToAO()
        clauses = self.convert()
        toRemove = []
        for i in range(0, len(clauses)):
            end = False
            for j in range(0, len(clauses[i])):
                for k in range(j+1, len(clauses[i])):
                    if clauses[i][j].isComplement(clauses[i][k]):
                        toRemove.append(clauses[i])
                        end = True
                        break
                if end:
                    break
        for rem in toRemove:
            clauses.remove(rem)

        # eliminate duplicate literal in clause
        for i in range(0, len(clauses)):
            toRemove = []
            for j in range(0, len(clauses[i])):
                for k in range(j+1, len(clauses[i])):
                    if clauses[i][j].toStr() == clauses[i][k].toStr():
                        toRemove.append(clauses[i][j])
                        break
            for rem in toRemove:
                clauses[i].remove(rem)

        # eliminate clause1 in clause2
        toRemove = []
        for i in range(0, len(clauses)):


            for j in range(0, len(clauses)):
                if i != j:
                    allFound = True
                    for literal1 in clauses[i]:
                        found = False
                        for literal2 in clauses[j]:
                            if literal1.toStr() == literal2.toStr():
                                found = True
                                break
                        if not found:
                            allFound = False
                            break
                    if allFound:
                        toRemove.append(clauses[i])
                        break

        for rem in toRemove:
            clauses.remove(rem)

        return clauses

    def isComplement(self,literal):
        this = self.toStr()
        lit = literal.toStr()
        notThis = "not("+this+")"
        notLiteral = "not("+lit+")"
        return this == notLiteral or lit == notThis

# toStr functions

    def toStr(self):
        func = getattr(self, "toStr" + self.__type)
        return func()

    def toStrAND(self):
        return "("+self.getP().toStr()+"^"+self.getQ().toStr()+")"

    def toStrOR(self):
        return "(" + self.getP().toStr() + "v" + self.getQ().toStr() + ")"

    def toStrIMP(self):
        return "(" + self.getP().toStr() + "->" + self.getQ().toStr() + ")"

    def toStrEQ(self):
        return "(" + self.getP().toStr() + "<->" + self.getQ().toStr() + ")"

    def toStrNOT(self):
        return "not(" + self.getP().toStr() + ")"

    def toStrL(self):
        return self.getP()

# Convert functions:

    def convert(self):
        func = getattr(self, "convert"+self.__type)
        return func()

    def convertAND(self):
        clauses1 = self.getP().convert()
        clauses2 = self.getQ().convert()
        return clauses1 + clauses2

    def convertOR(self):
        result = []
        clauses1 = self.getP().convert()
        clauses2 = self.getQ().convert()
        for clause1 in clauses1:
            for clause2 in clauses2:
                clauses = clause2 + clause1
                result.append(clauses)

        return result

    def convertNOT(self):
        p = self.getP()
        if p.isLiteral(): # case literal we return not literal
            return [[self]]
        elif p.getType() == "NOT": # case not not p we return p
            return p.getP().convert()
        elif p.getType() == "OR": # case or we return (not p ^ not q)
            return Formula("AND", Formula.Not(p.getP()), Formula.Not(p.getQ())).convert()
        else: # case and we return (not p v not q)
            return Formula("OR", Formula.Not(p.getP()), Formula.Not(p.getQ())).convert()

    # return clause containing only the literal
    def convertL(self):
        return [[self]]


# convert all implications and equivalences Functions:

    def convertToAO(self):
        func = getattr(self, "convertToAO" + self.__type)
        return func()

    def convertToAOAND(self):
        self.getP().convertToAO()
        self.getQ().convertToAO()
        return self

    def convertToAOOR(self):
        self.getP().convertToAO()
        self.getQ().convertToAO()
        return self

    def convertToAOIMP(self):
        # we return (not p or q)
        self.__P = Formula.Not(self.getP()).convertToAO()
        self.getQ().convertToAO()
        self.__type = "OR"
        return self

    def convertToAOEQ(self):
        self.getP().convertToAO()
        self.getQ().convertToAO()
        # p and q
        f1 = Formula("AND", self.getP(), self.getQ())
        # not p and not q
        f2 = Formula("AND", Formula.Not(self.getP()).convertToAO(),
                            Formula.Not(self.getQ()).convertToAO())
        self.__P = f1
        self.__Q = f2
        # we change equivalence to ((p and q) or (not p and not q))
        self.__type = "OR"
        return self

    def convertToAONOT(self):
        self.__P = self.getP().convertToAO()
        return self

    def convertToAOL(self):
        return self
