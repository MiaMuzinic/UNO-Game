import json

global korisnik_ime
def ucitaj_json():
    file = open("Igranje/Igraci.json", "r")
    podaci = json.load(file)
    return podaci


def prikazi_igrace():
    podaci = ucitaj_json()
    sortirano=sorted(podaci["korisnik"], key=lambda d: d["odigrano"],reverse=True)
    for i in range(len(sortirano)-1):
        print(sortirano[i])
  


def update_igraci(podaci):
    info = json.dumps(podaci, indent=2)
    
    zamjena = open("Igranje/Igraci.json", "w")
    zamjena.write(info)
    zamjena.close()

def stvori_korisnika():
    podaci = ucitaj_json()
    invalid = True
    while invalid:
        korisnik_ime = input("\nUnesi novo korisnicko ime: ")
        invalid = validacija(korisnik_ime)
        if invalid: print("\nKorisnicko ime postoji.")

    novi_podaci = {"korisnik_ime": korisnik_ime, "odigrano": 0,
                "pobjede": 0, "izgubljeno": 0}
    
    podaci["korisnik"].append(novi_podaci)
    update_igraci(podaci)
    
    return korisnik_ime

def ucitaj_igraca():
    podaci=ucitaj_json()
    
    postoji = False
    while not postoji:
        korisnik_ime = input("\nUnesi korisncko ime: ")
        postoji = validacija(korisnik_ime)
        if not postoji: print("\nNe postoji korisnicko ime.")
    return korisnik_ime


def validacija(korisnik_ime):
    podaci = ucitaj_json()
        
    for korisnik in podaci["korisnik"]:
        if korisnik["korisnik_ime"].lower() == korisnik_ime.lower():
            return True
    return False




def spremiPoredak(korisnik_ime, odigrano, pobjede, izgubljeno):
    podaci = ucitaj_json()
    for korisnik in podaci["korisnik"]:
        if korisnik["korisnik_ime"].lower() == korisnik_ime.lower():
            zamjenjeni = korisnik
            korisnik["odigrano"] += odigrano
            korisnik["pobjede"] += pobjede
            korisnik["izgubljeno"] += izgubljeno
            break

    i = podaci["korisnik"].index(zamjenjeni)
    podaci["korisnik"][i] = zamjenjeni

    update_igraci(podaci)
def top10_igraca():
    file = open("Igranje/Igraci.json", "r")
    podaci = json.load(file)
    sortirano=sorted(podaci["korisnik"], key=lambda d: d["pobjede"],reverse=True)
    for i in range(10):
        print(sortirano[i])
