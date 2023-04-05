"""
Ali Razghandi 99109296
Mohammad Mahdi Vahedi 99109314
"""

from scanner import Scanner
import exceptions

scanner = Scanner('input.txt')

token = None
line = 1
while token != 'EOF' and line != -1: # -1 is returned when there is no more lines to read
    try:
        line, token = scanner.get_next_token()
        print(line, token)
    except exceptions.InvalidInput as e:
        print(e.error_line, e)
    except exceptions.UnclosedComment as e:
        print(e.error_line, e)
        break
    except exceptions.UnmatchedComment as e:
        print(e.error_line, e)
    except exceptions.InvalidNumber as e:
        print(e.error_line, e)
