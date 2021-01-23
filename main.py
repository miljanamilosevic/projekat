from korisnici.korisnici import prijava, registracija
from knjige.knjige import prikazi_knjige, ucitaj_knjige, pretrazi_knjige, dodaj_knjige, izmeni_knjige, prodaja_knjiga
from akcije.akcije import pretrazi_akcije

def meni_administrator(trenutni_korisnik):
    while True:
        print('\n1.Prikaz svih knjiga')
        print('2.Pretraga knjiga')
        print('3. Prikaz svih akcija')
        print('4. Pretraga akcija')
        print('5.Registracija')
        print('6.Prikaz svih korisnika')
        print('7.Dodavanje knjige')
        print('8.Izmena knjiga')
        print('9.Brisanje knjige')
        print('10. Kraj')

        stavka = int(input("Izaberite stavku:"))

        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            pass
        elif stavka == 4:
            pretrazi_akcije()
        elif stavka == 5:
            registracija()
        elif stavka == 6:
            pass
        elif stavka == 7:
            dodaj_knjige()
        elif stavka == 8:
            izmeni_knjige()
        elif stavka == 9:
            pass
        elif stavka == 10:
            return
        else:
            print("Greska!Pokusajte ponovo!")

def meni_menadzer(trenutni_korisnik):
    while True:
        print('\n1.Prikaz svih knjiga')
        print('2.Pretraga knjiga')
        print('3. Prikaz svih akcija')
        print('4. Pretraga akcija')
        print('5.Registracija')
        print('6.Prikaz svih korisnika')
        print('7.Dodavanje akcijske ponude')
        print('8.Kreiranje izvestaja')
        print('9. Kraj')

        stavka = int(input("Izaberite stavku:"))

        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            pass
        elif stavka == 4:
            pass
        elif stavka == 5:
            pass
        elif stavka == 6:
            pass
        elif stavka == 7:
            pass
        elif stavka == 8:
            pass
        elif stavka == 9:
            return
        else:
            print("Greska!Pokusajte ponovo!")

def meni_prodavac(trenutni_korisnik):
    while True:
        print('\n1. Prikaz svih knjiga')
        print('2. Pretraga knjiga')
        print('3. Prikaz svih akcija')
        print('4. Pretraga akcija')
        print('5. Prodaja knjiga')
        print('6. Dodavanje knjige')
        print('7. Izmena knjige')
        print('8. Brisanje knjige')
        print('9. Kraj')

        stavka = int(input("Izaberite stavku:"))

        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            pass
        elif stavka == 4:
            pass
        elif stavka == 5:
            prodaja_knjiga(trenutni_korisnik['korisnicko_ime'])
        elif stavka == 6:
            dodaj_knjige()
        elif stavka == 7:
            pass
        elif stavka == 8:
            pass
        elif stavka == 9:
            return
        else:
            print("Greska!Pokusajte ponovo!")

def main():
    ulogovani_korisnik = prijava()
    if ulogovani_korisnik is not None:
        if ulogovani_korisnik['tip_korisnika'] == 'Administrator':
            meni_administrator(ulogovani_korisnik)
        elif ulogovani_korisnik['tip_korisnika'] == 'Prodavac':
            meni_prodavac(ulogovani_korisnik)
        elif ulogovani_korisnik['tip_korisnika'] == 'Menadzer':
            meni_menadzer(ulogovani_korisnik)
    else:
        print('Prijava neuspesna!')
        return


main()