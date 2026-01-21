#Apresentação das regras
print("--- Jogo Pedra, Papel ou Tesoura ---")
print("Regras: Escolham entre 'pedra', 'papel' ou 'tesoura'")

#Entrada de dados
jogador1 = input("Jogador 1 - Digite a sua jogada: ")
jogador2 = input("Jogador 2 - Digite a sua jogada: ")

#Tratamento dos dados
jogador1 = jogador1.lower().strip()
jogador2 = jogador2.lower().strip()

#Validação
if jogador1 == jogador2:
    print("Empate!")
elif (jogador1 == 'pedra' and jogador2 == 'tesoura') or (jogador1 == 'tesoura' and jogador2 == 'papel') or (jogador1 == 'papel' and jogador2 == 'pedra'):
    print("Jogador 1 venceu!")
else:
    print("jogador 2 venceu!")

