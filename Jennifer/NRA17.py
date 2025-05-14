import random
tupla = ()
lista = []
for _ in range (5):
    num = random.randint(1,100)
    lista.append(num)

tupla = tuple(lista)
print(tupla, min(lista), max(lista))