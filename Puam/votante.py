
#Fazer um programa que leia a idade de uma pessoa e informe:
# Não votante;
# Voto facultativo;
# Voto obrigatório;


def vota(idade):
    if (idade > 18):
        print("Voto obrigatório")
    if(idade < 16):
        print("Não votante")
    else:
        print("Voto facultativo")
