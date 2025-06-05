from parser.parse_table import parsing_table
from scanner.main import get_next_token
from collections import OrderedDict

class Node:
    def __init__(self, symbol, parent=None):
        self.symbol = symbol
        self.children = []
        self.parent = parent
    
    def add_child(self, child):
        self.children.append(child)

    def get_index_in_parent(self):
        if self.parent is None:
            return -1
        return self.parent.children.index(self)

def print_tree_to_file(node, f, prefix=""):
    """
    Print a tree so that each branch uses ├── for non-last children and └── for last children.
    The `prefix` string accumulates the appropriate "│   " or "    " from higher levels.
    """
    f.write(f"{prefix}{node.symbol}\n")

    child_count = len(node.children)
    for i, child in enumerate(node.children):
        is_last = (i == child_count - 1)

        branch = "└── " if is_last else "├── "

        # Compute the prefix to pass down:
        #   - If this child is last, use "    " (spaces) at this level
        #   - Otherwise, use "│   " to keep the vertical bar
        if is_last:
            next_prefix = prefix + "    "
        else:
            next_prefix = prefix + "│   "

        # Print the child’s line (with the branch) and recurse
        f.write(f"{prefix}{branch}{child.symbol}\n")

        # Recurse into children, passing along the new prefix
        print_tree_children(child, f, next_prefix)

def print_tree_children(node, f, prefix):
    """
    Helper to recurse on node.children when we’ve already printed node itself.
    (This separation makes it easier to reuse for both the root and deeper levels.)
    """
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
    root = Node("Program")
    stack = [("$", root), ("Program", None)]
    first_error = True
    last_node = None

    token_gen = get_next_token(input_code)
    current_token_type,current_token = next(token_gen)
    with open("parse_tree.txt", "w", encoding="utf-8") as tree_output:
        while stack:
            top, parent_node = stack[-1]
            if top == "epsilon":
                if parent_node:
                    parent_node.add_child(Node("epsilon", parent_node))
                stack.pop()
                continue
                        
            if current_token_type == "COMMENT" or current_token_type == "WHITESPACE":
                current_token_type,current_token = next(token_gen)
                continue

            top, parent_node = stack.pop()
            key = str((top, current_token))
            key_with_type = str((top, current_token_type))

            if top == "$" and current_token == "$":
                first_error = True
                current_node = Node(top, parent_node)
                last_node = current_node
                if parent_node:
                    parent_node.add_child(current_node)
                write_no_syntax_error()

            elif top == current_token or top == current_token_type:
                first_error = True

                if parent_node:
                    leaf = Node(f"({current_token_type}, {current_token})", parent_node)
                    last_node = leaf
                    parent_node.add_child(leaf)
                current_token_type,current_token = next(token_gen)
                continue

            elif key in parsing_table or key_with_type in parsing_table:
                first_error = True

                production = parsing_table.get(key, parsing_table.get(key_with_type))
                if top == "Program":
                    root = Node(top, parent_node)
                    last_node = root
                    if parent_node :
                        parent_node.add_child(root)
                    for symbol in reversed(production):
                        stack.append((symbol, root))
                else:
                    current_node = Node(top, parent_node)
                    last_node = current_node
                    if parent_node :
                        parent_node.add_child(current_node)
                    for symbol in reversed(production):
                        stack.append((symbol, current_node))
                

            else:
                if first_error:
                    print(last_node.symbol)
                    first_error = False
                    print(f"Syntax error at token '{current_token}'")
                write_syntax_error(current_token)
                current_token_type,current_token = next(token_gen)

        if first_error:
            root.add_child(Node("$", root))
            write_no_syntax_error()
        else:
            node = last_node
            print("last node:", node.symbol)
            while node.parent != None:
                index = node.get_index_in_parent()
                node.parent.children = node.parent.children[:index + 1]
                node = node.parent
            
        print_tree_to_file(root, tree_output)

with open("input.txt", "r") as file:
    example_code = file.read()
    example_code += "$"



predictive_parse(example_code)