# Generated from /home/ressay/StudiesTP/TPRC/TP1/gram.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\13/\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write(u"\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write(u"\3\t\3\t\3\n\6\n,\n\n\r\n\16\n-\2\2\13\3\3\5\4\7\5\t")
        buf.write(u"\6\13\7\r\b\17\t\21\n\23\13\3\2\4\4\2\13\f\"\"\5\2\63")
        buf.write(u";C\\c|\2/\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write(u"\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write(u"\2\2\23\3\2\2\2\3\25\3\2\2\2\5\31\3\2\2\2\7\33\3\2\2")
        buf.write(u"\2\t\35\3\2\2\2\13 \3\2\2\2\r\"\3\2\2\2\17$\3\2\2\2\21")
        buf.write(u"(\3\2\2\2\23+\3\2\2\2\25\26\t\2\2\2\26\27\3\2\2\2\27")
        buf.write(u"\30\b\2\2\2\30\4\3\2\2\2\31\32\7*\2\2\32\6\3\2\2\2\33")
        buf.write(u"\34\7+\2\2\34\b\3\2\2\2\35\36\7/\2\2\36\37\7@\2\2\37")
        buf.write(u"\n\3\2\2\2 !\7`\2\2!\f\3\2\2\2\"#\7x\2\2#\16\3\2\2\2")
        buf.write(u"$%\7>\2\2%&\7/\2\2&\'\7@\2\2\'\20\3\2\2\2()\7/\2\2)\22")
        buf.write(u"\3\2\2\2*,\t\3\2\2+*\3\2\2\2,-\3\2\2\2-+\3\2\2\2-.\3")
        buf.write(u"\2\2\2.\24\3\2\2\2\4\2-\3\b\2\2")
        return buf.getvalue()


class gramLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WHITESPACE = 1
    OP = 2
    CP = 3
    IMP = 4
    AND = 5
    OR = 6
    EQ = 7
    NOT = 8
    ID = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'('", u"')'", u"'->'", u"'^'", u"'v'", u"'<->'", u"'-'" ]

    symbolicNames = [ u"<INVALID>",
            u"WHITESPACE", u"OP", u"CP", u"IMP", u"AND", u"OR", u"EQ", u"NOT", 
            u"ID" ]

    ruleNames = [ u"WHITESPACE", u"OP", u"CP", u"IMP", u"AND", u"OR", u"EQ", 
                  u"NOT", u"ID" ]

    grammarFileName = u"gram.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(gramLexer, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


