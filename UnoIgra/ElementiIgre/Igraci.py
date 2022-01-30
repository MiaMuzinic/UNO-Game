from random import randint
from getpass import getpass
from Karte import generiraj_karte
from Boje import *
class Igrac:
    vrsta = "korisnik"
    pobjede = 0
    odigrano = 0
    izgubljeno = 0
    

    def __init__(self, korisnik_ime):
        self.korisnik_ime = korisnik_ime
        self.ruka = []


    def __str__(self):
        return "{0}".format(self.korisnik_ime)


        
    def makniKartu(self, niz_karata):
        sl_index = randint(0, len(niz_karata)-1)
        makniKartu = niz_karata[sl_index]

        self.ruka.append(makniKartu)
        niz_karata.remove(makniKartu)


    def staviKarte(self, karta, niz_karta, igra):
        ovuimas = False
        
        if (igra.karta_u_igri.vrsta == "Specijalna"
        and igra.karta_u_igri.vlasnik != self.korisnik_ime):
            if karta != igra.karta_u_igri.keypress:
                return True

        for i in self.ruka:
            if i.keypress == karta.upper():
                ovuimas = True
                spremi_kartu = i
                
                if (i.keypress == igra.karta_u_igri.keypress
                or i.boja == igra.karta_u_igri.boja
                or i.boja == Fore.WHITE
                or igra.karta_u_igri.boja == Fore.WHITE):
                    self.ruka.remove(i)
                    niz_karta.append(igra.karta_u_igri)
                    igra.karta_u_igri = i
                    return True

        if self.vrsta == "Robot": return False

        if ovuimas:    
            print(spremi_kartu.boja + "\t\t({0}) <─ Ne mmozes"
            "igrat ovu kartu.".format(spremi_kartu.sadrzaj))
            return False     

        print("\t\t({0}) <─ Nemas ovu kartu ".format(karta))
        return False


    def staviKarteuRuku(self, niz_karta):
        for i in range(7):
            self.makniKartu(niz_karta)


    def pokaziRuku(self):
        for i in self.ruka:
            print("\t{}".format(i), end="")
        print("\n")



class Robot(Igrac):
    vrsta = "Robot"
    
    def __str__(self):
        return "{0} robot".format(self.ime)


    def potezRobota(self, igra, karte):
        zadnja_karta = igra.karta_u_igri      
        potez = False
        while not potez:
            for i in self.ruka:
                potez = self.staviKarte(i.keypress, karte, igra)
                if potez:
                    break

            if not potez:
                self.makniKartu(karte)
                return 1
        if zadnja_karta is igra.karta_u_igri: return 2
        return 0
