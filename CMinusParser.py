from anytree import Node, RenderTree
from scanner import Scanner
import Grammer
import Diagram


class Parser:
    def __init__(self, scanner: Scanner):
        self.scanner = scanner
        Grammer.initializer()
        Diagram.initializer(Grammer.Non_Terminal.All_Non_Terminals)

    def parse(self):
        start_non_terminal = Grammer.Non_Terminal.get_non_terminal_by_name(Grammer.Non_Terminal.Start_Non_Terminal)
        root = Node(start_non_terminal.name, parnet=None)
        line_number, token = self.scanner.get_next_token()
        self.parse_help(line_number, token, start_non_terminal)

    def parse_help(self, line_number, token, non_terminal: Grammer.Non_Terminal):
        current_token = token
        current_line_number = line_number
        current_state = non_terminal.start_state
        while current_state.type != 'end':
            output_type, output = current_state.get_next_state(current_token)
            if output_type == "Non_Terminal":
                self.parse_help(current_token, output.label, current_line_number)
                current_line_number, current_token = self.scanner.get_next_token()
                current_state = output.destination
            elif output_type == "Terminal":
                current_line_number, current_token = self.scanner.get_next_token()
                current_state = output
            elif output_type == "EPSILON":
                current_state = output
            else:
                error_type = output[0]
                # TODO: handle error
                error_message = generate_panic_mode_error_message(error_type, output[1], current_line_number)
                if error_type == 1:
                    current_line_number, current_token = self.scanner.get_next_token()
                elif error_type == 2:
                    return None
                else:
                    current_state = output[2].destination
        return None


def generate_panic_mode_error_message(type, token, line_number):
    # error type: {1,2,3, 4}. 1,2 and 3 are based on slides and 4 is for Unexpected EOF.
    if type == 1:
        return '#{} : syntax error, illegal {}'.format(line_number, token)
    elif type == 4:
        return '#{} : syntax error, Unexpected EOF'.format(line_number)
    else:
        return '#{} : syntax error, missing {}'.format(line_number, token)


def generate_parse_tree_example():
    root = Node('root', parnet=None)
    a = Node('a', parent=root)
    c = Node('c', parent=a)
    d = Node('d', parent=c)
    k = Node('k', parent=a)
    b = Node('b', parent=root)
    for pre, _, node in RenderTree(root):
        tree_str = u"%s%s" % (pre, node.name)
        print(tree_str.ljust(8))