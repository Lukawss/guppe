import exercicios_secao4
from datetime import datetime
from random import randint

hora = datetime.now()
horario = hora.strftime("%d/%m/%Y %H:%M:%S")



log = randint(100000000, 9000000000)
res = str(log)

with open('log.txt','a+') as arquivo:
    arquivo.write(f'Atualização: {exercicios_secao4.var} ')
    arquivo.write(f'Log: {res}')
    arquivo.write(' - ')
    arquivo.write(horario)
    arquivo.write('\n')

