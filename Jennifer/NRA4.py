altura = float(input("Qual sua altura?"))
peso = float(input("Qual seu peso?"))


imc = ( peso/altura**2 )

if imc < 18.5:
    print("Abaixo do peso")

if 18.5 <= imc < 25:
    print("peso ideal")

if 30 > imc >= 25:
    print("sobrepeso")

if imc == 30 and imc <= 40:
    print("obesidade")
if imc > 40:
    print("obesidade morbita")