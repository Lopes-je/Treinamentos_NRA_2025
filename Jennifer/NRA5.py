reta1 = int(input("Qual a medida da reta 1?"))
reta2 =  int(input("Qual a medida da reta 2?"))
reta3 =  int(input("Qual a medida da reta 3?"))


if (reta1 + reta2 > reta3 ) and (reta2+reta3 > reta1) and (reta3 + reta1 > reta2):
    if reta1 == reta2 == reta3:
        print("forma um triangulo equilatero")

    elif reta1 != reta2 != reta3:
        print("forma um triangulo escaleno")

    else:
        print("forma um triangulo isoceles")


else:
    print("Não é triangulo")