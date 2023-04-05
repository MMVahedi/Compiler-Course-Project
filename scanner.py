class Scanner:
    def __init__(self, filename):
        self.filename = filename
        with open(filename) as f:
            self.lines = f.readlines()
        self.lines = list(map(lambda x: x.replace('\n', ''), self.lines))
        self.lineno = 1
        self.line_pointer = 0
        self.symbols = [';', ':', ',', '[', ']', '(', ')', '{', '}', '+', '-', '*', '=', '<']
        self.whitespaces = ['\n', '\r', '\t', '\v', '\f', ' ']
        self.keywords = ['if', 'else', 'void', 'int', 'repeat', 'break', 'until', 'return']

    def get_next_token(self):
        index = self.line_pointer
        line = self.lines[self.lineno - 1]
        current_token = ''
        token_type = None
        find_token = False
        while not find_token:
            if index == len(line):
                self.lineno += 1
                line = self.lines[self.lineno - 1]
                self.line_pointer = 0
                index = 0
            ch = line[index]
            if ch in self.symbols:  # symbol
                token_type = TokenTypes.SYMBOL
                current_token += ch
                index += 1
                if ch == '=' and line[index + 1] == '=':
                    current_token += line[index + 1]
                    index += 1

                find_token = True


            elif ch.isdigit() and (token_type is None or token_type == TokenTypes.NUM):  # number
                if token_type is None:
                    token_type = TokenTypes.NUM
                current_token += ch
                index += 1

                if line[index] in self.whitespaces or \
                        line[index] in self.symbols or \
                        line[index:index + 2] == '/*':

                    find_token = True

            elif ch.isalpha() or (line[index].isdigit() and token_type == TokenTypes.ID):  # id or keyword
                token_type = TokenTypes.ID
                current_token += ch
                index += 1
                if current_token in self.keywords:
                    token_type = TokenTypes.KEYWORD

                if line[index] in self.whitespaces or \
                        line[index] in self.symbols or \
                        line[index :index + 2] == '/*':
                    find_token = True

            elif ch == '/' and line[index + 1] == '*':  # comment
                while line[index:index + 2] != '*/':
                    index += 1
                index += 2
            elif ch in self.whitespaces:  # whitespace
                index += 1
            else:
                # TODO : Error handle con pedarsag
                pass

        self.line_pointer = index
        if index == len(line):
            self.lineno += 1
            self.line_pointer = 0
        return Token(token_type, current_token)


from enum import Enum


class TokenTypes(Enum):
    NUM = 'NUM'
    ID = 'ID'
    KEYWORD = 'KEYWORD'
    SYMBOL = 'SYMBOL'


class Token:
    def __init__(self, token_type: TokenTypes, value):
        self.token_type = token_type
        self.value = value

    def __str__(self):
        return f'({self.token_type.value}, {self.value})'

    def __repr__(self):
        return f'({self.token_type.value}, {self.value})'
