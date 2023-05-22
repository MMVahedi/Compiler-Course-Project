from anytree import Node, RenderTree
from scanner import Scanner

class Parser():
    def __init__(self, scanner: Scanner):
        self.scanner = scanner

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


generate_parse_tree_example()