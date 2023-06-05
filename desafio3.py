# O colaborador poderá simular um empréstimo de até 2 vezes o valor de seu respectivo salário, 
# desde que esse valor seja múltiplo de 2.
# Notas de maior valor: considerando primeiramente as notas de 100 e 50 reais 
# Notas de menor valor: considerando as notas de 20, 10, 5 e 2 reais.
# Notas meio a meio: metade do valor em notas maiores e a outra metade em notas menores
# Campos para inserção: do nome do colaborador, data de admissão, salário atual, valor de empréstimo, 
# e em seguida, exibir as opções de retirada
# Empréstimo de até 2 vezes o valor de seu respectivo salário, desde que esse valor seja múltiplo de 2.

from datetime import datetime, timedelta
import os

nome = input('Digite o seu nome completo: ')

inputDataAtual = datetime.now()
inputDataAdmissao = input('Digite a data da sua admissão no formato dd/mm/aaaa: ')
#convertendo o string da data no tipo datetime para conseguir comparar com a data atual
dataAdmissao = datetime.strptime(inputDataAdmissao, '%d/%m/%Y')

cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0

metadeValor = 0
i = 0

#confirmando se a data de admissão é maior que a data atual e se funcionario possui mais de 5 anos de casa
if dataAdmissao > inputDataAtual or (inputDataAtual - dataAdmissao) <= timedelta(days=365*5):
    print('Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.')
    exit()

salario = float(input('Digite o valor do seu salário atual: '))

#confirmando se o valor é menor que o dobro do salario e divisivel por 2
emprestimo = float(input('Digite o valor do empréstimo: '))
while(emprestimo > salario*2 or emprestimo%2 != 0):
    emprestimo = float(input('Insira um valor válido: '))

print('Digite o número da opção desejada para retirada do valor:')
opcoes = int(input('1 - Notas de maior valor \n2 - Notas de menor valor \n3 - Notas meio a meio\n'))
while(opcoes < 1 or opcoes > 3):
    opcoes = int(input('Escolha uma opção válida: '))

#limpa o terminal para facilitar visualização
os.system('cls' if os.name == 'nt' else 'clear')

print('Valor do empréstimo: R$', emprestimo)

metadeValor = emprestimo
if opcoes == 3:
    print('Notas meio a meio:')
    emprestimo = metadeValor / 2

#incrementando as variaveis de contagem e decrementando o valor
if opcoes == 1 or opcoes == 3:
    while(emprestimo >= 100):
        cem += 1
        emprestimo -= 100

    while(emprestimo >= 50):
        cinquenta += 1
        emprestimo -= 50

    while(emprestimo >= 20):
        vinte += 1
        emprestimo -= 20

    while(emprestimo >= 10):
        dez += 1
        emprestimo -= 10

    while(emprestimo >= 5):
        cinco += 1
        emprestimo -= 5

    while(emprestimo >= 2):
        dois += 1
        emprestimo -= 2 

if opcoes == 3: 
    emprestimo = metadeValor / 2

if opcoes == 2 or opcoes == 3:
    if opcoes == 3: 
        emprestimo = metadeValor
    while(emprestimo >= 20):
        vinte += 1
        emprestimo -= 20

    while(emprestimo >= 10):
        dez += 1
        emprestimo -= 10

    while(emprestimo >= 5):
        cinco += 1
        emprestimo -= 5

    while(emprestimo >= 2):
        dois += 1
        emprestimo -= 2 

#atribuindo novamente o valor correto do emprestimo caso a variavel tenha sido dividida para a opcao 3
if opcoes == 3:
    emprestimo = metadeValor * 2

emprestimo = metadeValor

#exibindo a mensagem de acordo com as notas utilizadas
if cem != 0:
    print('Notas de maior valor:')
    print(cem, 'x', '100 reais')
if cinquenta != 0:
    print(cinquenta, 'x', '50 reais')
if vinte != 0:
    if opcoes == 2 or opcoes == 3:
        print('Notas de menor valor:')
    print(vinte, 'x', '20 reais')
if dez != 0:
    print(dez, 'x', '10 reais')
if cinco != 0:
    print(cinco, 'x', '5 reais')
if dois != 0:
    print(dois, 'x', '2 reais')