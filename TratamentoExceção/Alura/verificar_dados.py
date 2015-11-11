'''
verificar os parametros do perfil dentro da classe Perfil.
EX. Testar o nome do perfil , verificar o tamanho da string e lançar uma exceçao
caso a mesma tenha menos de 3 caracteres.


class Perfil(object):
   
   def __init__(self, nome, telefone, empresa):
      if(len(nome) < 3):
        raise ValueError('Nome deve ter pelo menos 3 caracteres')
'''
#A classe deve herdar da classe Exception padrão do Python.

class ArgumentoInvalidoError(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def __str__(self):
      return repr(self.mensagem)

raise ArgumentoInvalidoError('Nome deve ter pelo menos 3 caracteres')
