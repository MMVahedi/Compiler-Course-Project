class InvalidInput(Exception):
    def __init__(self, message, error_line):
        super().__init__(message)
        self.error_line = error_line


class UnclosedComment(Exception):
    def __init__(self, message, error_line):
        super().__init__(message)
        self.error_line = error_line


class UnmatchedComment(Exception):
    def __init__(self, message, error_line):
        super().__init__(message)
        self.error_line = error_line


class InvalidNumber(Exception):
    def __init__(self, message, error_line):
        super().__init__(message)
        self.error_line = error_line
