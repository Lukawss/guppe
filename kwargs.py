"""
**kwargs

Poderiamos chamar esse parâmetro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca valores extras em
uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionário.


#Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor.title()}')


cores_favoritas(marcos='verde', julia='amarelo', vanessa='azul')

cores_favoritas(lucas='preto')

#OBS: Os parâmetros *args e **kwargs não são obrigatórios.


# Exemplos mais complexo

def ola(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem é você ...'

print(ola())
print(ola(geek='Python'))

"""
