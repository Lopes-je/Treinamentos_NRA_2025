valor_casa = float(input("Qual o valor da casa?"))

salario= float(input("Qual o salário do comprador"))

anos = int(input("Será pago em quantos anos?"))

meses = (anos/12)

prestação = (valor_casa/meses)

conta = (30/100*salario)

if prestação > conta:
    print ("negado")
else:
    print("aceito")