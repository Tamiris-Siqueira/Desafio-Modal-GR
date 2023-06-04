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

for n in range(20):
    vetor1.append(random.randint(0, 30))

for n in range(20):
    vetor2.append(random.randint(0, 30))

print('Vetor 1: ', vetor1)
print('Vetor 2: ', vetor2)

for num in vetor1:
    if num in vetor2:
        if num not in vetor3:
            vetor3.append(num)

print('Vetor 3: ', vetor3)
