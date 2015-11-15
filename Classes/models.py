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

class Data(object):
    def __init__(self, dia, mes, ano):
        self.dia= dia
        self.mes= mes
        self.ano= ano

    def imprimir(self):
        print ('%s/%s/%s' %(self.dia, self.mes, self.ano))

class Pessoa(object):
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def calcula_imc(self):
        return self.altura/(self.peso**2)

    def imprime_imc(self):
        print ('Imc de %s: %s' %(self.nome, calcula_imc))
