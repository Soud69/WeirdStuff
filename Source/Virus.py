#
# This Is Free Tool By Soud Alanzi AKA @8Y
# Dont Try Sell It Cuz It's Fucking Free
# Github: https://github.com/Soud69
# Instagram: https://instagram.com/8Y
# Telegram: https://t.me/Soud69
# Discord: Soud#5866
#

try:
	import os
	from os import system
	system("title " + "Soud Was Here - @8Y - Soud#5866")
	import colorama
	from colorama import Fore
	colorama.init(autoreset=True)
except Exception as m:
	print("Something Went Wrong\n")
	print(m)
	input()
	exit()

logo = """
         _______   __
   ____ |  _  \ \ / /
  / __ \ \ V / \ V / 
 / / _` |/ _ \  \ /  
| | (_| | |_| | | |  
 \ \__,_\_____/ \_/  
  \____/             
"""
print(f"{Fore.CYAN}{logo}")
print(f"{Fore.GREEN}\n\tInstagram: @8Y\n\tGithub: @Soud69\n\tDiscord: Soud#5866\n\tTelegram: @Soud69{Fore.RED}\n\t[Dont Try To Sell It]\n")
print(f'You Are {Fore.GREEN}{int(input("Enter Your Tall: "))}cm {Fore.RESET}And {Fore.GREEN}{int(input("Enter Your Weight: "))}kg')
