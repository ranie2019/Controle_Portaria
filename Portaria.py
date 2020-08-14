import random

funcionarios = ['doralice', 'juliana', 'joao paulo', 'kleber', 'claudia', 'alessandro', 'amanda', 'edney', 'joseclay','luciana', 'maria aparecida', 'reginaldo', 'geruel',
                'gloria', 'fernando', 'Wilson', 'irineide', 'palmarindo', 'vera', 'machado', 'manuel', 'genilson', 'ricardo', 'cida', 'sueli', 'ivam', 'evandro']

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
escolha12 = random.choice(funcionarios)
escolha13 = random.choice(funcionarios)
escolha14 = random.choice(funcionarios)
escolha15 = random.choice(funcionarios)
escolha16 = random.choice(funcionarios)
escolha17 = random.choice(funcionarios)
escolha18 = random.choice(funcionarios)
escolha19 = random.choice(funcionarios)
escolha20 = random.choice(funcionarios)
escolha21 = random.choice(funcionarios)
escolha22 = random.choice(funcionarios)

print('*' * 15)
print('1* Andar')
print('*' * 15)

print(f'Chapelaria = {escolha1}')
print(f'P5 = {escolha2}')
print(f'P5 = {escolha3}')
print(f'Catraca = {escolha4}')
print(f'Sub-solo = {escolha5}')

print('*' * 15)
print('2* Andar')
print('*' * 15)

print(f'Quimio = {escolha6}')
print(f'Docas = {escolha7}')
print(f'Farmacia = {escolha8}')
print(f'Farmacia = {escolha9}')
print(f'Farmacia = {escolha10}')

print('*' * 15)
print('3* Andar')
print('*' * 15)

print(f'P9 = {escolha11}')
print(f'P9 = {escolha12}')
print(f'P8 = {escolha13}')
print(f'P12 = {escolha14}')
print(f'P13 = {escolha15}')
print(f'P10 = {escolha16}')
print(f'HD = {escolha17}')

print('*' * 15)
print('4* Andar')
print('*' * 15)

print(f'P11 = {escolha18}')
print(f'P7 = {escolha19}')
print(f'C7 = {escolha20}')
print(f'Diretoria = Evandro')

print('*' * 15)
print('5* Andar')
print('*' * 15)

print(f'P14 = {escolha21}')

print('*' * 15)
print('Ronda = Marcia')
print(f'Ronda = {escolha22}')
print('*' * 15)

print('*' * 15)
print('Apoio = Tereza')
print('Apoio = Ranie')
print('Apoio = Casa Grande')
print('*' * 15)
