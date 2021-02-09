"""
Módulos Collections -  Counter  https://docs.python.org/3/library/collections.html#collections.Counter

Collections -> High-performace Container Datetypes


Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrência desse elemento

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável,  qui usamos uma lista
lista = [1, 1, 1, 3, 3, 4, 5, 5, 12, 13, 12, 13, 15, 98, 25, 99, 60, 60, 32, 12,]

res = Counter(lista)

print(type(res))

print(res)

# Counter({1: 3, 12: 3, 3: 2, 5: 2, 13: 2, 60: 2, 4: 1, 15: 1, 98: 1, 25: 1, 99: 1, 32: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências

# Exemplo 2

from collections import Counter

print(Counter('Geek University'))

#Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
"""

from collections import Counter

# Exemplo 3

texto = """Full Moon é o terceiro álbum de estúdio da cantora e produtora musical norte-americana Brandy Norwood .
A sua produção teve início na metade de 2001, após o término de um hiato longo tomado pela artista depois da 
finalização dos eventos promocionais do seu segundo trabalho de estúdio, Never Say Never (1998).
A vocalista, que passou por um período de hospitalização no final de 1999 como resultado de um colapso nervoso,
revelou ter tido receio de dar arranque ao processo de produção de Full Moon por medo de não conseguir alcançar as
expectativas do público, porém, com a ajuda de Rodney "Darkchild" Jerkins — produtor executivo e maior contribuinte 
na produção e arranjos de Never Say Never — e a equipa do mesmo, conseguiu conceber material suficiente para o disco.
Gravado principalmente no estúdio The Hit Factory em Miami, Flórida, Full Moon foi divulgado internacionalmente em
 meados de 2002 através da editora discográfica Atlantic. O projecto viu Norwood a abandonar a sua imagem de rapariga 
 adolescente em troca de uma mais sensual e adulta, com as letras das canções agora envolvendo metáforas sexuais."""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as  5 palavras com mais ocorrência no texto
print(res.most_common(10 ))
