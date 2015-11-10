

class Perfil(object):
    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        print ("Nome: %s, Telefone: %s, Empresa: %s" % (self.nome, self.telefone, self.empresa))

    def curtir(self):
        self.__curtidas += 1

    def obterCurtidas(self):
        return self.__curtidas


class Perfil_Vip(Perfil):
    def __init__(self, nome, telefone, empresa, apelido):
        super(Perfil_Vip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido

    def obter_creditos(self):
        return super(Perfil_Vip, self).obterCurtidas() * 10.0
