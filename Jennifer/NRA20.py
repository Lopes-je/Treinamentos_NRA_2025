controle_time = []
total_gol = []

while True:
    nome_jogador = input('Qual o nome do jogador?')
    partidas = int(input('Numero de partidas:'))
    gols = int(input('Quantidade de gols:'))


    total_gol.append(gols)

    jogador = {
        'nome': nome_jogador,
        'numero de partidas': partidas,
        'gols': gols
    }

    controle_time.append(jogador)
    resp = int(input('Quer adicioanr mais jogadores? 1 sim, 2 não.'))
    if resp = 1:
        break

print('O total de gols do time foi:',sum(total_gol))
print('lisatd e jogadores:')
for j in controle_time:
    print(j)
