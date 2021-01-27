from knjige.knjigeIO import ucitaj_knjige, sacuvaj_knjige
from racun.racunIO import sacuvaj_racune, ucitaj_racune
from akcije.akcijeIO import ucitaj_akcije
from datetime import datetime, date
from akcije.akcije import unos_cene


def kreiraj_sifru_racuna(racuni):
    sifra = racuni[-1]['sifra'] + 1
    return sifra


def unos_kolicine():
    try:
        kolicina = int(input("Unesite kolicinu izabrane knjige:\n>>>"))
        return kolicina
    except:
        print('Pogresan unos! Postavljena podrazumevana kolicina - 1')
        return 1


def prodaja_preko_sifre(racun):
    knjige = ucitaj_knjige()
    i = 1
    for knjiga in knjige:
        print("{0} - {1}".format(i, knjiga["sifra"]))
        i += 1
    while True:
        sifra = input("Unesite sifru knjige ili 'x' za izlaz\n>>>")
        if sifra == 'x':
            break
        for knjiga in knjige:
            if knjiga['sifra'] == sifra:
                kolicina = unos_kolicine()
                for i in range(0, kolicina):
                    racun['knjige'].append(knjiga)
                    racun['ukupna cena'] += knjiga['cena']


def prodaja_preko_akcije(racun):
    akcije = ucitaj_akcije()
    i = 1
    for akcija in akcije:

        print("{0} - {1}".format(i, akcija["sifra"]))
        i += 1
    while True:
        sifra = input("Unesite sifru akcije ili 'x' za izlaz\n>>>")
        if sifra == 'x':
            break
        for akcija in akcije:
            if akcija['sifra'] == int(sifra):
                if datetime.strptime(akcija['datum isteka'], "%Y-%m-%d") > datetime.strptime(str(date.today()), "%Y-%m-%d"):
                    racun['akcije'].append(akcija['sifra'])
                    for knjiga in akcija['knjige']:
                        racun['knjige'].append(knjiga)
                        racun['ukupna cena'] += knjiga['cena']
                else:
                    print("Akcija je istekla :(")


def prikaz_korpe(racun):
    pregled_knjiga(racun['knjige'])
    print("Ukupna cena", racun['ukupna cena'])


def prodaja_knjiga(trenutni_korisnik):
    racuni = ucitaj_racune()
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M")
    racun = {}
    racun['sifra'] = kreiraj_sifru_racuna(racuni)
    racun['prodavac'] = trenutni_korisnik
    racun['knjige'] = []
    racun['datum'] = date_time
    racun['ukupna cena'] = 0
    racun['akcije'] = []
    while True:
        print("1 - Unos sifri")
        print("2 - Unos akcije")
        print("3 - Prikaz korpe")
        print("4 - Zavrsi prodaju")
        print("x - Odustani od prodaje\n")
        unos = input(">>>")
        if unos == '4':
            break
        elif unos == '1':
            prodaja_preko_sifre(racun)
        elif unos == '2':
            prodaja_preko_akcije(racun)
        elif unos == '3':
            prikaz_korpe(racun)
        elif unos == 'x':
            return
        else:
            print("Pogresan unos! Pokusajte ponovo")
    racuni.append(racun)
    sacuvaj_racune(racuni)


def pregled_knjiga(knjige):
    zaglavlje = f"{'sifra':<5}{'naslov':<35}{'isbn':<20}{'autor':<20}{'izdavac':<20}{'broj strana':<20}{'godina':<20}{'cena':<10}{'kategorija':<20}"
    print(zaglavlje)
    print('-' * len(zaglavlje))
    for knjiga in knjige:
        ispis = f"{knjiga['sifra']:<5}{knjiga['naslov']:<35}{knjiga['isbn']:<20}{knjiga['autor']:<20}{knjiga['izdavac']:<20}{knjiga['broj strana']:<20}{knjiga['godina']:<20}{knjiga['cena']:<10}{knjiga['kategorija']:<20}"
        print(ispis)
    print('-' * len(zaglavlje))


