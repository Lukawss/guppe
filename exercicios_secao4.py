lista = [1, 2, 3, 4]

print([x * 10 for x in lista ])

nome = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome('LUCAS','DE S. QUEIROZ'))