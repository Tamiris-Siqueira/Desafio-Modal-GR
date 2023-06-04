# O colaborador poderá simular um empréstimo de até 2 vezes o valor de seu respectivo salário, 
# desde que esse valor seja múltiplo de 2.
# Notas de maior valor: considerando primeiramente as notas de 100 e 50 reais 
# Notas de menor valor: considerando as notas de 20, 10, 5 e 2 reais.
# Notas meio a meio: metade do valor em notas maiores e a outra metade em notas menores
# Campos para inserção: do nome do colaborador, data de admissão, salário atual, valor de empréstimo, 
# e em seguida, exibir as opções de retirada
# Empréstimo de até 2 vezes o valor de seu respectivo salário, desde que esse valor seja múltiplo de 2.

from datetime import datetime, timedelta

nome = input('Digite o seu nome completo: ')

inputDataAtual = datetime.now()
inputDataAdmissao = input('Digite a data da sua admissão no formato dd/mm/aaaa: ')
dataAdmissao = datetime.strptime(inputDataAdmissao, '%d/%m/%Y')

if dataAdmissao > inputDataAtual or (inputDataAtual - dataAdmissao) < timedelta(days=365*5):
    print('Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.')
    exit()

salario = float(input('Digite o valor do seu salário atual: '))

emprestimo = float(input('Digite o valor do empréstimo: '))
while(emprestimo > salario*2 or emprestimo%2 != 0):
    emprestimo = float(input('Insira um valor válido: '))

print('Digite o número da opção desejada para retirada do valor:')
opcoes = int(input('1 - Notas de maior valor \n2 - Notas de menor valor \n3 - Notas meio a meio\n'))
while(opcoes < 1 or opcoes > 3):
    opcoes = int(input('Escolha uma opção válida: '))

match opcoes:
    case 1:
        print('Notas de 100 e 50')
    case 2:
        print('Notas de 20, 10, 5 e 2')
    case 3:
        print('Metade em notas maiores (100 e 50) e metade em notas menores (20, 10, 5 e 2)')
    case _: 
        print('Erro. Opção inválida!')
        exit()
