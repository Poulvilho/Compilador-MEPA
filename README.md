# Compilador-MEPA

Trabalho para a disciplina de Compiladores no semestre 2019/1

# Sumário:

1 [Alunos](#-Alunos)<br>
2 [Resumo](#-Resumo)<br>
3 [Estruturação das Pastas](#-Estruturação-das-Pastas)<br>
3.1 [SRC](#-SRC)<br>
3.1.1 [Exemplo](#EXEMPLO)<br>
4 [Funcionamento](#-Funcionamento)

# Alunos

* 16/0031982 - João Pedro Mota Jardim
* 16/0016428 - Paulo Victor de Menezes Lopes

# Resumo

O trabalho consiste em um programa desenvolvido em Python que recebe como argumento um outro programa escrito em Pascal para transformar em um outro programa escrito em Mepa.

# Estruturação das Pastas

## SRC

Local onde se encontram os códigos compiladores e a pasta exemplo para testes.

### EXEMPLO

Local onde se encontram exemplos de programas em Pascal a serem compilados.

# Funcionamento

Para compilar, abra um terminal na raíz da pasta e execute o comando:

  ``` python3 src/compilador.py <arquivo a ser compilado> ```

Se quiser executar em algum dos arquivos de teste, execute o comando:

  ``` python3 src/compilador.py src/exemplo/<arquivo de teste> ```
