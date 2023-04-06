"""
Ali Razghandi 99109296
Mohammad Mahdi Vahedi 99109314
"""

from scanner import Scanner
import exceptions
from scanner import TokenTypes

scanner = Scanner('input.txt')

token = None
line = 1

symbol_list = set()
lexical_error = dict()
token_list = dict()

while token != 'EOF' and line != -1:  # -1 is returned when there is no more lines to read
    try:
        line, token = scanner.get_next_token()

        if line not in token_list:
            token_list[line] = list()

        token_list[line].append(token)

        if token.token_type == TokenTypes.ID or token.token_type == TokenTypes.KEYWORD:
            symbol_list.add(token.value)

    except exceptions.InvalidInput as e:
        line = e.error_line
        value = e.value
        if line not in lexical_error:
            lexical_error[line] = list()

        lexical_error[line].append(value)

    except exceptions.UnclosedComment as e:
        line = e.error_line
        value = e.value
        if line not in lexical_error:
            lexical_error[line] = list()

        lexical_error[line].append(value)
        break
    except exceptions.UnmatchedComment as e:
        line = e.error_line
        value = e.value
        if line not in lexical_error:
            lexical_error[line] = list()

        lexical_error[line].append(value)
    except exceptions.InvalidNumber as e:
        line = e.error_line
        value = e.value
        if line not in lexical_error:
            lexical_error[line] = list()

        lexical_error[line].append(value)

print(symbol_list)
print(lexical_error)
print(token_list)
