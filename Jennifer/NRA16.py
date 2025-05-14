def  leia_num(msg):
    esperado = 28

    while True:
        num = input(msg)
        if num.isdigit() and int(num) == esperado:
            return int(num)
        print("invalido")

n = leia_num('digite um numero:')
print(n)