import sys

try:
    sys.path.append("../Igranje")
    from Igra import *
    from Random_boje import *
    from BazaIgraca import *
except:
    sys.path.append("Igranje")
    from Igra import *
    from Random_boje import *
    from BazaIgraca import *

    

def main_menu():
    ocistiEkran()
    odabir_izbornik = input(promjeni_Boju() + """
    ***********************************************************************                                                                    

                                    UNO


        1.Nova igra
        2.Popis igraca i rezultati
        3.Top 10 igraca
        4.Pravila
        E-Kraj                                                          
    ***********************************************************************
        >> """)
    
    if odabir_izbornik == "1": nova_igra()
    elif odabir_izbornik == "2": poredakIgraca()
    elif odabir_izbornik == "3": top10()
    elif odabir_izbornik == "4": pravila()
    elif odabir_izbornik.lower() == "e": ocistiEkran(); quit()
    else: main_menu()


def nova_igra():
    ocistiEkran()
    
    odabirigrac = input(promjeni_Boju() + """
    ***********************************************************************                                                                    

                                    UNO

        
        1.Novi igrac
        2.Ucitaj igraca
        3.Natrag na izbornik
        E-Kraj                                                          
    ***********************************************************************
    
        >> """)
    
    if odabirigrac == "1": korisnik_ime = stvori_korisnika()
    elif odabirigrac == "2": korisnik_ime = ucitaj_igraca()
    elif odabirigrac == "3": main_menu()
    elif odabirigrac.lower() == "e": ocistiEkran(); quit()
    else: nova_igra()
    
    status = pocetak(korisnik_ime)
    g = status
    spremiPoredak(korisnik_ime, g[0], g[1], g[2])
    nova_igra()


def poredakIgraca():
    ocistiEkran()
    print("*****************************************************************")
    print("Ovo je popis igraca i njihovi rezultati:\n")
    prikazi_igrace()
    odabir=input("Za povratak u izbornik odaberi na tipkovnici E!! ")
    while(odabir.lower()!="e"):
        odabir=input("Za povratak u izbornik odaberi na tipkovnici E!!")
    main_menu()
    
def top10():
    ocistiEkran()
    print("*****************************************************************")
    print("Ovo je TOP 10 igraca:\n")
    top10_igraca()
    odabir=input("Za povratak u izbornik odaberi na tipkovnici E!! ")
    while(odabir.lower()!="e"):
        odabir=input("Za povratak u izbornik odaberi na tipkovnici E!!")
    main_menu()

def pravila():
    ocistiEkran()
    f = open("Igranje/Pravila.txt", "r")
    print(f.read())
    odabir=input("Za povratak u izbornik odaberi na tipkovnici E!! ")
    while(odabir.lower()!="e"):
        odabir=input("Za povratak u izbornik odaberi na tipkovnici E!!")
    main_menu()
