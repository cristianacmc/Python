from models import*
try:
    arquivo = open('perfis.csv', 'r')
    valores = arquivo.readline().split(':')
    Perfil(*valores)
    arquivo.close()
except (IOError, TypeError) as erro:
    print('Deu erro %s' % erro)
    
    
