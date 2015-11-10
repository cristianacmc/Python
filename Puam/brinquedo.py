#-*- coding: UTF-8 -*-
#  Na fábrica ABCD Brinquedos o salário líquido de cada funcionário é calculado a partir das seguintes considerações:
# Salário bruto;
# Adicional noturno, se trabalhar a noite, no valor de R$ 300,00;
# Salário família de R$ 90,00 se tiver filhos;
# Auxílio creche de R$ 100,00 para cada filho com idade inferior ou igual a 4 anos;
# Desconto de 17% do INSS para os funcionários que ganham até R$ 1.400,00
# desconto de 21% para os que ganham acima ou igual R$ 1400,00;
# Calcular e exibir o salário líquido.

def calcula_salario(sal_bruto, noturno, filhos, filhos_menores):
    if (sal_bruto < 1400.00):
        sal_liquido = sal_bruto - sal_bruto * 0,17
    else:
        sal_liquido = sal_bruto - sal_bruto * 0,21
    if (noturno == "sim"):
        sal_liquido += 300.00
    if filhos > 0:
        sal_liquido += 90.00
    if filhos_menores > 0:
        sal_liquido += filhos_menores * 100.00
    return sal_liquido

calcula_salario(2000.00, "sim", 2, 0)
