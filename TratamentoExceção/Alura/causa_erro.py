'''
Todo erro lançado pelo Python carrega informaçoes sobre sua causa e podemos
acessa-la atraves da palavra chave as:
'''

try:
    open('nao_existe.txt', 'r')
    print('arquivo foi aberto')
    arquivo.close()
except IOError as erro:
    print('Deu IOError: %s' %erro)
    
    
