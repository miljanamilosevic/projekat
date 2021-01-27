from racun.racunIO import ucitaj_racune, sacuvaj_racune
from akcije.akcijeIO import ucitaj_akcije


def ispis_knjiga(knjige, kolicine):
    zaglavlje = f"{'sifra':<7}{'naslov':<35}{'isbn':<20}{'autor':<20}{'izdavac':<20}{'broj strana':<20}{'godina':<20}{'cena':<10}{'kategorija':<20}{'kolicina':<20}{'Ukupna cena':<13}"
    print(zaglavlje)
    print('-'*len(zaglavlje))
    index = -1
    for knjiga in knjige:
        index += 1
        ispis = f"{knjiga['sifra']:<7}{knjiga['naslov']:<35}{knjiga['isbn']:<20}{knjiga['autor']:<20}{knjiga['izdavac']:<20}{knjiga['broj strana']:<20}{knjiga['godina']:<20}{knjiga['cena']:<10}{knjiga['kategorija']:<20}{kolicine[index]:<20}{str(knjiga['cena'] * kolicine[index]):<13}"
        print(ispis)
    print('-'*len(zaglavlje))





def kreiraj_akcije_od_sifre(sifre_akcija):
    sve_akcije = ucitaj_akcije()
    povratne_akcije = []
    for sifra_akcije in sifre_akcija:
        for akc in sve_akcije:
            if akc['sifra'] == sifra_akcije:
                povratne_akcije.append(akc)
                break
    return povratne_akcije


def ukupna_cena_akcije(akcija):
    cena = 0
    for knjiga in akcija['knjige']:
        cena += knjiga['cena']
    return cena

def ispis_akcija(akcije, kolicine):
    zaglavlje = f"{'sifra':<7}{'datum isteka':<14}{'naslov':<30}{'autor':<25}{'kategorija':<25}{'cena knjige':<13}{'kolicina':<10}{'Ukupna cena':<13}"

    print(zaglavlje)
    print('-' * len(zaglavlje))
    index = -1
    for akcija in akcije:
        cena_akcije = ukupna_cena_akcije(akcija)
        index += 1
        ispis = f"{akcija['sifra']:<7}{akcija['datum isteka']:<107}{kolicine[index]:<10}{str(kolicine[index] * cena_akcije):<13}"
        print(ispis)
        for knjiga in akcija['knjige']:
            ispis = '\t\t\t\t\t' + f" {knjiga['naslov']:<30}{knjiga['autor']:<25}{knjiga['kategorija']:<25}{knjiga['cena']:<13}"
            print(ispis)


def ukupna_prodaja_akcija():
    racuni = ucitaj_racune()
    akcije = []
    kolicine = []

    for racun in racuni:
        for sifra_akcije in racun['akcije']:
            is_existing = False
            for i in range(len(akcije)):
                if akcije[i] == sifra_akcije:
                    kolicine[i] += 1
                    is_existing = True
                    break
            if not is_existing:
                akcije.append(sifra_akcije)
                kolicine.append(1)
    akcije = kreiraj_akcije_od_sifre(akcije)
    ispis_akcija(akcije, kolicine)


def ukupna_prodaja_knjiga():
    racuni = ucitaj_racune()
    knjige = []
    kolicine = []

    for racun in racuni:
        for knjiga in racun['knjige']:
            is_existing = False
            for i in range(len(knjige)):
                if knjige[i]['sifra'] == knjiga['sifra']:
                    kolicine[i] += 1
                    is_existing = True
                    break

            if not is_existing:
                knjige.append(knjiga)
                kolicine.append(1)


    ispis_knjiga(knjige, kolicine)

def ukupna_prodaja_po_kljucu(kljuc, vrednost):
    racuni = ucitaj_racune()
    knjige = []
    kolicine = []

    for racun in racuni:
        for knjiga in racun['knjige']:
            if knjiga[kljuc].lower() == vrednost.lower():
                is_existing = False
                for i in range(len(knjige)):
                    if knjige[i]['sifra'] == knjiga['sifra']:
                        kolicine[i] += 1
                        is_existing = True
                        break
                if not is_existing:
                    knjige.append(knjiga)
                    kolicine.append(1)
    ispis_knjiga(knjige, kolicine)


def kreiranje_izvestaja():
    while True:
        print("1.Ukupna prodaja svih knjiga.")
        print("2.Ukupna prodaja svih akcija.")
        print("3.Ukupna prodaja svih knjiga po odredjenom kriterijumu.")
        print("x. Izlaz")
        opcija = input("Unesite opciju: ")


        if opcija == 'x':
            break
        elif opcija == '1':
            ukupna_prodaja_knjiga()

        elif opcija == '2':
            ukupna_prodaja_akcija()


        elif opcija == '3':
            while True:
                print("1. Izvestaj po autoru")
                print("2. Izvestaj po izdavacu")
                print("3. Izvestaj po kategoriji")
                opcija = input('\n>>>')

                if opcija == '1':
                    autor = input("Unesite ime autora")
                    ukupna_prodaja_po_kljucu('autor', autor)
                    break
                elif opcija == '2':
                    izdavac = input('Unesite izdavaca')
                    ukupna_prodaja_po_kljucu('izdavac', izdavac)
                    break
                elif opcija == '3':
                    kategorija = input('Unesite kategoriju')
                    ukupna_prodaja_po_kljucu('kategorija', kategorija)
                    break
                else:
                    print('Pogresna unos! Pokusajte ponovo.')
        else:
            print('Pogresan unos! Pokusajte ponovo.')