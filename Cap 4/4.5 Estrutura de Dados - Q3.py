
lista = [0,0,0,0]

for i in range(0,4):
    lista[i] = int(input(print("Digite a nota "+ str(i+1) + " :")))
    print(i)


print(lista)
print("A média da lista é: " + str((sum(lista))/4))