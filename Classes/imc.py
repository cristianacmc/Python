#-*- coding: UTF-8 -*-

class Pessoa(object):
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def calcula_imc(self):
        return self.altura/(self.peso**2)

    def imprime_imc(self):
        print ('Imc de %s: %s' %(self.nome, calcula_imc))
