#-*- coding: UTF-8 -*-


class Perfil(object):
    def __init__(self, nome, email, telefone, empresa):
        self.nome= nome
        self.email = email
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        print ('Nome: %s, Email: %s, Telefone: %s, Empresa: %s' %(self.nome, self.email, self.telefone, self.empresa))

    def curtir(self):
        self.__curtidas += 1

    def obterCurtidas(self):
        return self.__curtidas

class PerfilVip(Perfil):
    def __init__(self, nome, email, telefone, empresa, apelido):

        super(PerfilVip, self).__init__(nome, email, telefone, empresa)
        self.apelido = apelido

    def obter_creditos(self):
        return super(PerfilVip, self).obterCurtidas() *10
