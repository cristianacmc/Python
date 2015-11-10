

class Pessoa(object):
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def imprimeImc(self):
        if (self.altura > 0):
            imc = self.peso / (self.altura ** 2)
            return imc
        else:
            print("A altura tem que ser maior que 0")
