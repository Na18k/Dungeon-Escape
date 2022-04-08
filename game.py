from functions import pri, delay, clear, logo, status, separador, ler_save_game, escreve_save_game
from animations import animation

dados_do_jogo = ler_save_game()                  

def inicio():
	pri("", 5)
	print("Boas vindas viajante do espaço.")
	print("")
	print("Na18k | Thex 1223")
	print("") 
	print('Um dos jogos de "History Dungeon" por Kainan | Na18k')
	# animation(2)
	delay(3)
	clear()

	logo(1)
	delay(4)
	clear()

	# animation(3)

inicio()

nome_do_jogador = ""
hp = 200
lvl = 0
coins = 0
link = 0

jogo_rodando = 0
numero_de_while = 10 # Impede que o jogo passe do limite de jogadas

while jogo_rodando < numero_de_while:

	if(link	!= 0 and link != 1):
		print("")
		entrada_input = input("{} ==> ".format(nome_do_jogador))

	if(link != 0):
		clear()
		status(float(hp), float(lvl), float(coins))
		escreve_save_game(nome_do_jogador, hp, lvl, coins, link)

	if(link == 0):
		dados_do_jogo = ler_save_game()
		clear()
		separador()
		pri("", 3)
		print("MENU:")
		print("")
		print("[1] Iniciar Novo jogo")
		print("")

		if(dados_do_jogo[0] == "nada"):
			print("Nenhum jogo anterior salvo!")
			print("")
		else:
			print("[2] Continuar Jogando")
			print("")

		print("[3] Opções")
		print("")
		print("[4] Apagar Save")
		pri("", 2)
		separador()

		menu = int(input("==> "))

		if(menu == 1):
			clear()
			nome_do_jogador = input("Nome do jogador: ")
			escreve_save_game(nome_do_jogador, hp, lvl, coins, link)
			animation(1)


		elif(menu == 2):
			nome_do_jogador = dados_do_jogo[0]
			hp = dados_do_jogo[1]
			lvl = dados_do_jogo[2]
			coins = dados_do_jogo[3]
			link = dados_do_jogo[4]

		elif(menu == 3):
			print("Nada no momento para ser mostrado aqui. :)")
			print("Voltando ao menu...")
			delay(3)
			continue

		elif(menu == 4):
			escreve_save_game("nada", 0, 0, 0, 0)
			print("Save DELETADO!")
			print("Voltando ao menu...")
			delay(2)
			continue

		link = 1
		continue

	if(link == 1):
		print("Você está em uma masmora, especificamente num lugar com quatro paredes.")
		print("")
		print("			╔═════/ ══════╗")
		print("			║            O║")
		print("			║9            ║")
		print("			║6     X      ║")
		print("			║4            ║")
		print("			║2            ║")
		print("			╚═════════════╝")
		print()
		print("Existe nesta sala um barril, uma porta fechada, e na parede a esquerda os \n números [2469].")
		separador()
		link = 2
		continue

	elif(link == 1):
		print("Você está em uma masmora")
		link = 1
		continue
	elif(link == 1):
		print("Você está em uma masmora")
		link = 1
		continue

print("GAME END")