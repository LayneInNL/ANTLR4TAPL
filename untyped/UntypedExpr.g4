grammar UntypedExpr;

TRUE: 'true';
FALSE: 'false';
IF: 'if';
THEN: 'then';
ELSE: 'else';
ZERO: '0';
SUCC: 'succ';
PRED: 'pred';
ISZERO: 'iszero';
LPAREN: '(';
RPAREN: ')';
WS: [ \t\n\r\f]+ -> skip;

term:
	FALSE							# constFalse
	| TRUE							# constTrue
	| ZERO							# constZero
	| IF term THEN term ELSE term	# if
	| SUCC term						# succ
	| PRED term						# pred
	| ISZERO term					# isZero
	| LPAREN term RPAREN			# paren;