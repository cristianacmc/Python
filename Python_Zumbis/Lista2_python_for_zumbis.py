#1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
#um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))
if a >b+c or b > a+c or c > b+a:
    print('Não pode ser triangulo')
    print('Um dos lados e maior que a soma dos dois outros')
elif a == b == c:
    print('Equilatero')
elif a==b or a==c or b==c:
    print('Isosceles')
else:
    print('Escaleno')
    


#2. Determine se um ano é bissexto. Verifique no Google como fazer isso...
a = int (input('Ano: '))
if a % 4 == 0 and (a % 100 !=0 or a % 400 == 0):
    print('Bissexto')
else:
    print('Não é Bissexto')

#3. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de
# seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
# estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você
# faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na
# variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais
# variáveis com o conteúdo ZERO.

p = float(input('Weight: '))
if p > 50:
    e = p-50
    m = e * 4
else:
    m = e = o
    
print('Excess: %d' %e)
print('fine: %.2f' %m)


# 4. Faça um Programa que leia três números e mostre o maior deles.

a = int(input('Number 1: '))
b = int(input('Number 2: '))
c = int(input('Number 3: '))

if a >= b and a >= c:
    print('%d is the biggest number' %a)
elif b >= c:
    print('%d is the biggest number' %b)
else:
    print('%d is the biggest number' %c)

# 5. Faça um Programa que leia três números e mostre o maior e o menor deles.

a = int(input('Number 1: '))
b = int(input('Number 2: '))
c = int(input('Number 3: '))

if a >= b and a >= c:
    print('%d is the biggest number' %a)
elif b >= c:
    print('%d is the biggest number' %b)
else:
    print('%d is the biggest number' %c)

if a <= b and a <= c:
    print('%d is the smallest number' %a)
elif b <= c:
    print('%d is the smallest number' %b)
else:
    print('%d is the smallest number' %c)

# 6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
# e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
# quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
# descontos e o salário líquido, conforme a tabela abaixo:
# a. + Salário Bruto : R$
# b. - IR (11%) : R$
# c. - INSS (8%) : R$
# d. - Sindicato ( 5%) : R$
# e. = Salário Liquido : R$

hour = float(input('hour paid: '))
month = float(input('worked hours: '))
bruto = hour * month
ir = bruto * 0.11
inss = bruto * 0.8
sindi = bruto * 0.5
liquido = bruto - ir - inss - sindi

print('+ Salário Bruto:\t\t R$ %10.2f' %bruto)
print('- IR (11%):\t\t\t R$ %10.2f' %ir)
print('- INSS (8%):\t\t\t R$ %10.2f' %inss)
print('- Sindicato( 5%):\t\t R$ %10.2f' %sindi)
print('= Salário Liquido:\t R$ %10.2f' %liquido)



# 7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
# ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
# compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
m = int(input('Metros: '))
if m % 54 == 0:
    latas = m / 54
else:
    latas = int(m /54) + 1

print('latas: %d' %latas)
print('Preco: %.2f' %(latas*80))
