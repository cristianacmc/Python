#-*- coding:UTF8 -*-
#Implementar um programa onde o usuario digita dois números reais e logo após aparece as seguintes opções:
#a) Soma;
#b) Subtração;
#c) Multiplicação;
#d) Divisão;
#Após a escolha da opção, o programa deverá exibir resultado ou a mensagem "Opção inválida"



def calculadora(n1, n2, op):
    if (op=="a"):
        return n1 + n2
    if (op=="b"):
        return n1 - n2
    if (op=="c"):
        return n1 * n2
    if (op=="d"):
        return n1 / n2
    if (op not in "abcd"):
        return "Opção inválida"


n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
op = input("Digite a) Soma b) Subtração c) Multiplicação d) Divisão: ")

x= calculadora(n1, n2, op)
print x
