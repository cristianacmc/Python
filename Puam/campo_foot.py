
#O dono de um campo de futebol acaba de contratar um analista de sistemas para construir um programa
# o usuario digita a hora inicial de um aluguel do campo e a hora final.
# O programa deverá informar qual o valor a ser pago a partir de um valor por hora informado pelo dono.
# Um jogo poderá começar em um dia e terminar no outro, porém não poderá ter mais do que 24hs

from datetime import datetime

def alugaCampo(h_inicial, h_final, valor_h):
    if (h_final - h_inicial > 24):
        print("não pode ser mais do que 24hs")
    else:


alugaCampo(8, 12, 15)


'''
now = datetime.now()

print '%s:%s:%s' % (now.hour, now.minute, now.second)


 import datetime

 data1 = datetime.date(day=22, month=11, year=2013)

 data2 = datetime.date(day=25, month=3, year=2014)

 data2-data1
 datetime.timedelta(123)

 diferenca = data2-data1

 diferenca.days
 123
 '''
