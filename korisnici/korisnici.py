from korisnici.korisniciIO import ucitaj_korisnike, sacuvaj_korisnika



def prijava():
    korisnici = ucitaj_korisnike()
    for i in range(3):
        korisnicko_ime = input("korisnicko ime:")
        lozinka = input("lozinka:")

        for korisnik in korisnici:
            if korisnik['korisnicko_ime'] == korisnicko_ime and korisnik['lozinka'] == lozinka:
                return korisnik
        print("Neuspesno prijavljivanje! Preostali broj pokusaja: ", 2-i)

    return None

def registracija():
    korisnici = ucitaj_korisnike()
    korisnicko_ime = input("Unesite korisnicko ime: ")
    for korisnik in korisnici:
        if korisnik['korisnicko_ime'] == korisnicko_ime :
            print("Korisnicko ime vec postoji!Probajte ponovo! ")
            if registracija() == False:
                return False
    lozinka = input("Unesite lozinku: ")
    ime = input("Unesite ime korisnika: ")
    prezime = input("Unesite prezime korisnika: ")
    stavka = input("1.Menadzer \n2.Prodavac \nIzaberite opciju:  ")
    stavka1 = ("Menadzer")
    stavka2 = ("Prodavac")
    ret_val = {}
    ret_val['korisnicko_ime'] = korisnicko_ime
    ret_val['lozinka'] = lozinka
    ret_val['ime'] = ime
    ret_val['prezime'] = prezime
    if stavka == "1":
        ret_val['tip_korisnika'] = stavka1
    elif stavka == "2":
        ret_val['tip_korisnika'] = stavka2
    else:
        print("Greska!Izaberite ponovo!")
    korisnici.append(ret_val)
    ret_vall = [ret_val]
    list(ret_vall)
    sacuvaj_korisnika(korisnici)

def pregled_korisnika(korisnici):
    zaglavlje = f"{'korisnicko_ime':<10}{'ime':<20}{'prezime':<20}{'tip_korisnika':<20}"
    print(zaglavlje)
    print('-' * len(zaglavlje))
    for korisnik in korisnici:
        ispis = f"{korisnik['korisnicko_ime']:<10}{korisnik['ime']:<20}{korisnik['prezime']:<20}{korisnik['tip_korisnika']}"
        print(ispis)
    print('-' * len(zaglavlje))


def sortiraj_knjige(kljuc):
    korisnici = ucitaj_korisnike()

    for i in range(len(korisnici)):
        for j in range(len(korisnici)):
            if korisnici[i][kljuc] < korisnici[j][kljuc]:
                temp = korisnici[i]
                korisnici[i] = korisnici[j]
                korisnici[j] = temp
    return korisnici


def prikazi_korisnike():
    print("1.Sortiraj po imenu.")
    print("2.Sortiraj po prezimenu.")
    print("3.Sortiraj po tipu korisnika.")
    stavka = int(input("Izaberite opciju: "))
    korisnici = []
    if stavka == 1:
        korisnici = sortiraj_knjige("ime")
    elif stavka == 2:
        korisnici = sortiraj_knjige("prezime")
    elif stavka == 3:
        korisnici = sortiraj_knjige("tip_korisnika")
    else:
        print("Greska!Izaberite ponovo!")
    pregled_korisnika(korisnici)





