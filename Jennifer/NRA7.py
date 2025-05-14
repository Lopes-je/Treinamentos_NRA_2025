idades = []
homens = []
mulheres_20 = []



while True:
    idade = int(input("Qual sua idade?"))
    if idade >= 18:
        idades.append(idade)


    sexo = input("Qual seu sexo? F ou M?")
    if idade < 20 and sexo == 'F':
        mulheres_20.append(sexo) 
    else:
        homens.append(sexo)

    resp = int(input("Quer continuar? 1 sim, 2 não."))
    if resp == 1:
        continue
    else:
        break

print("A quantidade de pessoas maiores de 18 é: ",len(idades))
print("A quantidade de mulheres menores de 20 é:",len(mulheres_20))
print("A quantidade de homens é:" ,len(homens))



