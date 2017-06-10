# 1- Faça um programa que peça dois números inteiros e imprima a soma desses dois números
n1 = int (input ('first number: '))
n2 = int (input ('second number: '))
print ('Total: ',n1 + n2)

2- Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

m = int(input('metros: '))
print ('milimetros: ', m*1000)

# 3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. 
# Calcule o total em segundos.

d = int (input ('days: '))
h = int (input ('hours : '))
m = int (input ('minutes : '))
s = int (input ('seconds : '))

total = d * 24 * 60 * 60 * h * 60 * 60 * m * 60 + s
print total	

# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
# porcentagem do aumento. Exiba o valor do aumento e do novo salário.

s = float (input ('salary: '))
p = float (input ('pay rise percentage: '))
rise = s * p / 100
new = s + rise
print('rise: %.2f' % rise)
print('New salary: %.2f' % new)


# 5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
# preço a pagar.

m = float (input ('preco mercadoria: '))
p = float (input ('percentual desconto: '))
desconto = m * p / 100
novo = m - desconto
print('Desconto: , %.2f' % desconto)
print('Preco a pagar: , %.2f' % novo)

# 6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
# esperada para a viagem.

d = float (input('Distancia em km: '))
v = float (input('Velocidade media em km/h: '))
t = d / v
print ('Estimated time in hours: %.1f' %t)

# 7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
c = float (input('celsius: '))
f = 9 * c/5 +32 
print ('%.2f Fahrenheit' %f)

# 8) Faça agora o contrário, de Fahrenheit para Celsius.
f = float (input('Fahrenheit: '))
c = (f -32) * 5 /9 
print ("%.2f Celsius" %c)

#9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
#usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float (input('km travelled: '))
days = int(input('Days: '))
price = 60*days + km*0.15
print ('%.2f euro' %price)


#10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
#total de dias.

cigarretes = int(input('cigarretes per day: '))
anos = int(input('how many years smoking: '))
total_cigarretes = anos * 365 * cigarretes
days_lost = (total_cigarretes*10)/60/24
print ('you will loose %d days of life' % days_lost)


#11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado
#a um milhão.

print ('number of digits: %d' %len(str(2**100000)))

