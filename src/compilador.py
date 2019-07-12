import sys

from lex import analex

reservada = ["program", "(", ")", ",", ";", "begin", "end", "write", "read"]

def change_state(state : int, token : str, new_mepa) -> int:
    # Confere se começa com program
    if state == 0:
        if token == "program":
            return 1

        else:
            return -1
        
    # Confere se tem um nome após program
    elif state == 1:
        if token not in reservada:
            return 2

        else:
            return -2

    # Confere parenteses inicial
    elif state == 2:
        if token == "(":
            return 3

        else:
            return -3

    # Confere parênteses final
    elif state == 3:
        if token == ")":
            return 4

        elif token not in reservada:
            return 9

        else:
            return -2

    # Confere ponto e vírgula
    elif state == 4:
        if token == ";":
            return 5

        else:
            return -4

    # Confere begin
    elif state == 5:
        if token == "begin":
            new_mepa.write("INPP\n")
            return 6

        else:
            return -5

    # Confere end
    elif state == 6:
        if token == "end":
            return 7

        elif token in reservada[7:]:
            if token == reservada[7]:
                new_mepa.write("IMPR ")

            elif token == reservada[8]:
                new_mepa.write("READ ")

            return 11

        else:
            return -6

    # Confere ponto final
    elif state == 7:
        if token == ".":
            new_mepa.write("PARA")
            return 8

        else:
            return -7

    # Confere fim de arquivo
    elif state == 8:
        return -8

    # Confere argumentos do programa
    elif state == 9:
        if token == ")":
            return 4

        elif token == ",":
            return 10

        else:
            return -3

    # Confere argumentos após a vírgula
    elif state == 10:
        if token not in reservada:
            return 9

        else:
            return -2

    # Confere comandos
    elif state == 11:
        if token == "(":
            return 12

        else:
            return -3

    # Confere argumentos dos comandos
    elif state == 12:
        if int(token):
            new_mepa.write(token + "\n")
            return 13

        else:
            return -999

    # Confere parenteses final do comando
    elif state == 13:
        if token == ")":
            return 14

        else:
            return -3

    # Confere fim de comando
    elif state == 14:
        if token == "end":
            return 7
        elif token == ";":
            return 15
        else:
            return -4

    # Confere próximo comando
    elif state == 15:
        if token in reservada[7:]:
            if token == reservada[7]:
                new_mepa.write("IMPR ")

            elif token == reservada[8]:
                new_mepa.write("READ ")

            return 11
        else:
            return -2

def erro(n :int):
    if n == -1:
        print("Esperava mais de você, comece com 'program'.\n")
    elif n == -2:
        print("Esperava mais de você, identificadores não podem ser palavras reservadas.\n")
    elif n == -3:
        print("Esperava mais de você, falta de parenteses.\n")
    elif n == -4:
        print("Esperava mais de você, faltou um ponto-vírgula.\n")
    elif n == -5:
        print("Esperava mais de você, faltou um begin.\n")
    elif n == -6:
        print("Esperava mais de você, faltou um end.\n")
    elif n == -7:
        print("Esperava mais de você, faltou um ponto-final.\n")
    elif n == -8:
        print("Esperava mais de você, não pode nada após ponto-final.\n")
    else:
        print("Esperava mais de você.\n")


if __name__ == '__main__':
    tokens = analex(sys.argv[1])
    print(tokens)
    # Variável que analisa o estado atual do compilador
    state = 0
    new_mepa = open('exemplo/saida/' + tokens[1] + '.mepa', 'w')
    for token in tokens:
        state = change_state(state, token, new_mepa)
        if state < 0:
            erro(state)
            break