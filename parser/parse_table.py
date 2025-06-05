

parsing_table = {
    # Program
    str(("Program", "int")): ["Declaration-list"],
    str(("Program", "void")): ["Declaration-list"],
    str(("Program", "$")): ["Declaration-list"],

    # Declaration-list
    str(("Declaration-list", "int")): ["Declaration", "Declaration-list"],
    str(("Declaration-list", "void")): ["Declaration", "Declaration-list"],
    str(("Declaration-list", "(")): ["epsilon"],
    str(("Declaration-list", "NUM")): ["epsilon"],
    str(("Declaration-list", "ID")): ["epsilon"],
    str(("Declaration-list", "break")): ["epsilon"],
    str(("Declaration-list", ";")): ["epsilon"],
    str(("Declaration-list", "{")): ["epsilon"],
    str(("Declaration-list", "if")): ["epsilon"],
    str(("Declaration-list", "repeat")): ["epsilon"],
    str(("Declaration-list", "return")): ["epsilon"],
    str(("Declaration-list", "}")): ["epsilon"],
    str(("Declaration-list", "$")): ["epsilon"],


    # Declaration
    str(("Declaration", "int")): ["Declaration-initial", "Declaration-prime"],
    str(("Declaration", "void")): ["Declaration-initial", "Declaration-prime"],

    # Declaration-initial
    str(("Declaration-initial", "int")): ["Type-specifier", "ID"],
    str(("Declaration-initial", "void")): ["Type-specifier", "ID"],

    # Declaration-prime
    str(("Declaration-prime", "(")): ["Fun-declaration-prime"],
    str(("Declaration-prime", "[")): ["Var-declaration-prime"],
    str(("Declaration-prime", ";")): ["Var-declaration-prime"],

    # Var-declaration-prime
    str(("Var-declaration-prime", "[")): ["[", "NUM", "]", ";"],
    str(("Var-declaration-prime", ";")): [";"],

    # Fun-declaration-prime
    str(("Fun-declaration-prime", "(")): ["(", "Params", ")", "Compound-stmt"],

    # Type-specifier
    str(("Type-specifier", "int")): ["int"],
    str(("Type-specifier", "void")): ["void"],

    # Params
    str(("Params", "int")): ["int", "ID", "Param-prime", "Param-list"],
    str(("Params", "void")): ["void"],

    # Param-list
    str(("Param-list", ",")): [",", "Param", "Param-list"],
    str(("Param-list", ")")): ["epsilon"],

    # Param
    str(("Param", "int")): ["Declaration-initial", "Param-prime"],
    str(("Param", "void")): ["Declaration-initial", "Param-prime"],

    # Param-prime
    str(("Param-prime", "[")): ["[", "]"],
    str(("Param-prime", ",")): ["epsilon"],
    str(("Param-prime", ")")): ["epsilon"],

    # Compound-stmt
    str(("Compound-stmt", "{")): ["{", "Declaration-list", "Statement-list", "}"],

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

    # Expression-stmt
    str(("Expression-stmt", "(")): ["Expression", ";"],
    str(("Expression-stmt", "NUM")): ["Expression", ";"],
    str(("Expression-stmt", "ID")): ["Expression", ";"],
    str(("Expression-stmt", "break")): ["break", ";"],
    str(("Expression-stmt", ";")): [";"],

    # Selection-stmt
    str(("Selection-stmt", "if")): ["if", "(", "Expression", ")", "Statement", "else", "Statement"],

    # Iteration-stmt
    str(("Iteration-stmt", "repeat")): ["repeat", "Statement", "until", "(", "Expression", ")"],

    # Return-stmt
    str(("Return-stmt", "return")): ["return", "Return-stmt-prime"],

    # Return-stmt-prime
    str(("Return-stmt-prime", ";")): [";"],
    str(("Return-stmt-prime", "(")): ["Expression", ";"],
    str(("Return-stmt-prime", "NUM")): ["Expression", ";"],
    str(("Return-stmt-prime", "ID")): ["Expression", ";"],

    # Expression
    str(("Expression", "(")): ["Simple-expression-zegond"],
    str(("Expression", "NUM")): ["Simple-expression-zegond"],
    str(("Expression", "ID")): ["ID", "B"],

    # B
    str(("B", "=")): ["=", "Expression"],
    str(("B", "[")): ["[", "Expression", "]", "H"],
    str(("B", "(")): ["Simple-expression-prime"],
    str(("B", ";")): ["Simple-expression-prime"],
    str(("B", ")")): ["Simple-expression-prime"],
    str(("B", "+")): ["Simple-expression-prime"],
    str(("B", "-")): ["Simple-expression-prime"],
    str(("B", "*")): ["Simple-expression-prime"],
    str(("B", "<")): ["Simple-expression-prime"],
    str(("B", ">")): ["Simple-expression-prime"],
    str(("B", "==")): ["Simple-expression-prime"],

    # H
    str(("H", "=")): ["=", "Expression"],
    str(("H", "*")): ["G", "D", "C"],
    str(("H", "+")): ["G", "D", "C"],
    str(("H", "-")): ["G", "D", "C"],
    str(("H", "<")): ["G", "D", "C"],
    str(("H", "==")): ["G", "D", "C"],
    str(("H", ";")): ["G", "D", "C"],
    str(("H", ")")): ["G", "D", "C"],

    # Simple-expression-zegond
    str(("Simple-expression-zegond", "(")): ["Additive-expression-zegond", "C"],
    str(("Simple-expression-zegond", "NUM")): ["Additive-expression-zegond", "C"],

    # Simple-expression-prime
    str(("Simple-expression-prime", "(")): ["Additive-expression-prime", "C"],
    str(("Simple-expression-prime", ";")): ["Additive-expression-prime", "C"],
    str(("Simple-expression-prime", ")")): ["Additive-expression-prime", "C"],
    str(("Simple-expression-prime", "+")): ["Additive-expression-prime", "C"],
    str(("Simple-expression-prime", "*")): ["Additive-expression-prime", "C"],
    str(("Simple-expression-prime", "<")): ["Additive-expression-prime", "C"],
    str(("Simple-expression-prime", ">")): ["Additive-expression-prime", "C"],
    str(("Simple-expression-prime", "==")): ["Additive-expression-prime", "C"],

    # C
    str(("C", "<")): ["Relop", "Additive-expression"],
    str(("C", "==")): ["Relop", "Additive-expression"],
    str(("C", ";")): ["epsilon"],
    str(("C", ")")): ["epsilon"],
    str(("C", "]")): ["epsilon"],

    # Relop
    str(("Relop", "<")): ["<"],
    str(("Relop", "==")): ["=="],

    # Additive-expression
    str(("Additive-expression", "(")): ["Term", "D"],
    str(("Additive-expression", "ID")): ["Term", "D"],
    str(("Additive-expression", "NUM")): ["Term", "D"],

    # Additive-expression-prime
    str(("Additive-expression-prime", "(")): ["Term-prime", "D"],
    str(("Additive-expression-prime", "<")): ["Term-prime", "D"],
    str(("Additive-expression-prime", "==")): ["Term-prime", "D"],
    str(("Additive-expression-prime", ";")): ["Term-prime", "D"],
    str(("Additive-expression-prime", ")")): ["Term-prime", "D"],
    str(("Additive-expression-prime", "+")): ["Term-prime", "D"],
    str(("Additive-expression-prime", "*")): ["Term-prime", "D"],

    # Additive-expression-zegond
    str(("Additive-expression-zegond", "(")): ["Term-zegond", "D"],
    str(("Additive-expression-zegond", "NUM")): ["Term-zegond", "D"],

    # D
    str(("D", "+")): ["Addop", "Term", "D"],
    str(("D", "-")): ["Addop", "Term", "D"],
    str(("D", "<")): ["epsilon"],
    str(("D", "==")): ["epsilon"],
    str(("D", ";")): ["epsilon"],
    str(("D", ")")): ["epsilon"],
    str(("D", "]")): ["epsilon"],

    # Addop
    str(("Addop", "+")): ["+"],
    str(("Addop", "-")): ["-"],

    # Term
    str(("Term", "(")): ["Factor", "G"],
    str(("Term", "ID")): ["Factor", "G"],
    str(("Term", "NUM")): ["Factor", "G"],

    # Term-prime
    str(("Term-prime", "(")): ["Factor-prime", "G"],
    str(("Term-prime", "+")): ["Factor-prime", "G"],
    str(("Term-prime", "-")): ["Factor-prime", "G"],
    str(("Term-prime", "<")): ["Factor-prime", "G"],
    str(("Term-prime", "==")): ["Factor-prime", "G"],
    str(("Term-prime", ";")): ["Factor-prime", "G"],
    str(("Term-prime", ")")): ["Factor-prime", "G"],
    str(("Term-prime", "*")): ["Factor-prime", "G"],

    # Term-zegond
    str(("Term-zegond", "(")): ["Factor-zegond", "G"],
    str(("Term-zegond", "NUM")): ["Factor-zegond", "G"],

    # G
    str(("G", "*")): ["*", "Factor", "G"],
    str(("G", "+")): ["epsilon"],
    str(("G", "-")): ["epsilon"],
    str(("G", "<")): ["epsilon"],
    str(("G", "==")): ["epsilon"],
    str(("G", ";")): ["epsilon"],
    str(("G", ")")): ["epsilon"],
    str(("G", "]")): ["epsilon"],

    # Factor
    str(("Factor", "(")): ["(", "Expression", ")"],
    str(("Factor", "ID")): ["ID", "Var-call-prime"],
    str(("Factor", "NUM")): ["NUM"],

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

    # Var-prime
    str(("Var-prime", "[")): ["[", "Expression", "]"],
    str(("Var-prime", "*")): ["epsilon"],
    str(("Var-prime", "+")): ["epsilon"],
    str(("Var-prime", "-")): ["epsilon"],
    str(("Var-prime", "<")): ["epsilon"],
    str(("Var-prime", "==")): ["epsilon"],
    str(("Var-prime", ";")): ["epsilon"],
    str(("Var-prime", ")")): ["epsilon"],

    # Factor-prime
    str(("Factor-prime", "(")): ["(", "Args", ")"],
    str(("Factor-prime", "*")): ["epsilon"],
    str(("Factor-prime", "+")): ["epsilon"],
    str(("Factor-prime", "-")): ["epsilon"],
    str(("Factor-prime", "<")): ["epsilon"],
    str(("Factor-prime", "==")): ["epsilon"],
    str(("Factor-prime", ";")): ["epsilon"],
    str(("Factor-prime", ")")): ["epsilon"],

    # Factor-zegond
    str(("Factor-zegond", "(")): ["(", "Expression", ")"],
    str(("Factor-zegond", "NUM")): ["NUM"],

    # Args
    str(("Args", "(")): ["Arg-list"],
    str(("Args", "NUM")): ["Arg-list"],
    str(("Args", "ID")): ["Arg-list"],
    str(("Args", ")")): ["epsilon"],

    # Arg-list
    str(("Arg-list", "(")): ["Expression", "Arg-list-prime"],
    str(("Arg-list", "NUM")): ["Expression", "Arg-list-prime"],
    str(("Arg-list", "ID")): ["Expression", "Arg-list-prime"],

    # Arg-list-prime
    str(("Arg-list-prime", ",")): [",", "Expression", "Arg-list-prime"],
    str(("Arg-list-prime", ")")): ["epsilon"]
}
