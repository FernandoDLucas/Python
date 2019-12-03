def criarConta(numero, nome, valor, limite):
    conta = {'Numero': numero, 'Nome': nome, 'Valor': valor, 'limite': limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print("Numero: {}    Saldo: {}" .format(conta['Numero']))
conta1 = criarConta('1584-3', 'Fernando', 1100, 1500)
conta2 = criarConta('1326-7', 'Lucas', 1100, 1500)

print(conta1['Numero'])


