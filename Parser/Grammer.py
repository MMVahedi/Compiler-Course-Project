class Rule:
    All_Rules = []

    def __init__(self, rhs):
        self.rhs = rhs
        Rule.All_Rules.append(self)


class Non_Terminal:
    All_Non_Terminals = {}
    Start_Non_Terminal = 'Program'

    def __init__(self, name):
        self.name = name
        self.rules = []
        self.first = all_first_sets[name]
        self.follow = all_follow_sets[name]
        self.start_state = None
        Non_Terminal.All_Non_Terminals[name] = self

    @classmethod
    def get_non_terminal_by_name(cls, name: str) -> "Non_Terminal":
        if name in cls.All_Non_Terminals.keys():
            return cls.All_Non_Terminals[name]
        raise "invalid non-terminal!"

    def add_rule(self, rule_lst):
        self.rules.append(Rule(rule_lst))


def initializer():
    make_non_terminals()


def make_non_terminals():
    # Non-Terminals
    Program = Non_Terminal('Program')
    Declaration_list = Non_Terminal('Declaration-list')
    Declaration = Non_Terminal('Declaration')
    Declaration_initial = Non_Terminal('Declaration-initial')
    Declaration_prime = Non_Terminal('Declaration-prime')
    Var_declaration_prime = Non_Terminal('Var-declaration-prime')
    Fun_declaration_prime = Non_Terminal('Fun-declaration-prime')
    Type_specifier = Non_Terminal('Type-specifier')
    Params = Non_Terminal('Params')
    Param_list = Non_Terminal('Param-list')
    Param = Non_Terminal('Param')
    Param_prime = Non_Terminal('Param-prime')
    Compound_stmt = Non_Terminal('Compound-stmt')
    Statement_list = Non_Terminal('Statement-list')
    Statement = Non_Terminal('Statement')
    Expression_stmt = Non_Terminal('Expression-stmt')
    Selection_stmt = Non_Terminal('Selection-stmt')
    Iteration_stmt = Non_Terminal('Iteration-stmt')
    Return_stmt = Non_Terminal('Return-stmt')
    Return_stmt_prime = Non_Terminal('Return-stmt-prime')
    Expression = Non_Terminal('Expression')
    B = Non_Terminal('B')
    H = Non_Terminal('H')
    Simple_expression_zegond = Non_Terminal('Simple-expression-zegond')
    Simple_expression_prime = Non_Terminal('Simple-expression-prime')
    C = Non_Terminal('C')
    Relop = Non_Terminal('Relop')
    Additive_expression = Non_Terminal('Additive-expression')
    Additive_expression_prime = Non_Terminal('Additive-expression-prime')
    Additive_expression_zegond = Non_Terminal('Additive-expression-zegond')
    D = Non_Terminal('D')
    Addop = Non_Terminal('Addop')
    Term = Non_Terminal('Term')
    Term_prime = Non_Terminal('Term-prime')
    Term_zegond = Non_Terminal('Term-zegond')
    G = Non_Terminal('G')
    Factor = Non_Terminal('Factor')
    Var_call_prime = Non_Terminal('Var-call-prime')
    Var_prime = Non_Terminal('Var-prime')
    Factor_prime = Non_Terminal('Factor-prime')
    Factor_zegond = Non_Terminal('Factor-zegond')
    Args = Non_Terminal('Args')
    Arg_list = Non_Terminal('Arg-list')
    Arg_list_prime = Non_Terminal('Arg-list-prime')

    # Rules
    Program.add_rule([Declaration_list])
    Declaration_list.add_rule([Declaration, Declaration_list])
    Declaration_list.add_rule([None])
    Declaration.add_rule([Declaration_initial, Declaration_prime])
    Declaration_initial.add_rule(
        [Type_specifier, '#saveType', '#setForceDeclarationFlag', 'ID', '#startNoPush', '#pid', '#endNoPush',
         '#unsetForceDeclarationFlag'])
    Declaration_prime.add_rule([Fun_declaration_prime])
    Declaration_prime.add_rule([Var_declaration_prime, '#zeroInitialize', '#voidCheckThrow'])
    Var_declaration_prime.add_rule([';'])
    Var_declaration_prime.add_rule(['[', 'NUM', '#pnum', ']', '#declareArray', ';'])
    Fun_declaration_prime.add_rule(
        ['(', '#declareFunction', '#openScope', '#setFunctionScopeFlag', Params, ')', Compound_stmt, '#jumpBack'])
    Type_specifier.add_rule(['int'])
    Type_specifier.add_rule(['void', '#voidCheck'])
    Params.add_rule(
        ['int', '#saveType', '#setForceDeclarationFlag', 'ID', '#pid', '#unsetForceDeclarationFlag', Param_prime,
         '#popParam', Param_list])
    Params.add_rule(['void'])
    Param_list.add_rule([',', Param, Param_list])
    Param_list.add_rule([None])
    Param.add_rule([Declaration_initial, Param_prime, "#popParam"])
    Param_prime.add_rule(['[', ']', '#arrayParam'])
    Param_prime.add_rule([None])
    Compound_stmt.add_rule(['{', '#openScope', Declaration_list, Statement_list, '#closeScope', '}'])
    Statement_list.add_rule([Statement, Statement_list])
    Statement_list.add_rule([None])
    Statement.add_rule([Expression_stmt])
    Statement.add_rule([Compound_stmt])
    Statement.add_rule([Selection_stmt])
    Statement.add_rule([Iteration_stmt])
    Statement.add_rule([Return_stmt])
    Expression_stmt.add_rule([Expression, '#pop', ';'])
    Expression_stmt.add_rule(['break', '#break', ';'])
    Expression_stmt.add_rule([';'])
    Selection_stmt.add_rule(
        ['if', '(', '#startRHS', Expression, '#endRHS', ')', '#save', Statement, 'else', '#saveAndJpfFromLastSave',
         Statement, '#jpFromSaved'])
    Iteration_stmt.add_rule(
        ['repeat', '#label', '#startBreakScope', Statement, 'until', '(', '#startRHS', Expression, '#endRHS', ')',
         '#until', '#handleBreaks', ])
    Return_stmt.add_rule(['return', '#startRHS', Return_stmt_prime, '#endRHS', '#jumpBack'])
    Return_stmt_prime.add_rule([';'])
    Return_stmt_prime.add_rule([Expression, '#setReturnValue', ';'])
    Expression.add_rule([Simple_expression_zegond])
    Expression.add_rule(['ID', '#checkDeclaration', '#pid', '#uncheckDeclaration', '#checkType', B])
    B.add_rule(['=', '#startRHS', Expression, '#assign', '#endRHS'])
    B.add_rule(['[', '#startRHS', Expression, '#endRHS', ']', '#array', H])
    B.add_rule([Simple_expression_prime])
    H.add_rule(['=', '#startRHS', Expression, '#assign', '#endRHS', ])
    H.add_rule([G, D, C])
    Simple_expression_zegond.add_rule([Additive_expression_zegond, C])
    Simple_expression_prime.add_rule([Additive_expression_prime, C])
    C.add_rule([Relop, Additive_expression, '#execute'])
    C.add_rule([None])
    Relop.add_rule(['<', '#pushOperation'])
    Relop.add_rule(['==', '#pushOperation'])
    Additive_expression.add_rule([Term, D])
    Additive_expression_prime.add_rule([Term_prime, D])
    Additive_expression_zegond.add_rule([Term_zegond, D])
    D.add_rule([Addop, Term, '#execute', D])
    D.add_rule([None])
    Addop.add_rule(['+', '#pushOperation'])
    Addop.add_rule(['-', '#pushOperation'])
    Term.add_rule([Factor, G])
    Term_prime.add_rule([Factor_prime, G])
    Term_zegond.add_rule([Factor_zegond, G])
    G.add_rule(['*', '#pushOperation', Factor, '#execute', G])
    G.add_rule([None])
    Factor.add_rule(['(', '#startRHS', Expression, '#endRHS', ')'])
    Factor.add_rule(['ID', '#checkDeclaration', '#pid', '#uncheckDeclaration', Var_call_prime])
    Factor.add_rule(['NUM', '#pnum'])
    Var_call_prime.add_rule(['(', '#startArgumentList', Args, '#endArgumentList', ')', '#call'])
    Var_call_prime.add_rule([Var_prime])
    Var_prime.add_rule(['[', '#startRHS', Expression, '#endRHS', ']', '#array'])
    Var_prime.add_rule([None])
    Factor_prime.add_rule(['(', '#startArgumentList', Args, '#endArgumentList', ')', '#call'])
    Factor_prime.add_rule([None])
    Factor_zegond.add_rule(['(', '#startRHS', Expression, '#endRHS', ')'])
    Factor_zegond.add_rule(['NUM', '#pnum'])
    Args.add_rule([Arg_list])
    Args.add_rule([None])
    Arg_list.add_rule([Expression, '#addArgumentCount', Arg_list_prime])
    Arg_list_prime.add_rule([',', Expression, '#addArgumentCount', Arg_list_prime])
    Arg_list_prime.add_rule([None])


