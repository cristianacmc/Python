
'''
Quando trabalhamos com arquivos IO, existe um atalho para a abertura do arquivo
Não precisamos nos preocupar em inicializar a variável arquivo nem fazer o bloco
finally. O Python assume essa responsabilidade 
'''

with open("perfis.csv") as arquivo:
    for linha in arquivo:
        print(linha)
