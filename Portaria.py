import random

funcionarios = ['doralice', 'juliana', 'joao paulo', 'kleber', 'claudia', 'alessandro', 'amanda', 'edney', 'joseclay',
                'luciana', 'maria aparecida', 'reginaldo', 'geruel', 'gloria', 'fernando']

for f in funcionarios:
    print(f'{f}, ', end=' ')

print(' ')

print(''''\nDeseja Remover Algum Nome?
Se Sim Digite 1
Se Nao Digite 0
''')

a = int(input('Digite o Numero: '))
if a == 1:
    nome = str(input('Digite o Nome Que Voce Quer Remover: '))
    funcionarios.remove(nome)
    a = 30
    while a > 1:
        a = int(input('Digite o Numero: '))
        if a == 1:
            nome = str(input('Digite o Nome Que Voce Quer Remover: '))
            funcionarios.remove(nome)
            a += 1
else:
    print('Ok')

escolha1 = random.choice(funcionarios)
escolha2 = random.choice(funcionarios)
escolha3 = random.choice(funcionarios)
escolha4 = random.choice(funcionarios)
escolha5 = random.choice(funcionarios)
escolha6 = random.choice(funcionarios)
escolha7 = random.choice(funcionarios)
escolha8 = random.choice(funcionarios)
escolha9 = random.choice(funcionarios)
escolha10 = random.choice(funcionarios)
escolha11 = random.choice(funcionarios)

print('*' * 15)
print('1* Andar')
print('*' * 15)

print('Chapelaria = Wilson')
print('P5 = Irineide')
print('P5 = Vera')
print('Catraca = Palmarindo')
print(f'Sub-solo = {escolha1}')

print('*' * 15)
print('2* Andar')
print('*' * 15)

print(f'Quimio = {escolha2}')
print('Docas = Machado')
print('Farmacia = Manuel')
print('Farmacia = Genilson')
print('Farmacia = Ricardo')

print('*' * 15)
print('3* Andar')
print('*' * 15)

print('P9 = Cida')
print('P9 = Sueli')
print(f'P8 = {escolha3}')
print(f'P12 = {escolha4}')
print(f'P13 = {escolha5}')
print(f'P10 = Ivam')
print(f'HD = {escolha6}')

print('*' * 15)
print('4* Andar')
print('*' * 15)

print(f'P11 = {escolha7}')
print(f'P7 = {escolha8}')
print(f'C7 = {escolha9}')
print('Diretoria = Evandro')

print('*' * 15)
print('5* Andar')
print('*' * 15)

print(f'P14 = {escolha10}')

print('*' * 15)
print('Ronda = Marcia')
print(f'Ronda = {escolha11}')
print('*' * 15)

print('*' * 15)
print('Apoio = Tereza')
print('Apoio = Ranie')
print('Apoio = Casa Grande')
print('*' * 15)