# First
all_first_sets = {
    "Program":
        ['int', 'void', None],
    "Declaration-list":
        ['int', 'void', None],
    "Declaration":
        ['int', 'void'],
    "Declaration-initial":
        ['int', 'void'],
    "Declaration-prime":
        [';', '[', '('],
    "Var-declaration-prime":
        [';', '['],
    "Fun-declaration-prime":
        ['('],
    "Type-specifier":
        ['int', 'void'],
    "Params":
        ['int', 'void'],
    "Param-list":
        [',', None],
    "Param":
        ['int', 'void'],
    "Param-prime":
        ['[', None],
    "Compound-stmt":
        ['{'],
    "Statement-list":
        ['ID', ';', 'NUM', '(', '{', 'break', 'if', 'repeat', 'return', None],
    "Statement":
        ['ID', ';', 'NUM', '(', '{', 'break', 'if', 'repeat', 'return'],
    "Expression-stmt":
        ['ID', ';', 'NUM', '(', 'break'],
    "Selection-stmt":
        ['if'],
    "Iteration-stmt":
        ['repeat'],
    "Return-stmt":
        ['return'],
    "Return-stmt-prime":
        ['ID', ';', 'NUM', '('],
    "Expression":
        ['ID', 'NUM', '('],
    "B":
        ['[', '(', '=', '<', '==', '+', '-', '*', None],
    "H":
        ['=', '<', '==', '+', '-', '*', None],
    "Simple-expression-zegond":
        ['(', 'NUM'],
    "Simple-expression-prime":
        ['(', '<', '==', '+', '-', '*', None],
    "C":
        ['<', '==', None],
    "Relop":
        ['<', '=='],
    "Additive-expression":
        ['ID', '(', 'NUM'],
    "Additive-expression-prime":
        ['(', '+', '-', '*', None],
    "Additive-expression-zegond":
        ['(', 'NUM'],
    "D":
        ['+', '-', None],
    "Addop":
        ['+', '-'],
    "Term":
        ['ID', 'NUM', '('],
    "Term-prime":
        ['(', '*', None],
    "Term-zegond":
        ['(', 'NUM'],
    "G":
        ['*', None],
    "Factor":
        ['ID', 'NUM', '('],
    "Var-call-prime":
        ['[', '(', None],
    "Var-prime":
        ['[', None],
    "Factor-prime":
        ['(', None],
    "Factor-zegond":
        ['(', 'NUM'],
    "Args":
        ['ID', '(', 'NUM', None],
    "Arg-list":
        ['ID', '(', 'NUM'],
    "Arg-list-prime":
        [',', None]
}

