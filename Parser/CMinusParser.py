from anytree import Node, RenderTree
from Scanner.scanner import Scanner, Token
from Parser import Grammer
from Parser import Diagram
from CodeGen.codegen import CodeGen
from Scanner.exceptions import SemanticException


class Parser:
    def __init__(self, scanner: Scanner, codegen: CodeGen):
        self.scanner = scanner
        self.code_generator = codegen
        Grammer.initializer()
        Diagram.initializer(Grammer.Non_Terminal.All_Non_Terminals)
        self.current_token = None
        self.previous_token = None
        self.root = Node
        self.semantic_errors = []

    def get_parse_tree(self):
        end = Node('$', parent=self.root)
        tree = ''
        for pre, _, node in RenderTree(self.root):
            tree_str = u"%s%s" % (pre, node.name)
            tree += tree_str.ljust(8) + '\n'
        return tree

    def parse(self):
        start_non_terminal = Grammer.Non_Terminal.get_non_terminal_by_name(Grammer.Non_Terminal.Start_Non_Terminal)
        self.root = Node(start_non_terminal.name)
        # self.previous_token = self.current_token.__copy__
        self.current_token = self.scanner.get_next_token()
        self.parse_help(start_non_terminal, self.root)

    def parse_help(self, non_terminal: Grammer.Non_Terminal, parent):
        current_state = non_terminal.start_state
        while current_state.type != 'end':
            output_type, output = current_state.get_next_state(self.current_token)
            if output_type == "Non_Terminal":
                new_child = Node(output.label.name, parent=parent)
                self.parse_help(output.label, new_child)
                current_state = output.destination
            elif output_type == "Terminal":
                current_state = output[0]
                Node('({}, {})'.format(output[1], output[2]), parent=parent)
                self.previous_token = self.current_token
                self.current_token = self.scanner.get_next_token()
            elif output_type == "EPSILON":
                current_state = output
                Node('epsilon', parent=parent)
            elif output_type == "Action":
                action_symbol = output[1]
                scopes = self.code_generator.symbol_table.scopes
                # print(scopes)
                # print()
                # print(action_symbol)
                # for lst in scopes:
                #     for s in lst:
                #         print(s.lexeme)
                # print()
                try:
                    print(action_symbol)
                    print(self.previous_token.lexeme)
                    print(self.current_token.lexeme)
                    print()
                    self.code_generator.act(action_symbol, self.previous_token, self.current_token)
                except SemanticException as e:
                    # print()
                    # print(e)
                    # print()
                    self.semantic_errors.append(f"#{self.previous_token.lineno}: {e}")
                except:
                    pass
                current_state = output[0]
            elif output_type == 'Skip':
                self.previous_token = self.current_token
                self.current_token = self.scanner.get_next_token()
            else:
                print('error in cminus parser!')
        return None
