nome = input("Digite um nome: ")
partes = nome.split(' ')  

print(nome.upper())

print(nome.lower())

print("O nome completo tem essa quantidae de letras: ", len(nome))

primeiro_nome = nome.split()[0]
print("O primeiro nome tem essa quantidade de letras:", len(primeiro_nome))