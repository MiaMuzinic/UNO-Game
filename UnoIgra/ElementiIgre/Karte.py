from random import randint
from Boje import *
class ObicneKarte:
    def __init__(self, broj, boja):
        self.vlasnik = ""
        self.keypress = broj
        self.vrsta = "Numeric"
        self.sadrzaj = broj
        self.boja = boja
    
    def __str__(self):
        return self.boja + "|{0}|".format(self.sadrzaj)


class Specijalna:
    vrsta = "Specijalna"
    vlasnik = ""


class PlusCetiri(Specijalna):
    def __init__(self):
        self.keypress = "+4"
        self.sadrzaj = "+4"
        self.boja = Fore.WHITE
        self.znacenje = Fore.WHITE + Back.BLACK + Style.BRIGHT
        
    def __str__(self):
        return self.znacenje + "|{0}|".format(self.sadrzaj) + Style.RESET_ALL
    
    def akcija(self, igrac, karte):
        for i in range(4):
            igrac.makniKartu(karte)
            
class PlusDva(Specijalna):
    def __init__(self, boja):
        self.keypress = "+2"
        self.sadrzaj = "+2"
        self.boja = boja
        
    def __str__(self):
        return self.boja + "|{0}|".format(self.sadrzaj)

    def akcija(self, igrac, karte):
        for i in range(2):
            igrac.makniKartu(karte)


class PromjenaBoje(Specijalna):
    def __init__(self):
        self.keypress = "C"
        self.sadrzaj = Fore.GREEN + "|" + Fore.BLUE + "\\" + Fore.WHITE + "C" + Fore.RED +  "/" + Fore.YELLOW + "|"
        self.boja = Fore.WHITE
        self.znacenje = Back.BLACK + Style.BRIGHT
        
    def __str__(self):
        return self.znacenje + "{0}".format(self.sadrzaj) + Style.RESET_ALL
    
    def action(self, igrac, karte):
        if igrac.vrsta == "korisnik":
            while True:
                odabrana_boja = input("Unesi pocetno slovo boje koju zelis: ")
                if odabrana_boja.lower() in ["r", "b", "g", "y"]:
                    break
            return odabrana_boja

class PromjenaSmjera(Specijalna):
    def __init__(self, boja):
        self.keypress = "R"
        self.sadrzaj = "^v"
        self.boja = boja
    
    def __str__(self):
        return self.boja + "|{0}|".format(self.sadrzaj)
    
    def akcija(self, igra, odabrana_boja):
        pass


   
class Skip(Specijalna):
    def __init__(self, boja):
        self.keypress = "S"
        self.sadrzaj = "(/)"
        self.boja = boja
        
    def __str__(self):
        return self.boja + "|{0}|".format(self.sadrzaj)
    
    def akcija(self, igrac, karte):
        return 

        


def generiraj_karte():
    kreirane_karte = [karta for karta in range(1, 10)] * 2
    kreirane_karte.append(0)
    bojekarata = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW]
    niz_karata = []
    
    for i in kreirane_karte:
        for j in bojekarata:
            nova = ObicneKarte(str(i), j)
            niz_karata.append(nova)
            
    for i in range(2):
        promjenaboje = PromjenaBoje()
        plus4 = PlusCetiri()
        niz_karata.append(plus4)
        niz_karata.append(plus4)

        for j in bojekarata:
            plus2 = PlusDva(j)
            skip = Skip(j)
            obrnismjer = PromjenaSmjera(j)
            
            niz_karata.append(plus2)
            niz_karata.append(skip)
            
    niz_karata = shuffle(niz_karata)
        
    return niz_karata


def shuffle(niz_karata):
    brojkarata = len(niz_karata)
    
    for i in range(brojkarata-1, 0 , -1):
        slucajni_index = randint(0, brojkarata-1)
        niz_karata[slucajni_index], niz_karata[i] = niz_karata[i], niz_karata[slucajni_index]
    return niz_karata
        
