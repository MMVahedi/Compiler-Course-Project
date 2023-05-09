class Non_Terminal:
    All_Non_Terminals = []
    start = None

    def __int__(self, name, rules, first, follow):
        self.name = name
        self.rules = []
        self.first = [all_first_sets[name]]
        self.follow = [all_follow_sets[name]]
        Non_Terminal.All_Non_Terminals[name] = self

    def add_rule(self, rule):
        self.rules.append(rule)


class Rule:
    def __int__(self, rhs):
        self.rhs = rhs

# # Test Functions
# def find_unique_terminals(dict):
#     unique = []
#     for lst in dict.values():
#         for terminal in lst:
#             if not terminal in unique:
#                 unique.append(terminal)
#     return unique
#
#
# def find_unique_non_terminals(dict):
#     unique = []
#     for non_terminal in dict.keys():
#             if not non_terminal in unique:
#                 unique.append(non_terminal)
#     return unique





# First
all_first_sets = {
    "Program":
        ['int', 'void', None],
    "Declaration_list":
        ['int', 'void', None],
    "Declaration":
        ['int', 'void'],
    "Declaration_initial":
        ['int', 'void'],
    "Declaration_prime":
        [';', '[', '('],
    "Var_declaration_prime":
        [';', '['],
    "Fun_declaration_prime":
        ['('],
    "Type_specifier":
        ['int', 'void'],
    "Params":
        ['int', 'void'],
    "Param_list":
        [',', None],
    "Param":
        ['int', 'void'],
    "Param_prime":
        ['[', None],
    "Compound_stmt":
        ['{'],
    "Statement_list":
        ['ID', ';', 'NUM', '(', '{', 'break', 'if', 'repeat', 'return', None],
    "Statement":
        ['ID', ';', 'NUM', '(', '{', 'break', 'if', 'repeat', 'return'],
    "Expression_stmt":
        ['ID', ';', 'NUM', '(', 'break'],
    "Selection_stmt":
        ['if'],
    "Iteration_stmt":
        ['repeat'],
    "Return_stmt":
        ['return'],
    "Return_stmt_prime":
        ['ID', ';', 'NUM', '('],
    "Expression":
        ['ID', 'NUM', '('],
    "B":
        ['[', '(', '=', '<', '==', '+', '-', '*', None],
    "H":
        ['=', '<', '==', '+', '-', '*', None],
    "Simple_expression_zegond":
        ['(', 'NUM'],
    "Simple_expression_prime":
        ['(', '<', '==', '+', '-', '*', None],
    "C":
        ['<', '==', None],
    "Relop":
        ['<', '=='],
    "Additive_expression":
        ['ID', '(', 'NUM'],
    "Additive_expression_prime":
        ['(', '+', '-', '*', None],
    "Additive_expression_zegond":
        ['(', 'NUM'],
    "D":
        ['+', '-', None],
    "Addop":
        ['+', '-'],
    "Term":
        ['ID', 'NUM', '('],
    "Term_prime":
        ['(', '*', None],
    "Term_zegond":
        ['(', 'NUM'],
    "G":
        ['*', None],
    "Factor":
        ['ID', 'NUM', '('],
    "Var_call_prime":
        ['[', '(', None],
    "Var_prime":
        ['[', None],
    "Factor_prime":
        ['(', None],
    "Factor_zegond":
        ['(', 'NUM'],
    "Args":
        ['ID', '(', 'NUM', None],
    "Arg_list":
        ['ID', '(', 'NUM'],
    "Arg_list_prime":
        [',', None]
}

# Follow
all_follow_sets = {
    "Program":
        ['$'],
    "Declaration_list":
        ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
    "Declaration":
        ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
    "Declaration_initial":
        [';', '[', '(', ')', ','],
    "Declaration_prime":
        ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
    "Var_declaration_prime":
        ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
    "Fun_declaration_prime":
        ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
    "Type_specifier":
        ['ID'],
    "Params":
        [')'],
    "Param_list":
        [')'],
    "Param":
        [')', ','],
    "Param_prime":
        [')', ','],
    "Compound_stmt":
        ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return', '$'],
    "Statement_list":
        ['}'],
    "Statement":
        ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
    "Expression_stmt":
        ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
    "Selection_stmt":
        ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
    "Iteration_stmt":
        ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
    "Return_stmt":
        ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
    "Return_stmt_prime":
        ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
    "Expression":
        [';', ']', ')', ','],
    "B":
        [';', ']', ')', ','],
    "H":
        [';', ']', ')', ','],
    "Simple_expression_zegond":
        [';', ']', ')', ','],
    "Simple_expression_prime":
        [';', ']', ')', ','],
    "C":
        [';', ']', ')', ','],
    "Relop":
        ['ID', 'NUM', '('],
    "Additive_expression":
        [';', ']', ')', ','],
    "Additive_expression_prime":
        [';', ']', ')', ',', '<', '=='],
    "Additive_expression_zegond":
        [';', ']', ')', ',', '<', '=='],
    "D":
        [';', ']', ')', ',', '<', '=='],
    "Addop":
        ['ID', 'NUM', '('],
    "Term":
        [';', ']', ')', ',', '<', '==', '+', '-'],
    "Term_prime":
        [';', ']', ')', ',', '<', '==', '+', '-'],
    "Term_zegond":
        [';', ']', ')', ',', '<', '==', '+', '-'],
    "G":
        [';', ']', ')', ',', '<', '==', '+', '-'],
    "Factor":
        [';', ']', ')', ',', '<', '==', '+', '-', '*'],
    "Var_call_prime":
        [';', ']', ')', ',', '<', '==', '+', '-', '*'],
    "Var_prime":
        [';', ']', ')', ',', '<', '==', '+', '-', '*'],
    "Factor_prime":
        [';', ']', ')', ',', '<', '==', '+', '-', '*'],
    "Factor_zegond":
        [';', ']', ')', ',', '<', '==', '+', '-', '*'],
    "Args":
        [')'],
    "Arg_list":
        [')'],
    "Arg_list_prime":
        [')']
}

# TODO: Rules