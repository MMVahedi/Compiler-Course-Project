"""
Ali Razghandi 99109296
Mohammad Mahdi Vahedi 99109314
"""

from scanner import Scanner

scanner = Scanner('input.txt')\

for i in range(100):
    print(scanner.get_next_token())

# token = None
# while(True): #TODO token != EOF
#
#       token = scanner.get_next_token()