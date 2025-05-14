idades = []
mulheres_20 = []
homem_velho = ""
idade_mais_velho = 0

for i in range(5):
    nome = input("Qual seu nome?")
    sexo = input("Qual seu sexo? F ou M?").strip().upper()
    idade = int(input("Quantos anos tem?"))
    idades.append(idade)

    if sexo == "F":
        if idade < 20:
            mulheres_20.append(nome)

    if sexo == 'M':
        if idade > idade_mais_velho:
            idade_mais_velho = idade
            homem_velho = nome

media = sum(idades) / len(idades)

print("mulheres", mulheres_20, "homem mais velho", homem_velho, "idades", idades)
