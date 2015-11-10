#-*- coding: UTF-8 -*-
# Implementar um programa que leia 4 números inteiros:
# Se o último número for negativo calcular e exibir a média dos três primeiros.
# se o último número for positivo calcular e exibir a soma dos quadrados dos três primeiros.
# Se o último número for igual a zero calcular e exibir o produto do primeiro pelo segundo subtraído pelo terceiro.

def avalia_ultimo(a, b, c, d):
    if (d ==0):
        return a * b - c
    if (d >0):
        return a**2 + b**2 + c**2
    else:
        return (a + b + c)/3
