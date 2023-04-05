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

    def get_next_token(self):
        index = self.line_pointer
        line = self.lines[self.lineno - 1]
        current_token = ''
        token_type = None
        while True:
            ch = line[index]
            if ch in self.symbols:
                pass
            # elif is digit
            # elif is letter
            # elif == '/':
            elif ch in self.whitespaces:
                index += 1
            else:
                # TODO : Error handle con pedarsag
                pass