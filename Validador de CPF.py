CPF_val = 0
CPF_inv = 0
CPF_test = 0
lista_cpf = list()

print('-='*33)
print('-=                       VALIDADOR DE CPF                       -=')
print('-='*33)

while True:
    CPF = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    #ADQUIRE OS DADOS DA LISTA "CPF" (OS PRIMEIROS 9 DÍGITOS) NA COLUNA 0 E INSERE UMA SEQUÊNCIA DECRESCENTE INICIANDO PELO 10 NA COLUNA 1
    DV = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    #ADQUIRE OS DADOS DA LISTA "CPF" (OS PRIMEIROS 9 DÍGITOS MAIS UM VERIFICADOS) NA COLUNA 0 E INSERE UMA SEQUÊNCIA DECRESCENTE INICIANDO PELO 11 NA COLUNA 1
    DV2 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    #MULTIPLICA AS DUAS COLUNAS DA MESMA LINHA DA LISTA "DV" E ADICIONA CADA MULTIPLICAÇÃO EM SUA DEVIDA POSIÇÃO
    ListaV = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    #MULTIPLICA AS DUAS COLUNAS DA MESMA LINHA DA LISTA "DV2" E ADICIONA CADA MULTIPLICAÇÃO EM SUA DEVIDA POSIÇÃO
    ListaV2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    #DIGITOS VERIFICADORES
    V1 = 0
    V2 = 0

    #AUXILIA NA SEPARAÇÃO DOS DÍGITOS DO CPF
    num = 1

    dicionario_cpf = dict()
    digitos_cpf = [0]

    #INICIANDO A OPERAÇÃO
    if CPF_test == 0:
        resp = input('\nDeseja iniciar a operação de validação de CPF? Digite "s" ou "n": ').lower()

    else:
        print('-=' * 32)
        resp = input('\nDeseja continuar a operação de validação de CPF? Digite "s" ou "n": ').lower()

    #DIGITAÇÃO INCORRETA
    while (resp != 's') and (resp != 'n'):
        resp = input('\nDigite somente "s" ou "n": ').lower()

    #PARANDO A EXECUÇÃO
    if resp == 'n':
        break

    D10 = 10
    D11 = 11

    #DIGITOS DO CPF
    digitos_cpf[0] = int(input('\nInforme seu CPF (somente números): '))
    while digitos_cpf[0] < 10000000000 or digitos_cpf[0] > 99999999999:
        digitos_cpf[0] = int(input('\nEntrada inválida, por favor redigite: '))

    dicionario_cpf['CPF'] = digitos_cpf

    #ATRIBUINDO OS DÍGITOS A UMA LISTA
    for cont11 in range(0, 11):
        CPF[cont11] = digitos_cpf[0] // num % 10
        num *= 10

    #ATRIBUIÇÃO DE VALORES PARA CALCULAR OS VERIFICADORES
    for cpf_cont in range(0, 11):
        if cpf_cont <= 8:
            DV[cpf_cont][0] = CPF[cpf_cont]
            DV[cpf_cont][1] = D10
            ListaV[cpf_cont] = DV[cpf_cont][0] * DV[cpf_cont][1]

        if cpf_cont <= 9:
            DV2[cpf_cont][0] = CPF[cpf_cont]
            DV2[cpf_cont][1] = D11
            ListaV2[cpf_cont] = DV2[cpf_cont][0] * DV2[cpf_cont][1]

        if (cpf_cont >= 0) and (cpf_cont <= 8):

            ListaV[cpf_cont] = ListaV[cpf_cont] + ListaV[cpf_cont - 1]
            Soma = ListaV[cpf_cont]
            ListaV2[cpf_cont] = ListaV2[cpf_cont] + ListaV2[cpf_cont - 1]
            Soma2 = ListaV2[cpf_cont]

        D10 -= 1
        D11 -= 1

    #PRIMEIRO DÍGITO VERIFICADOR
    V1 = Soma % 11
    if V1 < 2:
        V1 = 0

    else:
        V1 = 11 - V1

    #SEGUNDO DÍGITO VERIFICADOR
    Soma2 = Soma2 + (V1 * 2)
    V2 = Soma2 % 11

    if V2 < 2:
        V2 = 0

    else:
        V2 = 11 - V2

    #INFORMANDO AO USUÁRIO
    if (CPF[9] != V1) or (CPF[10] != V2):
        print("\nCPF inválido!\n")
        CPF_inv += 1
        dicionario_cpf['VALIDACAO'] = 'INVÁLIDO'

    else:
        print("\nCPF válido!\n")
        CPF_val += 1
        dicionario_cpf['VALIDACAO'] = 'VÁLIDO'

    CPF_test += 1

    lista_cpf.append(dicionario_cpf)

if CPF_inv > 0:
    inv_porcen = (CPF_inv * 100) / CPF_test
else:
    inv_porcen = 0

if CPF_val > 0:
    val_porcen = (CPF_val * 100) / CPF_test
else:
    val_porcen = 0

#RESULTADOS DO TESTE
print()
print('-='*33)
print('-=                         RESULTADOS                           -=')
print('-='*33)

print(f'\nQuantidade de CPFs testados: {CPF_test}')
print(f'Quantidade de CPFs inválidos: {CPF_inv}')
print(f'Quantidade de CPFs válidos: {CPF_val}')
print(f'Porcentagem de CPFs inválidos: {inv_porcen:.2f}%')
print(f'Porcentagem de CPFs válidos: {val_porcen:.2f}%\n')

print('-='*33)
print('-=                           STATUS                             -=')
print('-='*33)
for contl in range(0, len(lista_cpf)):
    print(lista_cpf[contl])
