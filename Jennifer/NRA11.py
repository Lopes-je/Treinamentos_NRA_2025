cinco = []
dois = []
dez = []
um = []

sacado = int(input("Quanto vai sacar do caixa? "))

conta1 = sacado // 50
cinco.append(conta1)
resto = sacado % 50

conta2 = resto // 20
resto = resto % 20
dois.append(conta2)

conta3 = resto // 10
resto = resto % 10
dez.append(conta3)

conta4 = resto
um.append(conta4)

print("Notas de 50:", cinco)
print("Notas de 20:", dois)
print("Notas de 10:", dez)
print("Notas de 1:", um)