# Follow
all_follow_sets = {
    "Program":
        ['$'],
    "Declaration-list":
        ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
    "Declaration":
        ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
    "Declaration-initial":
        [';', '[', '(', ')', ','],
    "Declaration-prime":
        ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
    "Var-declaration-prime":
        ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
    "Fun-declaration-prime":
        ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return', '$'],
    "Type-specifier":
        ['ID'],
    "Params":
        [')'],
    "Param-list":
        [')'],
    "Param":
        [')', ','],
    "Param-prime":
        [')', ','],
    "Compound-stmt":
        ['ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return', '$'],
    "Statement-list":
        ['}'],
    "Statement":
        ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
    "Expression-stmt":
        ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
    "Selection-stmt":
        ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
    "Iteration-stmt":
        ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
    "Return-stmt":
        ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
    "Return-stmt-prime":
        ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'else', 'repeat', 'until', 'return'],
    "Expression":
        [';', ']', ')', ','],
    "B":
        [';', ']', ')', ','],
    "H":
        [';', ']', ')', ','],
    "Simple-expression-zegond":
        [';', ']', ')', ','],
    "Simple-expression-prime":
        [';', ']', ')', ','],
    "C":
        [';', ']', ')', ','],
    "Relop":
        ['ID', 'NUM', '('],
    "Additive-expression":
        [';', ']', ')', ','],
    "Additive-expression-prime":
        [';', ']', ')', ',', '<', '=='],
    "Additive-expression-zegond":
        [';', ']', ')', ',', '<', '=='],
    "D":
        [';', ']', ')', ',', '<', '=='],
    "Addop":
        ['ID', 'NUM', '('],
    "Term":
        [';', ']', ')', ',', '<', '==', '+', '-'],
    "Term-prime":
        [';', ']', ')', ',', '<', '==', '+', '-'],
    "Term-zegond":
        [';', ']', ')', ',', '<', '==', '+', '-'],
    "G":
        [';', ']', ')', ',', '<', '==', '+', '-'],
    "Factor":
        [';', ']', ')', ',', '<', '==', '+', '-', '*'],
    "Var-call-prime":
        [';', ']', ')', ',', '<', '==', '+', '-', '*'],
    "Var-prime":
        [';', ']', ')', ',', '<', '==', '+', '-', '*'],
    "Factor-prime":
        [';', ']', ')', ',', '<', '==', '+', '-', '*'],
    "Factor-zegond":
        [';', ']', ')', ',', '<', '==', '+', '-', '*'],
    "Args":
        [')'],
    "Arg-list":
        [')'],
    "Arg-list-prime":
        [')']
}
