def velocidade(espaco,tempo):
    v = espaco/tempo
    print("Velocidade: {} m/s" . format(v))

var1 = float(input(print("Digite o valor do espaço em metro: ")))
var2 = float(input(print("Digite o valor do tempo em segundos: ")))

velocidade(var1, var2)


def diz_oi():
    print("Oi")


diz_oi()


def velocidade(espaco, tempo):
    v = espaco/tempo
    return v

def calculadora(x,y):
    return {'soma': x+y, 'subtracao':x-y}

resultados = calculadora(1,2)
for key in resultados:
    print('{}: {}' . format(key, resultados[key]))
