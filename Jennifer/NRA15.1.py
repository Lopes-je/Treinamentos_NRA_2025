def funcao ():
    num = input("Digite um numero: ").split()

    numeros = []
    for i in num:
        numeros.append(int(num)) 

    maior = max(num)
    return maior

print(funcao())
