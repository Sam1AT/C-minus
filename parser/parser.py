from parser.parse_table import parsing_table
from scanner.main import get_next_token
from collections import OrderedDict

terminals = [
    "$", "ID", "[", "NUM", "]", ";", "(", ")", "int", "void", ",", "{", "}", 
    "break", "if", "else", "repeat", "until", "return", "=", "<", "==", "+", "−", "*"
]


class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def print_tree_to_file(node, f, prefix=""):
    """
    Print a tree so that each branch uses ├── for non-last children and └── for last children.
    """
    f.write(f"{prefix}{node.symbol}\n")
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        is_last = (i == child_count - 1)
        branch = "└── " if is_last else "├── "

        if is_last:
            next_prefix = prefix + "    "
        else:
            next_prefix = prefix + "│   "

        f.write(f"{prefix}{branch}{child.symbol}\n")
        print_tree_children(child, f, next_prefix)


def print_tree_children(node, f, prefix):
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        is_last = (i == child_count - 1)
        branch = "└── " if is_last else "├── "

        if is_last:
            next_prefix = prefix + "    "
        else:
            next_prefix = prefix + "│   "

        f.write(f"{prefix}{branch}{child.symbol}\n")
        print_tree_children(child, f, next_prefix)


def write_syntax_error(error_token, error_token_type, typ, lineno , output_path="syntax_errors.txt"):
    with open(output_path, "a") as f:
        l =  ['ID', 'NUM', "Params"]
        if error_token_type in l or error_token == None:
            error_token = error_token_type

        if typ == "illegal":
            f.write(f"#{lineno} : syntax error, illegal {error_token}\n")
        elif typ == "missing":
            f.write(f"#{lineno} : syntax error, missing {error_token}\n")
        else:
            f.write(f"#{lineno} : syntax error, Unexpected EOF")

def write_no_syntax_error(output_path="syntax_errors.txt"):
    with open(output_path, "w") as f:
        f.write("There is no syntax error.\n")

def predictive_parse(input_code):
    root = None
    end_of_file_flag = False
    stack = [("$", root), ("Program", None)]
    token_gen = get_next_token(input_code)
    current_token_type,current_token = next(token_gen)
    lineno = 1
    with open("parse_tree.txt", "w") as tree_output:
        while stack:
            try:
                top, parent_node = stack[-1]
                if top == "epsilon":
                    if parent_node:
                        parent_node.add_child(Node("epsilon"))
                    stack.pop()
                    continue

                if current_token_type == "COMMENT" or current_token_type == "WHITESPACE":
                    if current_token_type == "WHITESPACE" and '\n' in current_token:
                        lineno += current_token.count('\n')
                        
                    current_token_type,current_token = next(token_gen)
                    continue

                top, parent_node = stack.pop()
                key = str((top, current_token))
                key_with_type = str((top, current_token_type))
                production = parsing_table.get(key, parsing_table.get(key_with_type))
                print("->", production, current_token, top)
                if top == "$" and current_token == "$":
                    current_node = Node(top)
                    if parent_node:
                        root.add_child(current_node)
                    write_no_syntax_error()

                elif top == current_token or top == current_token_type:
                    if parent_node:
                        leaf = Node(f"({current_token_type}, {current_token})")
                        parent_node.add_child(leaf)
                    current_token_type,current_token = next(token_gen)
                    continue


                elif production and production != ['sync']:
                    if top == "Program":
                        root = Node(top)
                        if parent_node :
                            parent_node.add_child(root)
                        for symbol in reversed(production):
                            stack.append((symbol, root))
                    else:
                        current_node = Node(top)
                        if parent_node :
                            parent_node.add_child(current_node)
                        for symbol in reversed(production):
                            stack.append((symbol, current_node))

                else:
                    print(production, current_token, top, top in terminals)
                    if current_token == '$':
                        current_token_type,current_token = next(token_gen)
                        continue
                    elif production:
                        write_syntax_error(current_token, current_token_type, typ="missing", lineno=lineno)
                    else:
                        if top in terminals:
                            write_syntax_error(None ,top, typ="missing", lineno=lineno)
                        else:
                            write_syntax_error(current_token, current_token_type, typ="illegal", lineno=lineno)
                            current_token_type,current_token = next(token_gen)
                            stack.append((top, parent_node))
            except:
                write_syntax_error(current_token, current_token_type, typ="end_of_file", lineno=lineno)
                end_of_file_flag = True
                break
        
        if not end_of_file_flag:
            root.add_child(Node("$"))
        
        print_tree_to_file(root, tree_output)


with open("input.txt", "r") as file:
    example_code = file.read()
    example_code += "$"

with open("syntax_errors.txt", "w") as f:
            f.write("")

predictive_parse(example_code)