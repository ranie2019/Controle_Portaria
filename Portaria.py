import random

funcionarios = ['doralice', 'juliana', 'joao paulo', 'kleber', 'claudia', 'alessandro', 'amanda', 'edney', 'joseclay', 'luciana', 'maria aparecida', 'reginaldo', 'geruel',
                'gloria', 'fernando', 'wilson', 'irineide', 'palmarindo', 'vera', 'machado', 'manuel', 'genilson', 'ricardo', 'cida', 'sueli', 'ivam', 'evandro',
                'tereza', 'ranie', 'casa grande', 'marcia']

print(''''\nDeseja Remover Algum Nome?
Se Sim Digite 1
Se Nao Digite 0
''')

a = int(input('Digite o Numero: '))
if a == 1:
    nome = str(input('Digite o Nome Que Voce Quer Remover: '))
    funcionarios.remove(nome)
    a += 1
    while a > 1:
        a = int(input('Digite o Numero: '))
        if a == 1:
            nome = str(input('Digite o Nome Que Voce Quer Remover: '))
            funcionarios.remove(nome)
            a += 1

escolha = random.choice(funcionarios)


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
escolha23 = random.choice(funcionarios)
escolha24 = random.choice(funcionarios)
escolha25 = random.choice(funcionarios)
escolha26 = random.choice(funcionarios)


print(f'\n1* ANDAR\n \nChapelaria = {escolha1} \nP5 = {escolha2} \nP5 = {escolha3} \nCatraca = {escolha4} \nSub-solo = {escolha5} \n \n2* ANDAR\n \nQuimio = {escolha6} \nDocas = {escolha7}'
      f'\nFarmacia = {escolha8} \nFarmacia = {escolha9} \n \n3* ANDAR\n \nP9 = {escolha10} \nP9 = {escolha11} \nP8 = {escolha12} \nP12 = {escolha13} \nP13 = {escolha14} \nP10 = {escolha15}'
      f'\nHD = {escolha16} \n \n4* ANDAR\n \nP11 = {escolha17} \nP7 = {escolha18} \nC7 = {escolha19} \nDiretoria = {escolha20} \n \n5* ANDAR\n \nP14 = {escolha21} \nRonda = {escolha22} '
      f'\nRonda = {escolha23} \nApoio = {escolha24} \nApoio = {escolha25} \nApoio = {escolha26}')
