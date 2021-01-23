from akcije.akcijeIO import ucitaj_akcije
import datetime

def prikaz_tabele_akcija(akcije):
    zaglavlje = f"{'sifra':<5}{'datum vazenja':<10}{'naslov':<30}{'autor':<25}{'kategorija':<15}{'nova cena':<7}"

    print(zaglavlje)
    print('-'*len(zaglavlje))

    for akcija in akcije:
        ispis = f"{akcija['sifra']:<5}{akcija['datum vazenja']:<10}"
        print(ispis)
        for knjiga in akcija['knjige'].keys():
            ispis = '\t\t\t\t\t' + f" {akcija['knjige'][knjiga]['naslov']:<30}{akcija['knjige'][knjiga]['autor']:<25}{akcija['knjige'][knjiga]['kategorija']:<15}{akcija['knjige'][knjiga]['nova cena']:<7}"
            print(ispis)

    print('\n1.Sortirati akcije po sifri.')
    print('2.Sortirati akcije po datumu.')
    stavka = input("Izaberite stavku: ")
    print('***' * 20)
    if stavka == "1":
        sortiran_prikaz_tabele_akcija(sortiraj_akcije('sifra'))
    elif stavka == "2":
        sortiran_prikaz_tabele_akcija(sortiraj_akcije_po_datumu())
    else:
        print("Pogresan unos!")
        return
    print('-'*len(zaglavlje))

def sortiran_prikaz_tabele_akcija(akcije):

    zaglavlje = f"{'sifra':<5}  {'datum vazenja':<10}  {'naslov':<30}{'autor':<30}{'kategorija':<15}{'nova cena':<7}"

    print(zaglavlje)
    print('-'*len(zaglavlje))

    for akcija in akcije:
        ispis = f"{akcija['sifra']:<5}   {akcija['datum vazenja']:<10}"
        print(ispis)
        for knjiga in akcija['knjige'].keys():
            ispis = '\t\t\t\t\t' + f" {akcija['knjige'][knjiga]['naslov']:<30}{akcija['knjige'][knjiga]['autor']:<30}{akcija['knjige'][knjiga]['kategorija']:<15}{akcija['knjige'][knjiga]['nova cena']:<7}"
            print(ispis)

    print('-'*len(zaglavlje))

def sortiraj_akcije(kljuc):
    akcije = ucitaj_akcije()

    for i in range(len(akcije)):
        for j in range(len(akcije)):
            if akcije[i][kljuc] < akcije[j][kljuc]:
                temp = akcije[i]
                akcije[i] = akcije[j]
                akcije[j] = temp

    return akcije

def sortiraj_akcije_po_datumu():
    akcije = ucitaj_akcije()

    for i in range(len(akcije)):
        for j in range(len(akcije)):
            if datetime.datetime.strptime(akcije[i]['datum vazenja'], "%Y-%m-%d") < datetime.datetime.strptime(akcije[j]['datum vazenja'], "%Y-%m-%d"):
                temp = akcije[i]
                akcije[i] = akcije[j]
                akcije[j] = temp

    return akcije

def pretraga_akcija_string(kljuc, vrednost):
    akcije = ucitaj_akcije()
    filtrirane_akcije = []

    for akcija in akcije:
        pronadjena = False
        for knjiga in akcija['knjige'].keys():
            if vrednost.lower() in akcija['knjige'][knjiga][kljuc].lower():
                pronadjena = True
                break
        if pronadjena:
            filtrirane_akcije.append(akcija)

    return filtrirane_akcije


def pretraga_akcija_jednakost(kljuc,vrednost):
    akcije = ucitaj_akcije()
    filtritane_akcije=[]

    for akcija in akcije:
        if vrednost == akcija[kljuc]:
            filtritane_akcije.append(akcija)
    return filtritane_akcije


def pretrazi_akcije():
    akcije = ucitaj_akcije()
    print('-' * 20)
    print("\n1. Pretraga po sifri")
    print("2. Pretraga po artiklu")
    print("3. Pretraga po autoru")
    print("4. Pretraga po kategoriji")
    print('-' * 20)
    stavka = input("Izaberite stavku: ")
    print('-' * 20)
    akcije = []
    if stavka == '1':
        sifra = int(input("Unesite sifru: "))
        akcije = pretraga_akcija_jednakost("sifra", sifra)
    elif stavka == '2':
        naslov = input("Unesite naslov: ")
        akcije =pretraga_akcija_string("naslov", naslov)
    elif stavka == '3':
        autor = input("Unesite autora: ")
        akcije = pretraga_akcija_string("autor", autor)
    elif stavka == '4':
        kategorija = input("Unesite kategoriju:")
        akcije = pretraga_akcija_string('kategorija', kategorija)
    else:
        print("Pogresan unos")
        return

    prikaz_tabele_akcija(akcije)


