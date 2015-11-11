'''
O uso de dados de uma fonte externa deve ser verificado pela aplicaçao.
Se em uma linha do arquivo vier faltando um dado, vai gerar erro.
NO arquivo models.py, alterar o metodo gerar_perfis():

for linha in arquivo:
    valores = linha.split(',')

    if (len(valores) is not 3):
         raise ValueError ('Uma linha no arquivo %s deve ter 3 valores' % nome_arquivo)    
    perfis.append(classe(*valores))
'''    
