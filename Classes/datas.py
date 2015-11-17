#-*- coding: UTF-8 -*-

class Data(object):
    def __init__(self, dia, mes, ano):
        self.dia= dia
        self.mes= mes
        self.ano= ano

    def imprimir(self):
        print ('%s/%s/%s' %(self.dia, self.mes, self.ano))
