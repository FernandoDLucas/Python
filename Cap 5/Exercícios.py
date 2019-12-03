""" Exercícios funções"""

def divisao(x, y):
    return x/y

def velocidade_media(distancia, tempo):
    return divisao(distancia, tempo)

loop = 1

for i in range(0,4):
    distancia = int(input("Digite a distancia: "))
    tempo = int(input("Digite a tempo: "))
    print("A velocidade é: {} m/s" .format(velocidade_media(distancia, tempo)))




