from anytree import Node, RenderTree


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