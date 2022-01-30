from random import randint
from getpass import getpass
from platform import system
from subprocess import run

import sys
try:
    sys.path.append("../ElementiIgre")
    from Igraci import *
except:
    sys.path.append("ElementiIgre")
    from Igraci import *
    
global karte
global igra
global robot


karte = generiraj_karte()
robot = Robot("Robot")

def pocetak(korisnik_ime):
    ocistiEkran()
    
    igrac = Igrac(korisnik_ime)
    igra.novaIgra(igrac)
    igrac.odigrano += 1
    kontra = 0
    
    while True:
        kontra = Igraj(igrac, kontra)
        if kontra == None: break

        if len(robot.ruka) < 1:
            pobjednik = robot.korisnik_ime
            igrac.izgubljeno += 1
            break
        elif len(igrac.ruka) < 1:
            pobjednik = igrac.korisnik_ime
            igrac.pobjede += 1
            break
      
    return (igrac.odigrano, igrac.pobjede, igrac.izgubljeno)



class Igra:
    def __init__(self):
        self.karta_u_igri = None


    def prvaKarta(self, niz_karta):
        while True:
            random_indeks= randint(0, len(niz_karta)-1)
            makniKartu = niz_karta[random_indeks]
            if makniKartu.vrsta != "Specijalna": break
        
        self.karta_u_igri = makniKartu
        niz_karta.remove(makniKartu)


    def trenutna_karta(self):
        print("\n\n\t\t\t\t", end="")
        print(self.karta_u_igri)
        print("\n\n\n\n\n\n\n\n\n\n")


    def prikaziStol(self, igrac):
        ocistiEkran()
        print(Fore.WHITE + Style.BRIGHT + 
        "\n\n\n\n\n\n\nKarte od robota:" 
        " {0}\n\n".format(len(robot.ruka)) + Style.RESET_ALL)
        
        self.trenutna_karta()
        igrac.pokaziRuku()


    def novaIgra(self, igrac):
        igrac.ruka = []
        robot.ruka = []
        
        robot.staviKarteuRuku(karte)
        igrac.staviKarteuRuku(karte)
        
        self.prvaKarta(karte)
        self.prikaziStol(igrac)


    def igracNaRedu(self,igrac):
        zadnja_karta = self.karta_u_igri
        potez_moguc = False
        jedina_karta = False
        if self.karta_u_igri.vrsta == "Specijalna": jedina_karta= True
        
        while not potez_moguc:
            potezIgraca = input(self.karta_u_igri.boja + "Ti si na redu: ")
            if potezIgraca.lower() == "f":
                if (not jedina_karta or
                self.karta_u_igri.vlasnik == igrac.korisnik_ime):
                    igrac.makniKartu(karte)
                    return 1
                else:
                    getpass("Ne možeš završiti igru")
                    continue
            elif potezIgraca.lower() == "g":
                igrac.izgubljeno += 1
                return 2
            elif potezIgraca.lower() == "q":
                quit()
            
            potez_moguc = igrac.staviKarte(potezIgraca, karte, igra)
            
        if zadnja_karta is self.karta_u_igri:
            return 3
        return 0


    def prikaziPotezIgraca(self):
        ocistiEkran()
        print(Fore.WHITE + Style.BRIGHT + "\n\n\n\n\n\n\nKarte od robota:" 
            " {0}\n\n".format(len(robot.ruka)) + Style.RESET_ALL)
        self.trenutna_karta()
        getpass("Enter za nastavak...")


    def specijalniPotezi(self, cilj, zadnja_karta, kontra):
        kontra += 1
        if (self.karta_u_igri is zadnja_karta
        or self.karta_u_igri.keypress != zadnja_karta.keypress
        and self.karta_u_igri.vlasnik != cilj.korisnik_ime):
            for i in range (kontra):
                zadnja_karta.akcija(cilj, karte)
            return 0
        return kontra

            
        
def ocistiEkran():
    OS = system()
    if OS == "Windows":
        run("cls", shell=True)
    else:
        run("clear")


def Igraj(igrac, kontra):
    zadnja_karta = igra.karta_u_igri
    while True:
        korisnik_igra = igra.igracNaRedu(igrac)
        if korisnik_igra == 0:
            igra.karta_u_igri.vlasnik = igrac.korisnik_ime
            igra.prikaziPotezIgraca()
            if igra.karta_u_igri.keypress != "S": break
        elif korisnik_igra == 1: break
        elif korisnik_igra == 2: return None

        if zadnja_karta.vrsta == "Specijalna":
            kontra = igra.specijalniPotezi(igrac, zadnja_karta, kontra)
            if kontra == 0: break
        igra.prikaziStol(igrac)  
    igra.prikaziStol(igrac)
    
    if len(igrac.ruka) < 1: return 0    

    zadnja_karta = igra.karta_u_igri
    while True:
        robot_igra = robot.potezRobota(igra, karte)
        if robot_igra == 0:
            igra.karta_u_igri.vlasnik = robot.korisnik_ime
            if igra.karta_u_igri.keypress != "S": break
        elif robot_igra == 1: break
        
        if zadnja_karta.vrsta == "Specijalna":
            kontra = igra.specijalniPotezi(robot, zadnja_karta,kontra)
            if kontra == 0: break
        igra.prikaziStol(igrac)
    igra.prikaziStol(igrac)
    
    
    return kontra

igra = Igra()
