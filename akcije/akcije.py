from akcije.akcijeIO import ucitaj_akcije, sacuvaj_akcije
from datetime import datetime
from knjige.knjigeIO import ucitaj_knjige
import datetime


def prikaz_tabele_akcija(akcije):
    zaglavlje = f"{'sifra':<5}{'datum isteka':<10}{'naslov':<30}{'autor':<25}{'kategorija':<15}{'nova cena':<7}"
    print(zaglavlje)
    print('-' * len(zaglavlje))
    for akcija in akcije:
        ispis = f"{akcija['sifra']:<5}{akcija['datum isteka']:<10}"
        print(ispis)
        for knjiga in akcija['knjige']:
            ispis = '\t\t\t\t\t' + f" {knjiga['naslov']:<30}{knjiga['autor']:<25}{knjiga['kategorija']:<15}{knjiga['cena']:<7}"
            print(ispis)
    while True:
        print()
        print('=' * 30)
        print("1.Sortirati akcije po sifri.")
        print("2.Sortirati akcije po datumu.")
        print('=' * 30)
        stavka = input("Izaberite stavku: ")
        print('=' * 30)
        if stavka == "1":
            sortiran_prikaz_tabele_akcija(sortiraj_akcije())
            break
        elif stavka == "2":
            sortiran_prikaz_tabele_akcija(sortiraj_akcije_po_datumu())
            break
        else:
            print("Pogresan unos!")

    print('-' * len(zaglavlje))


def sortiran_prikaz_tabele_akcija(akcije):
    zaglavlje = f"{'sifra':<5}  {'datum isteka':<10}  {'naslov':<30}{'autor':<30}{'kategorija':<15}{'nova cena':<7}"

    print(zaglavlje)
    print('-' * len(zaglavlje))

    for akcija in akcije:
        ispis = f"{akcija['sifra']:<5}   {akcija['datum isteka']:<10}"
        print(ispis)
        for knjiga in akcija['knjige']:
            ispis = '\t\t\t\t\t' + f" {knjiga['naslov']:<30}{knjiga['autor']:<30}{knjiga['kategorija']:<15}{knjiga['cena']:<7}"
            print(ispis)

    print('-' * len(zaglavlje))


def sortiraj_akcije():
    akcije = ucitaj_akcije()
    for i in range(len(akcije)):
        for j in range(len(akcije)):
            if akcije[i]['sifra'] < akcije[j]['sifra']:
                temp = akcije[i]
                akcije[i] = akcije[j]
                akcije[j] = temp

    return akcije


def sortiraj_akcije_po_datumu():
    akcije = ucitaj_akcije()
    for i in range(len(akcije)):
        for j in range(len(akcije)):
            if datetime.datetime.strptime(akcije[i]['datum isteka'], "%Y-%m-%d") < datetime.datetime.strptime(
                    akcije[j]['datum isteka'], "%Y-%m-%d"):
                temp = akcije[i]
                akcije[i] = akcije[j]
                akcije[j] = temp

    return akcije


def pretraga_akcija_string(kljuc, vrednost):
    akcije = ucitaj_akcije()
    filtrirane_akcije = []
    for akcija in akcije:
        pronadjena = False
        for knjiga in akcija['knjige']:
            if vrednost.lower() in knjiga[kljuc].lower():
                pronadjena = True
                break
        if pronadjena:
            filtrirane_akcije.append(akcija)

    return filtrirane_akcije


def pretraga_akcija_jednakost(vrednost):
    akcije = ucitaj_akcije()
    filtritane_akcije = []
    for akcija in akcije:
        if vrednost == akcija['sifra']:
            filtritane_akcije.append(akcija)
    if filtritane_akcije == []:
        print("Neuspesna pretraga! Ne postoji akcija sa unetom sifrom. ")
    return filtritane_akcije


def pretrazi_akcije():
    akcije = ucitaj_akcije()
    while True:
        print()
        print('=' * 30)
        print("1. Pretraga po sifri")
        print("2. Pretraga po artiklu")
        print("3. Pretraga po autoru")
        print("4. Pretraga po kategoriji")
        print('=' * 30)
        stavka = input("Izaberite stavku: ")
        print('=' * 30)
        akcije = []
        if stavka == '1':
            sifra = int(input("Unesite sifru: "))
            akcije = pretraga_akcija_jednakost(sifra)
            break
        elif stavka == '2':
            naslov = input("Unesite naslov: ")
            akcije = pretraga_akcija_string("naslov", naslov)
            break
        elif stavka == '3':
            autor = input("Unesite autora: ")
            akcije = pretraga_akcija_string("autor", autor)
            break
        elif stavka == '4':
            kategorija = input("Unesite kategoriju:")
            akcije = pretraga_akcija_string('kategorija', kategorija)
            break
        else:
            print("Pogresan unos")
    prikaz_tabele_akcija(akcije)


def unos_cene():
    while True:
        cena = input(">>>")
        try:
            float(cena)
            return cena
        except:
            print("Nepravilan unos! Pokusajte ponovo.")


def dodavanje_akcijske_ponude():
    knjige = ucitaj_knjige()
    akcije = ucitaj_akcije()
    sifra_akcije = kreiraj_sifru_akcije(akcije)
    akcija = {}
    akcija['sifra'] = sifra_akcije
    akcija['knjige'] = []
    while True:
        sifra_knjige = input("Unesite sifru knjige ili 'x' za izlaz\n>>>")
        if sifra_knjige == 'x':
            break
        for knjiga in knjige:
            if sifra_knjige == knjiga['sifra']:
                print("Unesite cenu knjige: ")
                cena_knjige = unos_cene()
                knjiga['cena'] = float(cena_knjige)
                akcija['datum isteka'] = input("Unesite datum isteka (y-m-d): ")
                akcija['knjige'].append(knjiga)
                print("Uspesno dodavanje knjige!")
    akcije.append(akcija)
    sacuvaj_akcije(akcije)





def kreiraj_sifru_akcije(akcije):
    sifra = akcije[-1]['sifra'] + 1
    return sifra
