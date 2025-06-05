from collections import OrderedDict

KEYWORDS = {"if", "else", "void", "int", "repeat", "break", "until", "return"}
SYMBOLS = {';', ',', '[', ']', '(', ')', '{', '}', '+', '-', '*', '=', '<', '=='}
WHITESPACE_CHARS = {' ', '\n', '\r', '\t', '\v', '\f'}
INVALID_CHARACTERS = ["!", "#", "@", '%']

def char_class(ch):
    if ch in WHITESPACE_CHARS:
        return 'WHITESPACE'
    elif ch == "^":
        return 'DOLLAR'
    elif ch.isalpha():
        return 'LETTER'
    elif ch.isdigit():
        return 'DIGIT'
    elif ch == '/':
        return 'SLASH'
    elif ch == '*':
        return 'STAR'
    elif ch == '=':
        return 'EQUAL'
    elif ch in SYMBOLS:
        return 'SYMBOL'
    elif ch in INVALID_CHARACTERS:
        return 'INVALID'
    else:
        return 'OTHER'

DFA = {
    'START': {
        'WHITESPACE': 'IN_WHITESPACE',
        'DIGIT': 'IN_NUM',
        'LETTER': 'IN_ID',
        'SLASH': 'SLASH_SEEN',
        'EQUAL': 'EQUAL_SEEN',
        'SYMBOL': 'SYMBOL_DONE',
        'STAR': 'SEEN_STAR',
        'OTHER': 'ERROR'
    },
    'IN_WHITESPACE': {
        'WHITESPACE': 'IN_WHITESPACE',
    },
    'IN_NUM': {
        'DIGIT': 'IN_NUM',
        'LETTER': 'ERROR',
        'INVALID': 'ERROR',
    },
    'IN_ID': {
        'DIGIT': 'IN_ID',
        'LETTER': 'IN_ID',
        'INVALID': 'ERROR',
    },
    'SLASH_SEEN': {
        'STAR': 'IN_COMMENT',
        'SLASH': 'ERROR',
    },
    'IN_COMMENT': {
        'STAR': 'STAR_IN_COMMENT',
        'DIGIT': 'IN_COMMENT',
        'LETTER': 'IN_COMMENT',
        'WHITESPACE': 'IN_COMMENT',
        'OTHER': 'IN_COMMENT',
        'EQUAL': 'IN_COMMENT',
        'SYMBOL': 'IN_COMMENT',
        'SLASH': 'IN_COMMENT',
        'INVALID': 'IN_COMMENT',
        'DOLLAR': 'ERROR',
    },
    'STAR_IN_COMMENT': {
        'STAR': 'STAR_IN_COMMENT',
        'SLASH': 'COMMENT_DONE',
        'OTHER': 'IN_COMMENT',
        'DIGIT': 'IN_COMMENT',
        'LETTER': 'IN_COMMENT',
        'WHITESPACE': 'IN_COMMENT',
        'EQUAL': 'IN_COMMENT',
    },
    'EQUAL_SEEN': {
        'EQUAL': 'EQEQ_DONE',
        'INVALID': 'ERROR',
    },
    'SEEN_STAR': {
        'SLASH': 'ERROR',
        'WHITESPACE': 'SYMBOL_DONE',
        'DIGIT': 'SYMBOL_DONE',
        'LETTER': 'SYMBOL_DONE',
        'EQUAL': 'SYMBOL_DONE',
        'SYMBOL': 'ERROR',

    }
}

FINAL_STATES = {
    'IN_WHITESPACE': 'WHITESPACE',
    'IN_NUM': 'NUM',
    'IN_ID': 'ID',
    'SYMBOL_DONE': 'SYMBOL',
    'EQUAL_SEEN': 'SYMBOL',
    'COMMENT_DONE': 'COMMENT',
    'EQEQ_DONE': 'SYMBOL',
    'ERROR': 'ERROR'
}

def get_next_token(input_str):
    i = 0
    n = len(input_str)

    while i < n:
        state = 'START'
        lexeme = ''
        last_final_state = None
        last_final_lexeme = ''

        while i < n:
            ch = input_str[i]
            cls = char_class(ch)
            next_state = DFA.get(state, {}).get(cls)
            if next_state:
                if state == 'EQUAL_SEEN' and cls != 'EQUAL' and cls !='INVALID':
                    break

                if state == 'SEEN_STAR' and cls != 'SLASH':
                    i -= 1
                    break

                state = next_state
                lexeme += ch
                i += 1
                if state in FINAL_STATES:
                    last_final_state = state
                    last_final_lexeme = lexeme

                if state == 'COMMENT_DONE':
                    break
            else:
                break

        if last_final_state:
            token_type = FINAL_STATES[last_final_state]
            if token_type == 'ID' and last_final_lexeme in KEYWORDS:
                token_type = 'KEYWORD'
            token = (token_type, last_final_lexeme)
        else:
            ch = input_str[i]
            if ch in SYMBOLS:
                token = ("SYMBOL", ch)
            elif ch in WHITESPACE_CHARS:
                token = ("WHITESPACE", ch)
            else:
                token = ("ERROR", ch)
            i += 1

        yield token

def analyze_code(input_code):
    tokens = {1:[]}
    errors = {1:[]}
    symbol_table = OrderedDict()
    comment_open = False
    lineno = 1

    for token in get_next_token(input_code):
        token_type, token_val = token
        if token_type == 'WHITESPACE' and "\n" in token_val:
            lineno += token_val.count("\n")
            tokens[lineno] = []
            errors[lineno] = []
            continue

        if token_type == 'WHITESPACE' or token_type == 'COMMENT':
            continue

        if token_type == 'ID':
            if token_val not in symbol_table:
                symbol_table[token_val] = True


        if token_type == 'ERROR':
            error_msg = (token_val, "Invalid input")
            if token_val.startswith('/*'):
                error_msg = (token_val[:7] + "...", 'Unclosed comment')
            if token_val[-1].isdigit() and any(c.isalpha() for c in token_val):
                error_msg = (token_val, "Invalid number")
            elif token_val == '*/':
                error_msg = (token_val, "Unmatched comment")
            errors[lineno].append(error_msg)
        else:
            tokens[lineno].append((token_type, token_val))

    return tokens, symbol_table, errors, lineno

with open("input.txt", "r") as file:
    example_code = file.read()
    example_code += " ^"

tokens, symbols, lexical_errors, lineno = analyze_code(example_code)


with open("tokens.txt", "w") as f:
    for i in range(1, lineno + 1):
        l = tokens.get(i)
        if l and len(l) != 0:
            f.write(f"{i}.\t{(" ".join(map(str, l))).replace("'", "")}\n")

with open("lexical_errors.txt", "w") as f:
    error = False
    for i in range(1, lineno + 1):
        l = lexical_errors.get(i)
        if i == lineno and l[-1][0] == "^":
            l.pop()

        if l and len(l) != 0:
            error = True
            f.write(f"{i}.\t{(" ".join(map(str, l))).replace("'", "")}\n")

    if error == False:
        f.write(f"There is no lexical error.\n")


with open("symbol_tables.txt", "w") as f:
    idx = 1
    for keyword in sorted(KEYWORDS):
        f.write(f"{idx}.\t{keyword}\n")
        idx += 1
    for identifier in symbols:
        f.write(f"{idx}.\t{identifier}\n")
        idx += 1
