from korisnici.korisnici import prijava, registracija, prikazi_korisnike
from knjige.knjige import prikazi_knjige, ucitaj_knjige, pretrazi_knjige, dodaj_knjige, izmeni_knjige, prodaja_knjiga, obrisi_knjigu
from akcije.akcije import prikaz_tabele_akcija, pretrazi_akcije, dodavanje_akcijske_ponude
from akcije.akcijeIO import ucitaj_akcije
from racun.racuni import kreiranje_izvestaja


def meni_administrator():
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
        print("-" * 20)
        stavka = input("Izaberite stavku:")
        print("-" * 20)
        if stavka == '1':
            prikazi_knjige()
        elif stavka == '2':
            pretrazi_knjige()
        elif stavka == '3':
            prikaz_tabele_akcija(ucitaj_akcije())
        elif stavka == '4':
            pretrazi_akcije()
        elif stavka == '5':
            registracija()
        elif stavka == '6':
            prikazi_korisnike()
        elif stavka == '7':
            dodaj_knjige()
        elif stavka == '8':
            izmeni_knjige()
        elif stavka == '9':
            obrisi_knjigu()
        elif stavka == '10':
            return
        else:
            print("Greska!Pokusajte ponovo!")


def meni_menadzer():
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
        print("-" * 20)
        stavka = input("Izaberite stavku:")
        print("-" * 20)

        if stavka == '1':
            prikazi_knjige()
        elif stavka == '2':
            pretrazi_knjige()
        elif stavka == '3':
            prikaz_tabele_akcija(ucitaj_akcije())
        elif stavka == '4':
            pretrazi_akcije()
        elif stavka == '5':
            registracija()
        elif stavka == '6':
            prikazi_korisnike()
        elif stavka == '7':
            dodavanje_akcijske_ponude()
        elif stavka == '8':
            kreiranje_izvestaja()
        elif stavka == '9':
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
        print("-" * 20)
        stavka = input("Izaberite stavku:")
        print("-" * 20)

        if stavka == '1':
            prikazi_knjige()
        elif stavka == '2':
            pretrazi_knjige()
        elif stavka == '3':
            prikaz_tabele_akcija(ucitaj_akcije())
        elif stavka == '4':
            pretrazi_akcije()
        elif stavka == '5':
            prodaja_knjiga(trenutni_korisnik['korisnicko_ime'])
        elif stavka == '6':
            dodaj_knjige()
        elif stavka == '7':
            izmeni_knjige()
        elif stavka == '8':
            obrisi_knjigu()
        elif stavka == '9':
            return
        else:
            print("Greska!Pokusajte ponovo!")


def main():
    print("=================================")
    print("Dobro dosli u nasu malu knjizaru!")
    print("=================================")
    print("\n===========Ulogujte se===========")
    print()
    ulogovani_korisnik = prijava()
    if ulogovani_korisnik is not None:
        if ulogovani_korisnik['tip_korisnika'] == 'Administrator':
            meni_administrator()
        elif ulogovani_korisnik['tip_korisnika'] == 'Prodavac':
            meni_prodavac(ulogovani_korisnik)
        elif ulogovani_korisnik['tip_korisnika'] == 'Menadzer':
            meni_menadzer()
    else:
        print('Prijava neuspesna!')
        return


main()
