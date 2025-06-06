from parser.parse_table import parsing_table
from scanner.main import get_next_token
from collections import OrderedDict

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


def write_syntax_error(error_token, output_path="syntax_errors.txt"):
    with open(output_path, "w") as f:
        f.write(f"Syntax Error at token '{error_token}'\n")

def write_no_syntax_error(output_path="syntax_errors.txt"):
    with open(output_path, "w") as f:
        f.write("There is no syntax error.\n")

def predictive_parse(input_code):
    root = None
    stack = [("$", root), ("Program", None)]
    token_gen = get_next_token(input_code)
    current_token_type,current_token = next(token_gen)
    with open("parse_tree.txt", "w") as tree_output:
        while stack:
            top, parent_node = stack[-1]
            if top == "epsilon":
                if parent_node:
                    parent_node.add_child(Node("epsilon"))
                stack.pop()
                continue
                        
            if current_token_type == "COMMENT" or current_token_type == "WHITESPACE":
                current_token_type,current_token = next(token_gen)
                continue

            top, parent_node = stack.pop()
            key = str((top, current_token))
            key_with_type = str((top, current_token_type))

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

            elif key in parsing_table or key_with_type in parsing_table:
                production = parsing_table.get(key, parsing_table.get(key_with_type))
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
                write_syntax_error(current_token)

        root.add_child(Node("$"))
        print_tree_to_file(root, tree_output)
        write_no_syntax_error()


with open("input.txt", "r") as file:
    example_code = file.read()
    example_code += "$"



predictive_parse(example_code)