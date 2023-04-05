class InvalidInput(Exception):
    def __init__(self, message, error_line, value=None):
        super().__init__(message)
        self.error_line = error_line
        self.value = value


class UnclosedComment(Exception):
    def __init__(self, message, error_line, value):
        super().__init__(message)
        self.error_line = error_line
        self.value = value


class UnmatchedComment(Exception):
    def __init__(self, message, error_line, value):
        super().__init__(message)
        self.error_line = error_line
        self.value = value


class InvalidNumber(Exception):
    def __init__(self, message, error_line, value=None):
        super().__init__(message)
        self.error_line = error_line
        self.value = value
