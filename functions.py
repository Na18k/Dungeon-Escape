import time
import os

def pri(msg, space):
	i = 0
	while i < space:
		print("")
		i = i + 1
	print(msg)

def delay(tempo_de_delay):
	time.sleep(tempo_de_delay)

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def logo(numero_da_logo):
	if(numero_da_logo == 1):
		print("")
		print("____________________________________________________________________________")
		print(" /$$$$$$$                                                                   ")
		print("| $$__  $$                                                                  ")
		print("| $$  \ $$ /$$   /$$ /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$       ")
		print("| $$  | $$| $$  | $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$      ")
		print("| $$  | $$| $$  | $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \ $$| $$  \ $$      ")
		print("| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$_____/| $$  | $$| $$  | $$      ")
		print("| $$$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$/| $$  | $$      ")
		print("|_______/  \______/ |__/  |__/ \____  $$ \_______/ \______/ |__/  |__/      ")
		print("                               /$$  \ $$                                    ")
		print("                              |  $$$$$$/                                    ")
		print("                               \______/                                     ")
		print(" /$$$$$$$$                                                                  ")
		print("| $$_____/                                                                  ")
		print("| $$        /$$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$                 ")
		print("| $$$$$    /$$_____/ /$$_____/ |____  $$ /$$__  $$ /$$__  $$                ")
		print("| $$__/   |  $$$$$$ | $$        /$$$$$$$| $$  \ $$| $$$$$$$$                ")
		print("| $$       \____  $$| $$       /$$__  $$| $$  | $$| $$_____/                ")
		print("| $$$$$$$$ /$$$$$$$/|  $$$$$$$|  $$$$$$$| $$$$$$$/|  $$$$$$$                ")
		print("|________/|_______/  \_______/ \_______/| $$____/  \_______/                ")
		print("                                        | $$                                ")
		print("                                        | $$                                ")
		print("                                        |__/                                ")
		print("____________________________________________________________________________")
	elif(numero_da_logo == 2):
		
		print("★ ° . *　　　°　.　°☆ 　. * ● ¸ ★ ° . *　　　°　.　°☆ 　. * ● ¸")
		print(". 　　　★ 　° :. ★　 * • ○ ° ★　 . 　　　★ 　° :. ★　 * •  ○ ")
		print(".　 * 　.　 　　　　　. 　 .　 * 　.　 　　　　　. 　.• ○ °   • ○ ° ★")
		print("° 　. ● . ★ ° . *　　　°　.　°☆ ° 　. ● . ★ ° . *　　　°　.　°☆")
		print("　. * ● ¸ . 　　　★ 　° :●. 　 * 　. * ● ¸ . 　　　★ 　° :●. 　 ")
		print("• ○ ° ★　 .　 * 　.　 　　　　　.• ○ ° ★　 .　 * 　.　 　　　　　.")

	elif(numero_da_logo == 3):

		print("        :::    ::::::::   ::::::::   :::::::: ")
		print("     :+:+:   :+:    :+: :+:    :+: :+:    :+: ")
		print("      +:+         +:+        +:+         +:+  ")
		print("     +#+       +#+        +#+        +#++:    ")
		print("    +#+     +#+        +#+             +#+    ")
		print("   #+#    #+#        #+#       #+#    #+#     ")
		print("####### ########## ##########  ########       ")

def status(hp, lvl, coins):

	print("+ --------------------------------------------------------------------------- +")
	print("  HP: {:.2f} | LVL: {:.2f} | COINS: {:.2f}".format(hp, lvl, coins))
	print("+ --------------------------------------------------------------------------- +")
	
def separador():
	print("+ --------------------------------------------------------------------------- +")

def ler_save_game():
	arquivo = open("save_game.txt", "r")
	argumentos = []

	for linha in arquivo:
		linha = linha.strip()
		argumentos.append(linha)
	arquivo.close()

	return argumentos

def escreve_save_game(nome_do_jogador, hp, lvl, coins, link):

	arquivo = open("save_game.txt", "w")
	
	arquivo.write("{}\n".format(nome_do_jogador))
	arquivo.write("{}\n".format(hp))
	arquivo.write("{}\n".format(lvl))
	arquivo.write("{}\n".format(coins))
	arquivo.write("{}\n".format(link))

	arquivo.close()
