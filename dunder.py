"""
Dunder Name e Dunder Main

Dunder -> Double Under

Dunder Name -> __name__

Dunder Main -> __main__

Em Python, são utilizados Dunder para criar funções, atributos, propriedades e etc utilizando o double under para não
gerar conflito com os nomes desse elementos na programação.

Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente o Python atribuirá à variável
__name__ o valor __main__ indicando que este módulo é o módulo de execução principal.

from funcoes_com_parametros import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6]))


"""
import primeiro
import segundo

primeiro.funcao1()
segundo.funcao2()