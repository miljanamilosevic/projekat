from korisnici.korisniciIO import ucitaj_korisnike



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


