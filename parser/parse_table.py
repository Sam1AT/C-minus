

parsing_table = {
    # Program
    str(("Program", "int")): ["Declaration-list"],
    str(("Program", "void")): ["Declaration-list"],
    str(("Program", "$")): ["Declaration-list"],

    # Declaration-list || }, {, break, ;, if, repeat, return, ID, (, NUM, $
    str(("Declaration-list", "int")): ["Declaration", "Declaration-list"],
    str(("Declaration-list", "void")): ["Declaration", "Declaration-list"],
    str(("Declaration-list", "(")): ["epsilon"],
    str(("Declaration-list", "NUM")): ["epsilon"],
    str(("Declaration-list", ";")): ["epsilon"],
    str(("Declaration-list", "ID")): ["epsilon"],
    str(("Declaration-list", "{")): ["epsilon"],
    str(("Declaration-list", "break")): ["epsilon"],
    str(("Declaration-list", "if")): ["epsilon"],
    str(("Declaration-list", "repeat")): ["epsilon"],
    str(("Declaration-list", "return")): ["epsilon"],
    str(("Declaration-list", "}")): ["epsilon"],
    str(("Declaration-list", "$")): ["epsilon"],

    # Declaration || int, void, }, {, break, ;, if, repeat, return, ID, (, NUM, $
    str(("Declaration", "int")): ["Declaration-initial", "Declaration-prime"],
    str(("Declaration", "void")): ["Declaration-initial", "Declaration-prime"],
    
    str(("Declaration", "}")): ["sync"],
    str(("Declaration", "{")): ["sync"],
    str(("Declaration", "break")): ["sync"],
    str(("Declaration", ";")): ["sync"],
    str(("Declaration", "if")): ["sync"],
    str(("Declaration", "return")): ["sync"],
    str(("Declaration", "ID")): ["sync"],
    str(("Declaration", "(")): ["sync"],
    str(("Declaration", "NUM")): ["sync"],
    str(("Declaration", "$")): ["sync"],

    # Declaration-initial || (, [, ;, ), ,
    str(("Declaration-initial", "int")): ["Type-specifier", "ID"],
    str(("Declaration-initial", "void")): ["Type-specifier", "ID"],

    str(("Declaration", "(")): ["sync"],
    str(("Declaration", "[")): ["sync"],
    str(("Declaration", ")")): ["sync"],
    str(("Declaration", ";")): ["sync"],
    str(("Declaration", ",")): ["sync"],

    # Declaration-prime

    str(("Declaration-prime", "(")): ["Fun-declaration-prime"],
    str(("Declaration-prime", "[")): ["Var-declaration-prime"],
    str(("Declaration-prime", ";")): ["Var-declaration-prime"],

    # int, void, }, {, break, ;, if, repeat, return, ID, (, NUM, $
    str(("Declaration-prime", "int")): ["sync"],
    str(("Declaration-prime", "void")): ["sync"],
    str(("Declaration-prime", "}")): ["sync"],
    str(("Declaration-prime", "{")): ["sync"],
    str(("Declaration-prime", "break")): ["sync"],
    str(("Declaration-prime", "if")): ["sync"],
    str(("Declaration-prime", "repeat")): ["sync"],
    str(("Declaration-prime", "return")): ["sync"],
    str(("Declaration-prime", "ID")): ["sync"],
    str(("Declaration-prime", "NUM")): ["sync"],
    str(("Declaration-prime", "$")): ["sync"],

    # Var-declaration-prime
    str(("Var-declaration-prime", "[")): ["[", "NUM", "]", ";"],
    str(("Var-declaration-prime", ";")): [";"],

    # int, void, }, {, break, ;, if, repeat, return, ID, (, NUM, $
    str(("Var-declaration-prime", "int")): ["sync"],
    str(("Var-declaration-prime", "void")): ["sync"],
    str(("Var-declaration-prime", "}")): ["sync"],
    str(("Var-declaration-prime", "{")): ["sync"],
    str(("Var-declaration-prime", "break")): ["sync"],
    str(("Var-declaration-prime", "if")): ["sync"],
    str(("Var-declaration-prime", "repeat")): ["sync"],
    str(("Var-declaration-prime", "return")): ["sync"],
    str(("Var-declaration-prime", "ID")): ["sync"],
    str(("Var-declaration-prime", "NUM")): ["sync"],
    str(("Var-declaration-prime", "$")): ["sync"],
    str(("Var-declaration-prime", "(")): ["sync"],


    # Fun-declaration-prime
    str(("Fun-declaration-prime", "(")): ["(", "Params", ")", "Compound-stmt"],

    # int, void, }, {, break, ;, if, repeat, return, ID, (, NUM, $
    str(("Fun-declaration-prime", "int")): ["sync"],
    str(("Fun-declaration-prime", "void")): ["sync"],
    str(("Fun-declaration-prime", "}")): ["sync"],
    str(("Fun-declaration-prime", "{")): ["sync"],
    str(("Fun-declaration-prime", "break")): ["sync"],
    str(("Fun-declaration-prime", "if")): ["sync"],
    str(("Fun-declaration-prime", "repeat")): ["sync"],
    str(("Fun-declaration-prime", "return")): ["sync"],
    str(("Fun-declaration-prime", "ID")): ["sync"],
    str(("Fun-declaration-prime", "NUM")): ["sync"],
    str(("Fun-declaration-prime", "$")): ["sync"],
    str(("Fun-declaration-prime", ";")): ["sync"],

    # Type-specifier
    str(("Type-specifier", "int")): ["int"],
    str(("Type-specifier", "void")): ["void"],

    # ID
    str(("Type-specifier", "ID")): ["sync"],

    # Params
    str(("Params", "int")): ["int", "ID", "Param-prime", "Param-list"],
    str(("Params", "void")): ["void"],

    # )
    str(("Params", ")")): ["sync"],

    # Param-list
    str(("Param-list", ",")): [",", "Param", "Param-list"],
    str(("Param-list", ")")): ["epsilon"],

    # Param
    str(("Param", "int")): ["Declaration-initial", "Param-prime"],
    str(("Param", "void")): ["Declaration-initial", "Param-prime"],

    # ), ,
    str(("Param", ")")): ["sync"],
    str(("Param", ",")): ["sync"],

    # Param-prime
    str(("Param-prime", "[")): ["[", "]"],
    str(("Param-prime", ",")): ["epsilon"],
    str(("Param-prime", ")")): ["epsilon"],

    
    # Compound-stmt
    str(("Compound-stmt", "{")): ["{", "Declaration-list", "Statement-list", "}"],

    # int, void, }, {, break, ;, if, repeat, return, ID, (, NUM, $, else, until
    str(("Compound-stmt", "int")): ["sync"],
    str(("Compound-stmt", "void")): ["sync"],
    str(("Compound-stmt", "}")): ["sync"],
    str(("Compound-stmt", "break")): ["sync"],
    str(("Compound-stmt", ";")): ["sync"],
    str(("Compound-stmt", "if")): ["sync"],
    str(("Compound-stmt", "repeat")): ["sync"],
    str(("Compound-stmt", "return")): ["sync"],
    str(("Compound-stmt", "ID")): ["sync"],
    str(("Compound-stmt", "(")): ["sync"],
    str(("Compound-stmt", "NUM")): ["sync"],
    str(("Compound-stmt", "else")): ["sync"],
    str(("Compound-stmt", "until")): ["sync"],
    str(("Compound-stmt", "$")): ["sync"],

    # Statement-list
    str(("Statement-list", "(")): ["Statement", "Statement-list"],
    str(("Statement-list", "NUM")): ["Statement", "Statement-list"],
    str(("Statement-list", "ID")): ["Statement", "Statement-list"],
    str(("Statement-list", "break")): ["Statement", "Statement-list"],
    str(("Statement-list", ";")): ["Statement", "Statement-list"],
    str(("Statement-list", "{")): ["Statement", "Statement-list"],
    str(("Statement-list", "if")): ["Statement", "Statement-list"],
    str(("Statement-list", "repeat")): ["Statement", "Statement-list"],
    str(("Statement-list", "return")): ["Statement", "Statement-list"],
    str(("Statement-list", "}")): ["epsilon"],

    
    # Statement
    str(("Statement", "(")): ["Expression-stmt"],
    str(("Statement", "NUM")): ["Expression-stmt"],
    str(("Statement", "ID")): ["Expression-stmt"],
    str(("Statement", "break")): ["Expression-stmt"],
    str(("Statement", ";")): ["Expression-stmt"],
    str(("Statement", "{")): ["Compound-stmt"],
    str(("Statement", "if")): ["Selection-stmt"],
    str(("Statement", "repeat")): ["Iteration-stmt"],
    str(("Statement", "return")): ["Return-stmt"],

    # }, {, break, ;, if, repeat, return, ID, (, NUM, else, until
    str(("Statement", "}")): ["sync"],
    str(("Statement", "else")): ["sync"],
    str(("Statement", "until")): ["sync"],

    # Expression-stmt
    str(("Expression-stmt", "(")): ["Expression", ";"],
    str(("Expression-stmt", "NUM")): ["Expression", ";"],
    str(("Expression-stmt", "ID")): ["Expression", ";"],
    str(("Expression-stmt", "break")): ["break", ";"],
    str(("Expression-stmt", ";")): [";"],

    # }, {, break, ;, if, repeat, return, ID, (, NUM, else, until
    str(("Expression-stmt", "}")): ["sync"],
    str(("Expression-stmt", "{")): ["sync"],
    str(("Expression-stmt", "if")): ["sync"],
    str(("Expression-stmt", "repeat")): ["sync"],
    str(("Expression-stmt", "return")): ["sync"],
    str(("Expression-stmt", "else")): ["sync"],
    str(("Expression-stmt", "until")): ["sync"],


    # Selection-stmt
    str(("Selection-stmt", "if")): ["if", "(", "Expression", ")", "Statement", "else", "Statement"],

    # }, {, break, ;, if, repeat, return, ID, (, NUM, else, until
    str(("Selection-stmt", "}")): ["sync"],
    str(("Selection-stmt", "{")): ["sync"],
    str(("Selection-stmt", "break")): ["sync"],
    str(("Selection-stmt", ";")): ["sync"],   
    str(("Selection-stmt", "repeat")): ["sync"], 
    str(("Selection-stmt", "return")): ["sync"], 
    str(("Selection-stmt", "ID")): ["sync"], 
    str(("Selection-stmt", "(")): ["sync"], 
    str(("Selection-stmt", "NUM")): ["sync"], 
    str(("Selection-stmt", "else")): ["sync"], 
    str(("Selection-stmt", "until")): ["sync"], 


    # Iteration-stmt
    str(("Iteration-stmt", "repeat")): ["repeat", "Statement", "until", "(", "Expression", ")"],
    
    # }, {, break, ;, if, repeat, return, ID, (, NUM, else, until
    str(("Iteration-stmt", "}")): ["sync"],
    str(("Iteration-stmt", "{")): ["sync"],
    str(("Iteration-stmt", "break")): ["sync"],
    str(("Iteration-stmt", ";")): ["sync"],   
    str(("Iteration-stmt", "if")): ["sync"], 
    str(("Iteration-stmt", "return")): ["sync"], 
    str(("Iteration-stmt", "ID")): ["sync"], 
    str(("Iteration-stmt", "(")): ["sync"], 
    str(("Iteration-stmt", "NUM")): ["sync"], 
    str(("Iteration-stmt", "else")): ["sync"], 
    str(("Iteration-stmt", "until")): ["sync"], 


    # Return-stmt
    str(("Return-stmt", "return")): ["return", "Return-stmt-prime"],

    # }, {, break, ;, if, repeat, return, ID, (, NUM, else, until
    str(("Return-stmt", "}")): ["sync"],
    str(("Return-stmt", "{")): ["sync"],
    str(("Return-stmt", "break")): ["sync"],
    str(("Return-stmt", ";")): ["sync"],
    str(("Return-stmt", "if")): ["sync"],
    str(("Return-stmt", "repeat")): ["sync"],
    str(("Return-stmt", "ID")): ["sync"],
    str(("Return-stmt", "(")): ["sync"],
    str(("Return-stmt", "NUM")): ["sync"],
    str(("Return-stmt", "else")): ["sync"],
    str(("Return-stmt", "until")): ["sync"],

    # Return-stmt-prime
    str(("Return-stmt-prime", ";")): [";"],
    str(("Return-stmt-prime", "(")): ["Expression", ";"],
    str(("Return-stmt-prime", "NUM")): ["Expression", ";"],
    str(("Return-stmt-prime", "ID")): ["Expression", ";"],

    # }, {, break, ;, if, repeat, return, ID, (, NUM, else, until
    str(("Return-stmt-prime", "}")): ["sync"],
    str(("Return-stmt-prime", "{")): ["sync"],
    str(("Return-stmt-prime", "break")): ["sync"],
    str(("Return-stmt-prime", "if")): ["sync"],
    str(("Return-stmt-prime", "repeat")): ["sync"],
    str(("Return-stmt-prime", "return")): ["sync"],
    str(("Return-stmt-prime", "else")): ["sync"],
    str(("Return-stmt-prime", "until")): ["sync"],
    

    # Expression
    str(("Expression", "ID")): ["ID", "B"],
    str(("Expression", "(")): ["Simple-expression-zegond"],
    str(("Expression", "NUM")): ["Simple-expression-zegond"],

    # ;, ), ], ,
    str(("Expression", ";")): ["sync"],
    str(("Expression", ")")): ["sync"],
    str(("Expression", "]")): ["sync"],
    str(("Expression", ",")): ["sync"],

    # B
    str(("B", "=")): ["=", "Expression"],
    str(("B", "[")): ["[", "Expression", "]", "H"],
    str(("B", "]")): ["Simple-expression-prime"],
    str(("B", "(")): ["Simple-expression-prime"],
    str(("B", ")")): ["Simple-expression-prime"],
    str(("B", "*")): ["Simple-expression-prime"],
    str(("B", "+")): ["Simple-expression-prime"],
    str(("B", "-")): ["Simple-expression-prime"],
    str(("B", "<")): ["Simple-expression-prime"],
    str(("B", "==")): ["Simple-expression-prime"],
    str(("B", ";")): ["Simple-expression-prime"],
    str(("B", ",")): ["Simple-expression-prime"],

    # ;, ), ], ,

    # H
    str(("H", "=")): ["=", "Expression"],
    str(("H", "*")): ["G", "D", "C"],
    str(("H", "+")): ["G", "D", "C"],
    str(("H", "-")): ["G", "D", "C"],
    str(("H", "<")): ["G", "D", "C"],
    str(("H", "==")): ["G", "D", "C"],
    str(("H", ";")): ["G", "D", "C"],
    str(("H", ")")): ["G", "D", "C"],
    str(("H", "]")): ["G", "D", "C"],
    str(("H", ",")): ["G", "D", "C"],

    # ;, ), ], ,

    # Simple-expression-zegond
    str(("Simple-expression-zegond", "(")): ["Additive-expression-zegond", "C"],
    str(("Simple-expression-zegond", "NUM")): ["Additive-expression-zegond", "C"],

    # ;, ), ], ,
    str(("Simple-expression-zegond", ";")): ["sync"],
    str(("Simple-expression-zegond", ")")): ["sync"],
    str(("Simple-expression-zegond", "]")): ["sync"],
    str(("Simple-expression-zegond", ",")): ["sync"],

    # Simple-expression-prime
    str(("Simple-expression-prime", "(")): ["Additive-expression-prime", "C"],
    str(("Simple-expression-prime", "*")): ["Additive-expression-prime", "C"],
    str(("Simple-expression-prime", "+")): ["Additive-expression-prime", "C"],
    str(("Simple-expression-prime", "-")): ["Additive-expression-prime", "C"],
    str(("Simple-expression-prime", "<")): ["Additive-expression-prime", "C"],
    str(("Simple-expression-prime", "==")): ["Additive-expression-prime", "C"],
    str(("Simple-expression-prime", ";")): ["Additive-expression-prime", "C"],
    str(("Simple-expression-prime", ")")): ["Additive-expression-prime", "C"],
    str(("Simple-expression-prime", "]")): ["Additive-expression-prime", "C"],
    str(("Simple-expression-prime", ",")): ["Additive-expression-prime", "C"],

    # C
    str(("C", "<")): ["Relop", "Additive-expression"],
    str(("C", "==")): ["Relop", "Additive-expression"],
    str(("C", ";")): ["epsilon"],
    str(("C", ")")): ["epsilon"],
    str(("C", "]")): ["epsilon"],
    str(("C", ",")): ["epsilon"],

    
    # Relop
    str(("Relop", "<")): ["<"],
    str(("Relop", "==")): ["=="],

    # (, ID, NUM
    str(("Relop", "(")): ["sync"],
    str(("Relop", "ID")): ["sync"],
    str(("Relop", "NUM")): ["sync"],

    # Additive-expression
    str(("Additive-expression", "(")): ["Term", "D"],
    str(("Additive-expression", "ID")): ["Term", "D"],
    str(("Additive-expression", "NUM")): ["Term", "D"],

    # ;, ), ], ,
    str(("Additive-expression", ";")): ["sync"],
    str(("Additive-expression", ")")): ["sync"],
    str(("Additive-expression", "]")): ["sync"],
    str(("Additive-expression", ",")): ["sync"],

    # Additive-expression-prime
    str(("Additive-expression-prime", "(")): ["Term-prime", "D"],
    str(("Additive-expression-prime", "*")): ["Term-prime", "D"],
    str(("Additive-expression-prime", "+")): ["Term-prime", "D"],
    str(("Additive-expression-prime", "-")): ["Term-prime", "D"],
    str(("Additive-expression-prime", "<")): ["Term-prime", "D"],
    str(("Additive-expression-prime", "==")): ["Term-prime", "D"],
    str(("Additive-expression-prime", ";")): ["Term-prime", "D"],
    str(("Additive-expression-prime", ")")): ["Term-prime", "D"],
    str(("Additive-expression-prime", "]")): ["Term-prime", "D"],
    str(("Additive-expression-prime", ",")): ["Term-prime", "D"],
    
    # Additive-expression-zegond
    str(("Additive-expression-zegond", "(")): ["Term-zegond", "D"],
    str(("Additive-expression-zegond", "NUM")): ["Term-zegond", "D"],

    # ;, ), <, ==, ], ,
    str(("Additive-expression-zegond", ";")): ["sync"],
    str(("Additive-expression-zegond", ")")): ["sync"],
    str(("Additive-expression-zegond", "]")): ["sync"],
    str(("Additive-expression-zegond", "<")): ["sync"],
    str(("Additive-expression-zegond", "==")): ["sync"],
    str(("Additive-expression-zegond", ",")): ["sync"],

    # D
    str(("D", "+")): ["Addop", "Term", "D"],
    str(("D", "-")): ["Addop", "Term", "D"],
    str(("D", ";")): ["epsilon"],
    str(("D", ")")): ["epsilon"],
    str(("D", "]")): ["epsilon"],
    str(("D", "<")): ["epsilon"],
    str(("D", "==")): ["epsilon"],
    str(("D", ",")): ["epsilon"],
    


    # Addop
    str(("Addop", "+")): ["+"],
    str(("Addop", "-")): ["-"],

    # (, ID, NUM
    str(("Addop", "(")): ["sync"],
    str(("Addop", "ID")): ["sync"],
    str(("Addop", "NUM")): ["sync"],

    # Term
    str(("Term", "(")): ["Factor", "G"],
    str(("Term", "ID")): ["Factor", "G"],
    str(("Term", "NUM")): ["Factor", "G"],

    # ;, ), +, −, <, ==, ], ,
    str(("Term", ";")): ["sync"],
    str(("Term", ")")): ["sync"],
    str(("Term", "+")): ["sync"],
    str(("Term", "-")): ["sync"],
    str(("Term", "<")): ["sync"],
    str(("Term", "==")): ["sync"],
    str(("Term", "]")): ["sync"],
    str(("Term", ",")): ["sync"],

    # Term-prime
    str(("Term-prime", "(")): ["Factor-prime", "G"],
    str(("Term-prime", "*")): ["Factor-prime", "G"],
    str(("Term-prime", "+")): ["Factor-prime", "G"],
    str(("Term-prime", "-")): ["Factor-prime", "G"],
    str(("Term-prime", "<")): ["Factor-prime", "G"],
    str(("Term-prime", "==")): ["Factor-prime", "G"],
    str(("Term-prime", ";")): ["Factor-prime", "G"],
    str(("Term-prime", ")")): ["Factor-prime", "G"],
    str(("Term-prime", "]")): ["Factor-prime", "G"],
    str(("Term-prime", ",")): ["Factor-prime", "G"],

    
    # Term-zegond
    str(("Term-zegond", "(")): ["Factor-zegond", "G"],
    str(("Term-zegond", "NUM")): ["Factor-zegond", "G"],

    # ;, ), <, ==, +, −, ], ,
    str(("Term-zegond", ";")): ["sync"],
    str(("Term-zegond", ")")): ["sync"],
    str(("Term-zegond", "]")): ["sync"],
    str(("Term-zegond", "<")): ["sync"],
    str(("Term-zegond", "==")): ["sync"],
    str(("Term-zegond", "+")): ["sync"],
    str(("Term-zegond", "-")): ["sync"],
    str(("Term-zegond", ",")): ["sync"],
    
    # G
    str(("G", "*")): ["*", "Factor", "G"],
    str(("G", ";")): ["epsilon"],
    str(("G", ")")): ["epsilon"],
    str(("G", "]")): ["epsilon"],
    str(("G", "+")): ["epsilon"],
    str(("G", "-")): ["epsilon"],
    str(("G", "<")): ["epsilon"],
    str(("G", "==")): ["epsilon"],
    str(("G", ",")): ["epsilon"],

    
    # Factor
    str(("Factor", "(")): ["(", "Expression", ")"],
    str(("Factor", "ID")): ["ID", "Var-call-prime"],
    str(("Factor", "NUM")): ["NUM"],

    # ;, ), +, −, <, ==, *, ], ,
    str(("Factor", ";")): ["sync"],
    str(("Factor", ")")): ["sync"],
    str(("Factor", "+")): ["sync"],
    str(("Factor", "-")): ["sync"],
    str(("Factor", "<")): ["sync"],
    str(("Factor", "==")): ["sync"],
    str(("Factor", "*")): ["sync"],
    str(("Factor", "]")): ["sync"],
    str(("Factor", ",")): ["sync"],

    # Var-call-prime
    str(("Var-call-prime", "(")): ["(", "Args", ")"],
    str(("Var-call-prime", "[")): ["Var-prime"],
    str(("Var-call-prime", "*")): ["Var-prime"],
    str(("Var-call-prime", "+")): ["Var-prime"],
    str(("Var-call-prime", "-")): ["Var-prime"],
    str(("Var-call-prime", "<")): ["Var-prime"],
    str(("Var-call-prime", "==")): ["Var-prime"],
    str(("Var-call-prime", ";")): ["Var-prime"],
    str(("Var-call-prime", ")")): ["Var-prime"],
    str(("Var-call-prime", "]")): ["Var-prime"],
    str(("Var-call-prime", ",")): ["Var-prime"],
    
    # Var-prime
    str(("Var-prime", "[")): ["[", "Expression", "]"],
    str(("Var-prime", "*")): ["epsilon"],
    str(("Var-prime", "+")): ["epsilon"],
    str(("Var-prime", "-")): ["epsilon"],
    str(("Var-prime", "<")): ["epsilon"],
    str(("Var-prime", "==")): ["epsilon"],
    str(("Var-prime", ";")): ["epsilon"],
    str(("Var-prime", ")")): ["epsilon"],
    str(("Var-prime", "]")): ["epsilon"],
    str(("Var-prime", ",")): ["epsilon"],


    # Factor-prime
    str(("Factor-prime", "(")): ["(", "Args", ")"],
    str(("Factor-prime", "*")): ["epsilon"],
    str(("Factor-prime", "+")): ["epsilon"],
    str(("Factor-prime", "-")): ["epsilon"],
    str(("Factor-prime", "<")): ["epsilon"],
    str(("Factor-prime", "==")): ["epsilon"],
    str(("Factor-prime", ";")): ["epsilon"],
    str(("Factor-prime", ")")): ["epsilon"],
    str(("Factor-prime", "]")): ["epsilon"],
    str(("Factor-prime", ",")): ["epsilon"],

    # Factor-zegond
    str(("Factor-zegond", "(")): ["(", "Expression", ")"],
    str(("Factor-zegond", "NUM")): ["NUM"],

    # ;, ), <, ==, +, −, *, ], ,
    str(("Factor-zegond", ";")): ["sync"],
    str(("Factor-zegond", ")")): ["sync"],
    str(("Factor-zegond", "]")): ["sync"],
    str(("Factor-zegond", "<")): ["sync"],
    str(("Factor-zegond", "==")): ["sync"],
    str(("Factor-zegond", "+")): ["sync"],
    str(("Factor-zegond", "-")): ["sync"],
    str(("Factor-zegond", "*")): ["sync"],
    str(("Factor-zegond", ",")): ["sync"],
   
    # Args
    str(("Args", "(")): ["Arg-list"],
    str(("Args", "NUM")): ["Arg-list"],
    str(("Args", "ID")): ["Arg-list"],
    str(("Args", ")")): ["epsilon"],

    # Arg-list
    str(("Arg-list", "(")): ["Expression", "Arg-list-prime"],
    str(("Arg-list", "NUM")): ["Expression", "Arg-list-prime"],
    str(("Arg-list", "ID")): ["Expression", "Arg-list-prime"],

    # )
    str(("Arg-list", ")")): ["sync"],

    # Arg-list-prime
    str(("Arg-list-prime", ",")): [",", "Expression", "Arg-list-prime"],
    str(("Arg-list-prime", ")")): ["epsilon"]

    
}