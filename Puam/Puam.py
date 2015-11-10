
# ler um numero inteiro e informe se este é par ou impar;
def verifica_mod(numero):
  return numero%2 == 0

# o usuario digita um numero inteiro
# programa informa se é um numero positivo ou negativo
# (incluir o zero como positivo)
def positivo_negativo(x):
    if x>=0:
        print("Numero positivo")
    else:
        print("Numero negativo")



# informe se um numero é multiplo de 3 e de 7
# caso contrario apenas informar que nao é multiplo;
def multiplo(a):
	if (a%3) and (a%7) == 0:
		print("O numero é multiplo de 3 e 7")
	else:
		print("O numero não é multiplo de 3 e 7")


# leia a idade de uma pessoa e informe se esta pessoa pode ou não votar;
def votar(n):
	if n >= 18:
		print ("Pode votar!")
	else:
		print ("Ainda não pode votar!")




def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ()
  test(verifica_mod(0))
  test(verifica_mod(1))
  test(verifica_mod(2))
  test(verifica_mod(10))

  print ()
  print ('Positivo ou negativo')
  test( positivo_negativo(8)


  print ()
  print ('Multiplo de 7 ou 3')
  test(multiplo(21)


  print ()
  test(votar(18)
  test(votar(13)


if __name__ == '__main__':
  main()
