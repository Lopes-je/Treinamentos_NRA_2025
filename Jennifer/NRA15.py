def funcao_maior():
    maior = 0
    while True: 
        num = int(input("Digite um numero: "))
        if num > 0:   
            if num > maior:
                maior = num
        else:
            break
    return maior
num = funcao_maior()
print(num)