from CMinusParser import Parser
from scanner import Scanner

parser = Parser(Scanner('input.txt'))
parser.parse()
parse_tree = parser.get_parse_tree()
with open('parse_tree.txt', 'w', encoding="utf-8") as f:
    f.write(parse_tree)
with open('syntax_errors.txt', 'w') as f:
    if len(parser.errors) == 0:
        f.write('There is no syntax error.')
    else:
        for error in parser.errors:
            f.write(error + '\n')
