"""
Ali Razghandi 99109296
Mohammad Mahdi Vahedi 99109314
"""

from scanner import Scanner
import exceptions
from scanner import TokenTypes


def write_dict_to_txt(dict_to_write, filename, mode):
    with open(filename, 'w') as f:
        if mode == 'tuple' and len(dict_to_write) == 0:
            f.write('There is no lexical error.')
        else:
            for num, element in dict_to_write.items():
                element_string = str(num) + '.' + '\t'
                for item in element:
                    if mode == 'tuple':
                        element_string += '(' + item[0] + ', ' + item[1] + ') '
                    else:
                        element_string += str(item) + ' '
                element_string += '\n'
                f.write(element_string)


def write_list_to_txt(list_to_write, filename):
    with open(filename, 'w') as f:
        for index, element in enumerate(list_to_write):
            element_string = str(index + 1) + '.' + '\t' + element + '\n'
            f.write(element_string)


if __name__ == '__main__':
    scanner = Scanner('input.txt')

    token = None
    line = 1

    symbol_list = ['break', 'else', 'if', 'int', 'repeat', 'return', 'until', 'void']
    lexical_error = dict()
    token_list = dict()

    while token != 'EOF' and line != -1:  # -1 is returned when there is no more lines to read
        try:
            line, token = scanner.get_next_token()

            if line not in token_list and line != -1:
                token_list[line] = list()

            if line != -1:
                token_list[line].append(token)

            if (token.token_type == TokenTypes.ID or token.token_type == TokenTypes.KEYWORD) and \
                    token.value not in symbol_list:
                symbol_list.append(token.value)

        except exceptions.InvalidInput as e:
            line = e.error_line
            value = e.value
            if line not in lexical_error:
                lexical_error[line] = list()

            lexical_error[line].append((value, 'Invalid input'))

        except exceptions.UnclosedComment as e:
            line = e.error_line
            value = e.value
            if line not in lexical_error:
                lexical_error[line] = list()

            lexical_error[line].append((value, 'Unclosed comment'))
            break
        except exceptions.UnmatchedComment as e:
            line = e.error_line
            value = e.value
            if line not in lexical_error:
                lexical_error[line] = list()

            lexical_error[line].append((value, 'Unmatched comment'))
        except exceptions.InvalidNumber as e:
            line = e.error_line
            value = e.value
            if line not in lexical_error:
                lexical_error[line] = list()

            lexical_error[line].append((value, 'Invalid number'))

    write_dict_to_txt(token_list, 'tokens.txt', 'string')
    write_dict_to_txt(lexical_error, 'lexical_errors.txt', 'tuple')
    write_list_to_txt(symbol_list, 'symbol_table.txt')