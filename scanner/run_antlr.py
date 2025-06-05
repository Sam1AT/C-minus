from antlr4 import FileStream, CommonTokenStream, Token
from CMinus import CMinus


def normalize_token_type(token_type):
    keywords = {'IF', 'ELSE', 'VOID', 'INT', 'REPEAT', 'BREAK', 'UNTIL', 'RETURN'}
    symbols = {
        'EQ', 'ASSIGN', 'LT', 'PLUS', 'MINUS', 'MULT', 'DIV',
        'SEMI', 'COMMA', 'LPAREN', 'RPAREN',
        'LBRACE', 'RBRACE', 'LSQUARE', 'RSQUARE'
    }

    if token_type in keywords:
        return 'KEYWORD'
    elif token_type == 'NUM':
        return 'NUM'
    elif token_type == 'ID':
        return 'ID'
    elif token_type in symbols:
        return 'SYMBOL'
    else:
        return token_type

def main(input_file="input.txt", output_file="ANTLR_p1"):
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = CMinus(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    with open(input_file, encoding='utf-8') as f:
        lines = f.readlines()

    current_line = 1
    line_tokens = []

    with open(output_file, "w", encoding="utf-8") as out:
        for token in token_stream.tokens:
            if token.type == Token.EOF:
                break

            token_line = token.line
            token_text = token.text
            token_type_name = lexer.symbolicNames[token.type]
            mapped_type = normalize_token_type(token_type_name)
            if token_line != current_line:
                if ' '.join(line_tokens) == "":
                    current_line = token_line
                    continue
                out.write(f"{current_line}.\t{' '.join(line_tokens)}\n")
                line_tokens = []
                current_line = token_line

            line_tokens.append(f"({mapped_type}, {token_text})")

        if line_tokens:
            out.write(f"{current_line}.\t{' '.join(line_tokens)}\n")

if __name__ == '__main__':
    main()
