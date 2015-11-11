'''
SE o construtor tem 3 parametros, a lista deve ter a mesma quantidade de
elementos. Se a quantidade nao bate teremos um TypeError. 
'''


from models import *
try:
        arquivo = open('perfis.csv','r')
        valores = arquivo.readline().split(':') #deve ser virgula, para simular o problema
        Perfil(*valores)
        arquivo.close()
except IOError as erro:
        print('Deu IOError %s' % erro)
except  TypeError as erro:
        print('Deu TypeError %s' % erro)
