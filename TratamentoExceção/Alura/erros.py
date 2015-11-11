try:
    open('não_existe.txt', 'r')
    print('O arquivo foi aberto')
    arquivo.close()
except IOError as erro:
    print ('Deu IOError')



'''
IOError-é um dos erros, uma das exceções, que já vem embutida no Python.
TypeError: ex.[1,2] + (3,4). TypeError: can only concatenate list (not "tuple") to list
As exceçoes acontecem durante a execuçao da aplicaçao.
Ha erros que indicam algum problema na sintaxe. ex:IndentationError: expected an indented block. 
codigo ou mensagens de erros nao devem ser exibidas para o usario, apenas para o desenvolvedor.
try-except - bloco que captura erros durante a execuçao. 
'''

