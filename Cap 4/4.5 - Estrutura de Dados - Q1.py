

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
print('O maior valor da lista é ' + str(max(lista)))
print('O menor valor da lista é ' + str(min(lista)))
i = 0;
for num in lista[0:(len(lista))]:
    if num%2 == 0:
        print(num)

print('O primeiro valor da lista aparece novamente ' + str(lista.count(lista[0])) +' vezes')
print("A média dos valores da lista é: "+ str((sum(lista)/len(lista))))

sumNeg = 0;
for num in lista[0:(len(lista))]:
    if num < 0:
        sumNeg += num

print("A soma dos valores negativos é" + str(sumNeg))





