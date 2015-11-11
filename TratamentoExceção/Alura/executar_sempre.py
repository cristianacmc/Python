'''
se o arquivo for aberto com a função open e um erro for lançado na função
readline(), o arquivo não sera fechado e isso impedira que outros usuários
ou aplicações consigam interagir com o arquivo.
bloco_finally: codigo que deve ser sempre executado com ou sem exceçao
'''
from models import *
arquivo = None  #inicializar a variavel arquivo
try:
    arquivo = open('Perfis.csv','r')
    valores = arquivo.readline().split(',')
    Perfil(*valores)
except (IOError, TypeError) as erro:
    print("Deu erro % s" %erro)
finally:
    if (arquivo is not None):
        print('fechando arquivo')
        arquivo.close()
    
