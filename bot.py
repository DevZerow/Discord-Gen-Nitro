import random
import requests
import string
import os
import time

LICNECE = """
Copyright (c) 2022 Zerow
L'autorisation est accordée, gratuitement, à toute personne obtenant une copie de ce logiciel et des fichiers de documentation associés (le "Logiciel"), de traiter le Logiciel sans restriction, y compris, sans limitation, les droits d'utilisation, de copie, de modification, de fusion , publier, distribuer, sous-licencier et/ou vendre des copies du Logiciel, et permettre aux personnes à qui le Logiciel est fourni de le faire, sous réserve des conditions suivantes :
L'avis de droit d'auteur ci-dessus et cet avis d'autorisation doivent être inclus dans toutes les copies ou parties substantielles du Logiciel.
LE LOGICIEL EST FOURNI « EN L'ÉTAT », SANS GARANTIE D'AUCUNE SORTE, EXPLICITE OU IMPLICITE, Y COMPRIS, MAIS SANS S'Y LIMITER, LES GARANTIES DE QUALITÉ MARCHANDE, D'ADÉQUATION À UN USAGE PARTICULIER ET D'ABSENCE DE CONTREFAÇON. EN AUCUN CAS, LES AUTEURS OU LES DÉTENTEURS DU COPYRIGHT NE SERONT RESPONSABLES DE TOUTE RÉCLAMATION, DOMMAGE OU AUTRE RESPONSABILITÉ, QUE CE SOIT DANS UNE ACTION CONTRACTUELLE, DÉLICTUELLE OU AUTRE, DÉCOULANT DE, DE OU EN RELATION AVEC LE LOGICIEL OU L'UTILISATION OU D'AUTRES TRANSACTIONS DANS LE LOGICIEL.
"""
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(3)

print(LICNECE)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

try: 
    import numpy
except ImportError: 
    input(
        f"Module numpy non installé, pour installer exécuter '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nAppuyez sur Entrée pour quitter")
    exit() 
url = "https://google.com"
try:
    response = requests.get(url) 
    print("Internet check")
    time.sleep(.4)
except requests.exceptions.ConnectionError:
   
    input("Vous n'êtes pas connecté à Internet, vérifiez votre connexion et réessayez.\nAppuyez sur Entrée pour quitter")
    exit() 
    
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(3)

print("""███████╗███████╗██████╗░░█████╗░░██╗░░░░░░░██╗
╚════██║██╔════╝██╔══██╗██╔══██╗░██║░░██╗░░██║
░░███╔═╝█████╗░░██████╔╝██║░░██║░╚██╗████╗██╔╝
██╔══╝░░██╔══╝░░██╔══██╗██║░░██║░░████╔═████║░
███████╗███████╗██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░
╚══════╝╚══════╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░""")
time.sleep(2) 
print(".")                   
print("Il s'agit d'un générateur de code discord nitro et d'un vérificateur en python. Cela générera des codes nitro et vérifiera si le code est valide ou non. '*'.\n\n\n")
time.sleep(3) 

caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

while True:
    nitrocode = ''

    for i in range(16):
        nitrocode = f"{nitrocode}{random.choice(caracteres)}"

    print(f"https://discord.gift/{nitrocode}")

    with open("nitros.txt", "a+") as nitroFile:

        nitroFile.write(f"https://discord.gift/{nitrocode}\n")

        nitroFile.close()

while True:
    nitrocode = ''
    
with open("nitros-valid.txt") as file:
    for line in file.readlines():
        nitrocode = line.strip("\n")

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitrocode}?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f"\n\n Valid | {nitrocode}\n\n")
        file.write(f"https://discord.gift/{nitrocode}\n")
        file.close()
