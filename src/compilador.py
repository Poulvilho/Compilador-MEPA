import sys

from lex import analex

if __name__ == '__main__':
    tokens = analex(sys.argv[1])
    print(tokens)
