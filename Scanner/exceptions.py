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


class SemanticException(Exception):
    Messages = [
        "Semantic Error! '{}' is not defined.",
        "Semantic Error! Illegal type of void for '{}'.",
        "Semantic Error! Mismatch in numbers of arguments of '{}'.",
        "Semantic Error! No 'repeat ... until' found for 'break'.",
        "Semantic Error! Type mismatch in operands, Got {} instead of {}.",
        "Semantic Error! Mismatch in type of argument {} of '{}'. Expected '{}' but got '{}' instead."
    ]
    def __init__(self, error_type, argu):
        message = self.Messages[error_type]
        if error_type != 3:
            message = message.format(*argu)
        super().__init__(message)
        self.value = message


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
