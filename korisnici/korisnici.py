from korisnici.korisniciIO import ucitaj_korisnike



def prijava():
    korisnici = ucitaj_korisnike()

    korisnicko_ime = input("korisnicko ime:")
    lozinka = input("lozinka:")

    for korisnik in korisnici:
        if korisnik['korisnicko_ime'] == korisnicko_ime and korisnik['lozinka'] == lozinka:
            return korisnik
    return None
#ponovi tri puta?while ili for petlja

