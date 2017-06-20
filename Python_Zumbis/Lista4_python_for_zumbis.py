'''# 1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
# as funções max e min.

from random import randint
vetor = []
for k in range(10):
    vetor.append(randint(1,100))

maior = menor = vetor[0]
k = 1
while k < 10:
    if vetor[k] > maior:
        maior = vetor[k]
    else:
        menor = vetor[k]
    k = k + 1

print ('Vetor: ', vetor)
print ('Maior: %d' %maior)
print ('Menor: %d' %menor)

        

# 2. Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
# números ímpares na lista IMPAR. Imprima as três listas.

from random import randint
vetor = [randint(1,100) for k in range(20)]
even = [x for x in vetor if x % 2 ==0]
odd = [x for x in vetor if x % 2 !=0]
print ('Vetor: ', vetor)
print ('Even: ', even)
print ('Odd: ', odd)'''
  

# 3. Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um
# terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
# intercalados dos dois outros vetores. Imprima os três vetores.

'''from random import randint
v1 = [randint(1,100) for k in range(10)]
v2 = [randint(1,100) for k in range(10)]
v3 = []
for x in zip(v1,v2):
    v3.extend(list(x))
print ('v1', v1)
print ('v2', v2)
print ('v3', v3)

from random import randint

v1 = []
v2 = []
v3 = []
for k in range (10):
    x = randint(1,100)
    v1.append(x)
    v3.append(x)
    x = randint(1,100)
    v2.append(x)
    v3.append(x)

print('v1: ', v1)
print('v2: ', v2)
print('v3: ', v3)    '''


# 4. Seja o statement sobre diversidade: “The Python Software Foundation and the global Python
# community welcome and encourage participation by everyone. Our community is based on
# mutual respect, tolerance, and encouragement, and we are working to help each other live up
# to these principles. We want our community to be more diverse: whoever you are, and
# whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com
# split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras
# “python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais
# e cuidado com maiúsculas e minúsculas.
text = '''The Python Software Foundation and the global Python
# community welcome and encourage participation by everyone. Our community is based on
# mutual respect, tolerance, and encouragement, and we are working to help each other live up
# to these principles. We want our community to be more diverse: whoever you are, and
# whatever your background, we welcome you.'''.lower()

'''import string
for c in string.punctuation:
    text = text.replace(c, ' ')
resp = []
for p in text.split():
    if p[0] in 'python' or p[-1] in 'python':
        resp.append(p)

print (resp)

import string
for c in string.punctuation:
    text = text.replace(c , ' ')
resp = [p for p in text.split() if p[0] in 'python' or p[-1] in 'python']
print (resp)'''
        

# 5. Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras
# “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para
# minúsculas e de remover antes os caracteres especiais.

text = '''The Python Software Foundation and the global Python
# community welcome and encourage participation by everyone. Our community is based on
# mutual respect, tolerance, and encouragement, and we are working to help each other live up
# to these principles. We want our community to be more diverse: whoever you are, and
# whatever your background, we welcome you.'''.lower()

import string
for c in string.punctuation:
    text = text.replace(c, ' ')

def pitonica(word):
    for w in word:
        if w in 'python':
            return True
    return False

resp = []
for p in text.split():
    if pitonica(p) and len(p)> 4:
        resp.append(p)

print (resp)
print (len(resp))

        
    
