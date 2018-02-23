# Generated from /home/ressay/StudiesTP/TPRC/TP1/gram.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\13\62\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3")
        buf.write(u"\2\3\2\3\2\3\2\3\2\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3 \n\3\f\3\16\3#\13\3\3")
        buf.write(u"\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4,\n\4\3\5\3\5\3\6\3\6\3")
        buf.write(u"\6\2\4\2\4\7\2\4\6\b\n\2\4\3\2\7\b\4\2\6\6\t\t\2\60\2")
        buf.write(u"\f\3\2\2\2\4\30\3\2\2\2\6+\3\2\2\2\b-\3\2\2\2\n/\3\2")
        buf.write(u"\2\2\f\r\b\2\1\2\r\16\5\4\3\2\16\25\3\2\2\2\17\20\f\4")
        buf.write(u"\2\2\20\21\5\n\6\2\21\22\5\4\3\2\22\24\3\2\2\2\23\17")
        buf.write(u"\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26")
        buf.write(u"\3\3\2\2\2\27\25\3\2\2\2\30\31\b\3\1\2\31\32\5\6\4\2")
        buf.write(u"\32!\3\2\2\2\33\34\f\4\2\2\34\35\5\b\5\2\35\36\5\6\4")
        buf.write(u"\2\36 \3\2\2\2\37\33\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"")
        buf.write(u"\3\2\2\2\"\5\3\2\2\2#!\3\2\2\2$,\7\13\2\2%&\7\4\2\2&")
        buf.write(u"\'\5\2\2\2\'(\7\5\2\2(,\3\2\2\2)*\7\n\2\2*,\5\6\4\2+")
        buf.write(u"$\3\2\2\2+%\3\2\2\2+)\3\2\2\2,\7\3\2\2\2-.\t\2\2\2.\t")
        buf.write(u"\3\2\2\2/\60\t\3\2\2\60\13\3\2\2\2\5\25!+")
        return buf.getvalue()


class gramParser ( Parser ):

    grammarFileName = "gram.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"'('", u"')'", u"'->'", 
                     u"'^'", u"'v'", u"'<->'", u"'-'" ]

    symbolicNames = [ u"<INVALID>", u"WHITESPACE", u"OP", u"CP", u"IMP", 
                      u"AND", u"OR", u"EQ", u"NOT", u"ID" ]

    RULE_form = 0
    RULE_t = 1
    RULE_l = 2
    RULE_op1 = 3
    RULE_op2 = 4

    ruleNames =  [ u"form", u"t", u"l", u"op1", u"op2" ]

    EOF = Token.EOF
    WHITESPACE=1
    OP=2
    CP=3
    IMP=4
    AND=5
    OR=6
    EQ=7
    NOT=8
    ID=9

    def __init__(self, input, output=sys.stdout):
        super(gramParser, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class FormContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(gramParser.FormContext, self).__init__(parent, invokingState)
            self.parser = parser

        def t(self):
            return self.getTypedRuleContext(gramParser.TContext,0)


        def form(self):
            return self.getTypedRuleContext(gramParser.FormContext,0)


        def op2(self):
            return self.getTypedRuleContext(gramParser.Op2Context,0)


        def getRuleIndex(self):
            return gramParser.RULE_form

        def enterRule(self, listener):
            if hasattr(listener, "enterForm"):
                listener.enterForm(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitForm"):
                listener.exitForm(self)



    def form(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramParser.FormContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_form, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.t(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramParser.FormContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_form)
                    self.state = 13
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 14
                    self.op2()
                    self.state = 15
                    self.t(0) 
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class TContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(gramParser.TContext, self).__init__(parent, invokingState)
            self.parser = parser

        def l(self):
            return self.getTypedRuleContext(gramParser.LContext,0)


        def t(self):
            return self.getTypedRuleContext(gramParser.TContext,0)


        def op1(self):
            return self.getTypedRuleContext(gramParser.Op1Context,0)


        def getRuleIndex(self):
            return gramParser.RULE_t

        def enterRule(self, listener):
            if hasattr(listener, "enterT"):
                listener.enterT(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitT"):
                listener.exitT(self)



    def t(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramParser.TContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_t, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.l()
            self._ctx.stop = self._input.LT(-1)
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramParser.TContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_t)
                    self.state = 25
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 26
                    self.op1()
                    self.state = 27
                    self.l() 
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class LContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(gramParser.LContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramParser.ID, 0)

        def OP(self):
            return self.getToken(gramParser.OP, 0)

        def form(self):
            return self.getTypedRuleContext(gramParser.FormContext,0)


        def CP(self):
            return self.getToken(gramParser.CP, 0)

        def NOT(self):
            return self.getToken(gramParser.NOT, 0)

        def l(self):
            return self.getTypedRuleContext(gramParser.LContext,0)


        def getRuleIndex(self):
            return gramParser.RULE_l

        def enterRule(self, listener):
            if hasattr(listener, "enterL"):
                listener.enterL(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitL"):
                listener.exitL(self)




    def l(self):

        localctx = gramParser.LContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_l)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [gramParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(gramParser.ID)
                pass
            elif token in [gramParser.OP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(gramParser.OP)
                self.state = 36
                self.form(0)
                self.state = 37
                self.match(gramParser.CP)
                pass
            elif token in [gramParser.NOT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.match(gramParser.NOT)
                self.state = 40
                self.l()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Op1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(gramParser.Op1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(gramParser.AND, 0)

        def OR(self):
            return self.getToken(gramParser.OR, 0)

        def getRuleIndex(self):
            return gramParser.RULE_op1

        def enterRule(self, listener):
            if hasattr(listener, "enterOp1"):
                listener.enterOp1(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOp1"):
                listener.exitOp1(self)




    def op1(self):

        localctx = gramParser.Op1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_op1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not(_la==gramParser.AND or _la==gramParser.OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Op2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(gramParser.Op2Context, self).__init__(parent, invokingState)
            self.parser = parser

        def IMP(self):
            return self.getToken(gramParser.IMP, 0)

        def EQ(self):
            return self.getToken(gramParser.EQ, 0)

        def getRuleIndex(self):
            return gramParser.RULE_op2

        def enterRule(self, listener):
            if hasattr(listener, "enterOp2"):
                listener.enterOp2(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOp2"):
                listener.exitOp2(self)




    def op2(self):

        localctx = gramParser.Op2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_op2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not(_la==gramParser.IMP or _la==gramParser.EQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.form_sempred
        self._predicates[1] = self.t_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def form_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def t_sempred(self, localctx, predIndex):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




