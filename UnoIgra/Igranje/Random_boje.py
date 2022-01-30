from random import choice
import sys
try:
    sys.path.append("../ElementiIgre")
    from Boje import *
except:
    sys.path.append("ElementiIgre")
    from Boje import *

    
def promjeni_Boju():
    lista = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW]
    return choice(lista)
