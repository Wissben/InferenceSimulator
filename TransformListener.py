from gramListener import gramListener
from Formula import Formula

class TransformListener(gramListener):
    stack = []
    operator = {
        '->': "IMP",
        '^': "AND",
        'v': "OR",
        '<->': "EQ"
    }

    # stack functions

    def pop(self):
        return self.stack.pop()

    def append(self, value):
        # print "appending"+value.toStr()
        self.stack.append(value)

    def getFormula(self):
        if self.stack:
            return self.stack[0]
        return None

    # Listener functions

    def exitForm(self, ctx):
        pass
        if ctx.form() is not None:
            f2 = self.pop()
            f1 = self.pop()
            form = Formula(self.operator[ctx.op2().getText()], f1, f2)
        else:
            form = self.pop()
        self.append(form)

    def exitT(self, ctx):
        if ctx.t() is not None:
            f2 = self.pop()
            f1 = self.pop()
            form = Formula(self.operator[ctx.op1().getText()], f1, f2)
        else:
            form = self.pop()
        self.append(form)

    def exitL(self, ctx):
        if ctx.NOT() is not None:
            form = Formula("NOT",self.pop())
        elif ctx.ID() is not None:
            form = Formula("L", ctx.ID().getText())
        else:
            form = self.pop()
        self.append(form)
