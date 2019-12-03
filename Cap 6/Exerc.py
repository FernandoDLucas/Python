import random
def imprime_mensagem_abertura():
    print("*******************************")
    print("***Bem vindo ao jogo da Forca***")
    print("********************************")

def carregar_palavra_secreta():
    with open('palavras.txt') as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]
def pede_chute():
    chute = input('Qual a letra? ')
    chute = chute.strip().upper()

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1

def imprime_mensagem_vencedor():
        print('Você ganhou!')
def imprime_mensagem_perdedor():
        print('Você perdeu!')

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas=inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

        if(acertou):
            imprime_mensagem_vencedor()
        else:
            imprime_mensagem_perdedor()

jogar()