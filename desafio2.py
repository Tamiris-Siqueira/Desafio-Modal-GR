# A ModalGR possui um sistema em desenvolvimento sobre notas musicais
# no qual cada uma das 7 notas possui um grau representado por um algarismo romano.
# A ideia é receber um vetor de notas e retornar um outro vetor com os respectivos graus da escala.
# Exibir em tela a saída de acordo com a entrada das notas musicais.

import random

notas = ['Dó', 'Ré', 'Mi', 'Fá', 'Sol', 'Lá', 'Si']
graus = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
entradaNotas = []
saidaGraus = []

#cria uma ordem aleatoria para a lista de notas com um tamanho de 1 a 7
entradaNotas = random.sample(notas, random.randint(1, 7))

print(entradaNotas)

#percorre a lista aleatoria de notas e compara com a lista de notas, 
#caso seja igual, utiliza o indice para atribuir o grau correspondente
for en in entradaNotas:
    for i in range(len(notas)):
        if en == notas[i]:
            saidaGraus.append(graus[i])

print(saidaGraus)