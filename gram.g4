grammar gram;
WHITESPACE : (' '|'\n'|'\t') -> skip ;
OP : '(';
CP : ')';
IMP : '->';
AND : '^';
OR : 'v';
EQ : '<->';
NOT : '-';
ID : [1-9a-zA-Z]+;


form : form op2 t | t ;
t : t op1 l | l;
l : ID | (OP form CP) | (NOT l);
op1 : AND | OR;
op2 : IMP | EQ;
//op2 : Op2;
//op1 : Op1;