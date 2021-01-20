from knjige.knjigeIO import ucitaj_knjige

def pregled_knjiga(knjige):
    zaglavlje = f"{'sifra':<5}{'naslov':<35}{'isbn':<20}{'autor':<20}{'izdavac':<20}{'broj strana':<20}{'godina':<20}{'cena':<10}{'kategorija':<20}"
    print(zaglavlje)
    print('-'*len(zaglavlje))
    for knjiga in knjige:
        ispis = f"{knjiga['sifra']:<5}{knjiga['naslov']:<35}{knjiga['isbn']:<20}{knjiga['autor']:<20}{knjiga['izdavac']:<20}{knjiga['broj strana']:<20}{knjiga['godina']:<20}{knjiga['cena']:<10}{knjiga['kategorija']:<20}"
        print(ispis)
    print('-'*len(zaglavlje))


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
    print("6.Pretrazi po opsegu cene.") ######

    stavka = int(input("Izaberite stavku:"))
    knjige = []
    if stavka == 1:
        sifra = input("Unesite sifru: ")
        knjige = pretrazi_knjige_brojevi('sifra', sifra)
    elif stavka == 2:
        naslov = input("Unesite naslov")
        knjige = pretrazi_knjige_string('naslov', naslov)
    elif stavka == 3:
        autor = input("Unesite autora: ")
        knjige = pretrazi_knjige_string('autor', autor)
    elif stavka == 4:
        kategorija = input("Unesite kategoriju: ")
        knjige = pretrazi_knjige_string('kategorija', kategorija)
    elif stavka == 5:
        izdavac = input("Unesite izdavaca: ")
        knjige = pretrazi_knjige_string('izdavac',izdavac)
    elif stavka == 6:
        cena1 = int(input("Unesite minimalnu cenu: "))
        cena2 = int(input("Unesite maksimalnu cenu: "))
        if cena2 < cena1:
            knjige = pretrazi_knjige_opseg('cena', cena2, cena1)
        else:
            knjige = pretrazi_knjige_opseg('cena', cena1, cena2)
    else:
        print("Greska!Pokusajte ponovo!")

    for knjiga in knjige:
        print(knjiga)     #prikaz knjiga


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

    stavka = int(input("Izaberite opciju: "))

    knjige = []

    if stavka == 1:
        knjige = sortiraj_knjige("naslov")
    elif stavka == 2:
        knjige = sortiraj_knjige("kategorija")
    elif stavka == 3:
        knjige = sortiraj_knjige("autor")
    elif stavka == 4:
        knjige = sortiraj_knjige("izdavac")
    elif stavka == 5:
        knjige = sortiraj_knjige("cena")
    else:
        print("Greska!Izaberite ponovo!")

    pregled_knjiga(knjige)


def provera(knjige, sifra):
    for knjiga in knjige:
        if knjiga["sifra"] == sifra:
            return knjiga


def dodaj_knjige():
    knjige = ucitaj_knjige()
    while True:
        knjiga = {}
        knjiga["sifra"] = input("Unesite novu sifru: ")

        knjiga["naslov"] = input("Unesite naslov knjige: ")
        knjiga["isbn"] = input("Unesite isbn: ")
        knjiga["autor"] = input("Unesite autora: ")
        knjiga["izdavac"] = input("Unesite izdavaca: ")
        knjiga["broj strana"] = int(input("Unesite koliko strana ima knjiga: "))
        knjiga["godina"] = int(input("Unesite godinu izdavanja: "))
        knjiga["cena"] = float(input("Unesite cenu knjige: "))
        knjiga["kategorija"] = input("Unesite kojoj kategoriji pripada knjiga: ")
        if provera(knjige, knjiga["sifra"]) is None:
            knjige.append(knjiga)
            break
        else:
            print("\nKnjiga sa unetom sifrom vec postoji!Probajte ponovo!")
        ###kako da cuva knjige u json fajl, da ovo pise posle sifre

