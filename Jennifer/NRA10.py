while True:
    num = int(input("Digite um número: "))

    if num > 0:
        for i in range(11):
            conta = i * num
            print(conta)
    else:
        print("Inválido")