lista = []
lista_par = []
lista_impar = []

for _ in range(10):
    num = int(input('Digite um numero:'))
    lista.append(num)

    if num % 2 ==0:
        lista_par.append(num)

    else:
        lista_impar.append(num)

print('Lista completa:',lista)
print('Numeros pares:',lista_par)
print('Numeros impares:',lista_impar)