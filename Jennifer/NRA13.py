palavra = input("Digite um frase: ")

sem_espaco = palavra.split(" ")
encontrada = palavra.find('a') +1
contada = palavra.count('a')
posicao_ultima = palavra.rfind("a")
print("primeira posição da letra a:", encontrada, "ocorrencia da letra a:",contada,"ultima vez que ela aparece:", posicao_ultima)