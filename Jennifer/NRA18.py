lista = []
for _ in range (5):
    num = int(input('digite 5 numeros:'))
    lista.append(num)

print('Maior numero:',max(lista))
print('Menor numero:',min(lista))
print('Posição do maior numero:', lista.index(max(lista))+1) 
print('Posição do menor numero:',lista.index(min(lista))+1)
