import sys

def analex (argv):
    # Read the file and store in var context
    file = open(argv, "r")
    aux = file.read()
    context = []

    for i in aux:
        if i in ['(', ',', ')', ';',
                 '=', '+', '-', '*', '/', '%' # operadores matemáticos
                ]:
            context.append(' ')
            context.append(i)
            context.append(' ')
        else:
            context.append(i)

    context = ''.join(context).split()

    return context

if __name__ == '__main__':
    tokens = analex(sys.argv[1])
    print("Lista de tokens:")
    print(tokens)
    