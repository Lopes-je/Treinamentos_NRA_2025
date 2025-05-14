def funcao():
    frase = input("Digite uma frase:").strip().replace(" ", "").lower()
    inversa = frase[::-1]
    if frase == inversa:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")
funcao()