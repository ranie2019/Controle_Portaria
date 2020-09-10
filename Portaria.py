import random

funcionarios = ['doralice', 'juliana', 'joao paulo', 'kleber', 'claudia', 'alessandro', 'amanda', 'edney', 'joseclay', 'luciana', 'maria aparecida', 'reginaldo', 'geruel',
                'gloria', 'fernando', 'Wilson', 'irineide', 'palmarindo', 'vera', 'machado', 'manuel', 'genilson', 'ricardo', 'cida', 'sueli', 'ivam', 'evandro', 'Evandro',
                'Tereza', 'Ranie', 'Casa Grande', 'Marcia']

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

escolha = random.choice(funcionarios)

# escolha1 = random.choice(funcionarios)
# escolha2 = random.choice(funcionarios)
# escolha3 = random.choice(funcionarios)
# escolha4 = random.choice(funcionarios)
# escolha5 = random.choice(funcionarios)
# escolha6 = random.choice(funcionarios)
# escolha7 = random.choice(funcionarios)
# escolha8 = random.choice(funcionarios)
# escolha9 = random.choice(funcionarios)
# escolha10 = random.choice(funcionarios)
# escolha11 = random.choice(funcionarios)
# escolha12 = random.choice(funcionarios)
# escolha13 = random.choice(funcionarios)
# escolha14 = random.choice(funcionarios)
# escolha15 = random.choice(funcionarios)
# escolha16 = random.choice(funcionarios)
# escolha17 = random.choice(funcionarios)
# escolha18 = random.choice(funcionarios)
# escolha19 = random.choice(funcionarios)
# escolha20 = random.choice(funcionarios)
# escolha21 = random.choice(funcionarios)
# escolha22 = random.choice(funcionarios)


print(f'\n1* ANDAR\n \nChapelaria = {escolha} \nP5 = {escolha} \nP5 = {escolha} \nCatraca = {escolha} \nSub-solo = {escolha} \n \n2* ANDAR\n \nQuimio = {escolha} \nDocas = {escolha}'
      f'\nFarmacia = {escolha} \nFarmacia = {escolha} \n \n3* ANDAR\n \nP9 = {escolha} \nP9 = {escolha} \nP8 = {escolha} \nP12 = {escolha} \nP13 = {escolha} \nP10 = {escolha}'
      f'\nHD = {escolha} \n \n4* ANDAR\n \nP11 = {escolha} \nP7 = {escolha} \nC7 = {escolha} \nDiretoria = {escolha} \n \n5* ANDAR\n \nP14 = {escolha} \nRonda = {escolha} '
      f'\nRonda = {escolha} \nApoio = {escolha} \nApoio = {escolha} \nApoio = {escolha}')
