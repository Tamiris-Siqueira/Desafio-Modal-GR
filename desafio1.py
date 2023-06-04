# A ModalGR possui um sistema em desenvolvimento que recebe dois vetores de 20 números inteiros.
# A partir desses valores armazenar em um terceiro vetor números que se repetem.
# Valores repetidos no mesmo vetor não devem ser armazenados no vetor final.
# Caso o vetor ”a” contenha dois ou mais números repetidos 
# no vetor “b” contenha uma ou mais ocorrências desse valor,
# deve-se armazenar apenas uma  ocorrência dessa situação

import random

vetor1 = []
vetor2 = []
vetor3 = []

#criando valores aleatorios de 0 a 30 para uma lista de tamanho 20
for n in range(20):
    vetor1.append(random.randint(0, 30))

for n in range(20):
    vetor2.append(random.randint(0, 30))

print('Vetor 1: ', vetor1)
print('Vetor 2: ', vetor2)

#percorrendo o vetor 1 e verificando se o valor é correspondente com algum do vetor 2
for num in vetor1:
    if num in vetor2:
        #verificando se o valor que existe no vetor 1 e 2 ainda não foi atribuido no vetor 3
        if num not in vetor3:
            vetor3.append(num)

print('Vetor 3: ', vetor3)