def pretrazi_knjige_string(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []
    for knjiga in knjige:
        if vrednost.lower() in knjiga[kljuc].lower():
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige


def pretrazi_knjige_brojevi(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []
    for knjiga in knjige:
        if vrednost == knjiga[kljuc]:
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige


def pretrazi_knjige_opseg(kljuc, cenamin, cenamax):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []
    for knjiga in knjige:
        if cenamin <= knjiga[kljuc] and cenamax >= knjiga[kljuc]:
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige


def pretrazi_knjige():
    print("1. Pretrazi po sifri.")
    print("2.Pretrazi po naslovu.")
    print("3.Pretrazi po autoru.")
    print("4.Pretrazi po kategoriji.")
    print("5. Pretrazi po izdavacu.")
    print("6.Pretrazi po opsegu cene.")  ######

    stavka = input("Izaberite stavku:")
    knjige = []
    if stavka == '1':
        sifra = input("Unesite sifru: ")
        knjige = pretrazi_knjige_brojevi('sifra', sifra)
    elif stavka == '2':
        naslov = input("Unesite naslov")
        knjige = pretrazi_knjige_string('naslov', naslov)
    elif stavka == '3':
        autor = input("Unesite autora: ")
        knjige = pretrazi_knjige_string('autor', autor)
    elif stavka == '4':
        kategorija = input("Unesite kategoriju: ")
        knjige = pretrazi_knjige_string('kategorija', kategorija)
    elif stavka == '5':
        izdavac = input("Unesite izdavaca: ")
        knjige = pretrazi_knjige_string('izdavac', izdavac)
    elif stavka == '6':
        print('Unesite minimalnu cenu')
        cena1 = unos_cene()
        print("Unesite maksimalnu cenu")
        cena2 = unos_cene()
        if cena2 < cena1:
            knjige = pretrazi_knjige_opseg('cena', cena2, cena1)
        else:
            knjige = pretrazi_knjige_opseg('cena', cena1, cena2)
    else:
        print("Greska!Pokusajte ponovo!")

    for knjiga in knjige:
        print(knjiga)  ##prikazi knjige


def sortiraj_knjige(kljuc):
    knjige = ucitaj_knjige()

    for i in range(len(knjige)):
        for j in range(len(knjige)):
            if knjige[i][kljuc] < knjige[j][kljuc]:
                temp = knjige[i]
                knjige[i] = knjige[j]
                knjige[j] = temp
    return knjige


def prikazi_knjige():
    print("1.Sortiraj po naslovu knjige.")
    print("2.Sortiraj po kategoriji.")
    print("3.Sortiraj po autoru.")
    print("4.Sortiraj po izdavacu.")
    print("5.Sortiraj po ceni.")
    stavka = input("Izaberite opciju: ")
    knjige = []
    if stavka == '1':
        knjige = sortiraj_knjige("naslov")
    elif stavka == '2':
        knjige = sortiraj_knjige("kategorija")
    elif stavka == '3':
        knjige = sortiraj_knjige("autor")
    elif stavka == '4':
        knjige = sortiraj_knjige("izdavac")
    elif stavka == '5':
        knjige = sortiraj_knjige("cena")
    else:
        print("Greska!Izaberite ponovo!")
    pregled_knjiga(knjige)


def dodaj_knjige():
    ####
    knjige = ucitaj_knjige()
    while True:
        sifra = input("Unesite sifru:")
        postoji = False
        for knjiga in knjige:
            if knjiga['sifra'] == sifra:
                print('Knjiga sa unetom sifrom vec postoji!Probajte ponovo!')
                postoji = True
                break
        if not postoji:
            break

    naslov = input('Unesite naslov knjige: ')
    autor = input('Unesite autora knjige: ')
    isbn = input('ISBN: ')
    izdavac = input('Unesite izdavaca: ')
    godina = int(input('Unesite godinu izdavanja: '))
    cena = float(input('Unesite cenu knjige: '))
    kategorija = input('Unesite kojoj kategoriji knjiga pripada: ')
    broj_strana = int(input('Unesite koliko strana ima knjiga: '))
    nova_knjiga = {}
    nova_knjiga['sifra'] = sifra
    nova_knjiga['naslov'] = naslov
    nova_knjiga['isbn'] = isbn
    nova_knjiga['autor'] = autor
    nova_knjiga['izdavac'] = izdavac
    nova_knjiga['broj strana'] = broj_strana
    nova_knjiga['cena'] = cena
    nova_knjiga['godina'] = godina
    nova_knjiga['kategorija'] = kategorija
    while True:
        print("\nDa li zelite da nastavite?\n1. Da\n2. Ne ")
        stavka = input('Izaberite stavku: ')
        if (stavka == '1'):
            print("Nova knjiga je dodata u bazu. ")
            knjige.append(nova_knjiga)
            break
        elif (stavka == '2'):
            return False
        else:
            print("Greska!Pokusajte ponovo!")
    sacuvaj_knjige(knjige)


def izmeni_knjige():
    ####
    knjige = ucitaj_knjige()

    while True:
        sifra = input("Unesite sifru:")
        postoji = False
        i = -1
        for knjiga in knjige:
            i += 1
            if knjiga['sifra'] == sifra:
                print("Knjiga uspesno pronadjena!")
                postoji = True
                break
        if not postoji:
            print("Knjiga sa unetom sifrom nije pronadjena!")
        else:
            break

    izmena = knjige[i]
    z = i
    izmene = [izmena]
    list(izmene)
    print("Ako ne zelite da promenite neku vrednost, ostavite prazno polje.")
    naslov = input("\nIzmenite naslov: ")
    if (naslov == " "):
        naslov = knjige[i]['naslov']
    autor = input("Izmenite autora: ")
    if (autor == " "):
        autor = knjige[i]['autor']
    isbn = input("Izmenite ISBN: ")
    if (isbn == " "):
        isbn = knjige[i]['isbn']
    izdavac = input("Izmenite izdavaca: ")
    if (izdavac == " "):
        publisher = knjige[i]['izdavac']
    godina = int(input("Izmenite godinu: "))
    if (godina == " "):
        godina = knjige[i]['godina']
    cena = float(input("Izmenite cenu: "))
    if (cena == " "):
        cena = knjige[i]['cena']
    kategorija = input("Izmenite kategoriju knjige: ")
    if (kategorija == ''):
        kategorija = knjige[i]['kategorija']
    broj_strana = int(input("Izmenite broj strana: "))
    if (broj_strana == " "):
        broj_strana = knjige[i]['broj strana']
    nova_knjiga = {}
    nova_knjiga['sifra'] = sifra
    nova_knjiga['naslov'] = naslov
    nova_knjiga['autor'] = autor
    nova_knjiga['isbn'] = isbn
    nova_knjiga['izdavac'] = izdavac
    nova_knjiga['godina'] = godina
    nova_knjiga['cena'] = cena
    nova_knjiga['kategorija'] = kategorija
    nova_knjiga['broj strana'] = broj_strana
    izmene = [knjige[z], nova_knjiga]
    list(izmene)
    while True:
        print("\nDa li zelite da nastavite?\n1. Da\n2. Ne")
        stavka = input("Izaberite stavku: ")
        if (stavka == '1'):
            knjige[z] = nova_knjiga
            break
        elif (stavka == '2'):
            return False
        else:
            print("Greska!Pokusajte ponovo! ")

    sacuvaj_knjige(knjige)
    return False
