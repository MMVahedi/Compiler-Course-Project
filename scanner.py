from exceptions import *


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
        if self.lineno - 1 >= len(self.lines):
            return -1, Token(TokenTypes.EOF, 'EOF')
        line = self.lines[self.lineno - 1]
        while len(line) == 0:
            self.lineno += 1
            line = self.lines[self.lineno - 1]
            if self.lineno - 1 > len(self.lines):
                return -1, Token(TokenTypes.EOF, 'EOF')

        current_token = ''
        token_type = None
        find_token = False
        while not find_token:
            ch = line[index]
            if ch in self.symbols and not (ch == '*' and line[index + 1] == '/'):  # symbol
                token_type = TokenTypes.SYMBOL
                current_token += ch
                index += 1
                if ch == '=':
                    next_ch = line[index]
                    if next_ch == '=':
                        current_token += line[index]
                        index += 1

                    elif not (next_ch.isdigit() or (next_ch in self.symbols) or next_ch.isalpha() or (
                            next_ch in self.whitespaces)):
                        index += 1
                        self.line_pointer = index
                        raise InvalidInput('Invalid input', self.lineno, ch + next_ch)

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

            elif (ch.isalpha() and (token_type == TokenTypes.ID or token_type is None)) or \
                    (ch.isdigit() and token_type == TokenTypes.ID):  # id or keyword
                token_type = TokenTypes.ID
                current_token += ch
                index += 1
                if current_token in self.keywords:
                    token_type = TokenTypes.KEYWORD

                if len(line) == index or \
                        line[index] in self.whitespaces or \
                        line[index] in self.symbols or \
                        line[index:index + 2] == '/*':
                    find_token = True

            elif ch == '/' and index + 1 < len(line) and line[index + 1] == '*':  # comment
                dummy = 0
                dummy_comment = ''
                current_line = self.lineno
                while line[index:index + 2] != '*/':
                    if dummy <= 6:
                        dummy_comment += line[index]
                        dummy += 1
                    index += 1
                    if index == len(line):
                        self.lineno += 1
                        line = self.lines[self.lineno - 1] if self.lineno - 1 < len(self.lines) else None
                        self.line_pointer = 0
                        index = 0
                    if self.lineno - 1 >= len(self.lines):
                        # raise Unmatched Comment error here because we have no more lines to read
                        raise UnclosedComment('Unclosed comment', current_line, dummy_comment + '...')

                index += 2
                if index == len(line):
                    self.lineno += 1
                    line = self.lines[self.lineno - 1] if self.lineno - 1 < len(self.lines) else None
                    self.line_pointer = 0
                    index = 0

                if line is None:
                    return -1, Token(TokenTypes.EOF, 'EOF')

            elif ch in self.whitespaces:  # whitespace
                index += 1
                if index == len(line):
                    self.lineno += 1
                    line = self.lines[self.lineno - 1]
                    self.line_pointer = 0
                    index = 0
            else:
                index += 1
                self.line_pointer = index
                current_line = self.lineno
                if index >= len(line):
                    self.lineno += 1
                    self.line_pointer = 0
                if token_type == TokenTypes.NUM and ch.isalpha():
                    raise InvalidNumber('Invalid number', current_line, current_token + ch)
                if ch == '*' and line[index] == '/':
                    index += 1

                    if index >= len(line):
                        self.lineno += 1
                        self.line_pointer = 0
                    raise UnmatchedComment('Unmatched comment', current_line, '*/')

                raise InvalidInput('Invalid input', current_line, current_token + ch)

        self.line_pointer = index
        current_line = self.lineno
        if index == len(line):
            self.lineno += 1
            self.line_pointer = 0

        return current_line, Token(token_type, current_token)


from enum import Enum


class TokenTypes(Enum):
    NUM = 'NUM'
    ID = 'ID'
    KEYWORD = 'KEYWORD'
    SYMBOL = 'SYMBOL'
    EOF = 'EOF'


class Token:
    def __init__(self, token_type: TokenTypes, value):
        self.token_type = token_type
        self.value = value

    def __str__(self):
        return f'({self.token_type.value}, {self.value})'

    def __repr__(self):
        return f'({self.token_type.value}, {self.value})'
