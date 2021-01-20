from akcije.akcijeIO import ucitaj_akcije

def pretrazi_akcije_string(kljuc, vrednost):
    akcije = ucitaj_akcije()
    filtrirane_akcije = []
    for akcija in akcije:
        if vrednost.lower() in akcija[kljuc].lower():
            filtrirane_akcije.append(akcija)

    return filtrirane_akcije

def pretrazi_akcije_brojevi(kljuc, vrednost):
    akcije = ucitaj_akcije()
    filtrirane_akcije = []
    for akcija in akcije:
        if vrednost == akcija[kljuc]:
            filtrirane_akcije.append(akcija)

    return filtrirane_akcije

def pretrazi_akcije():
    print("1. Pretrazi po sifri.")
    print("2.Pretrazi po naslovu knjige.")
    print("3.Pretrazi po autoru knjige.")
    print("4.Pretrazi po kategoriji knjige.")

    stavka = int(input("Izaberite stavku:"))
    akcije = []
    if stavka == 1:
        sifra = input("Unesite sifru: ")
        akcije = pretrazi_akcije_brojevi('sifra', sifra)
    elif stavka == 2:
        naslov = input("Unesite naslov")
        akcije = pretrazi_akcije_string('naslov', naslov)
    elif stavka == 3:
        autor = input("Unesite autora: ")
        akcije = pretrazi_akcije_string('autor', autor)
    elif stavka == 4:
        kategorija = input("Unesite kategoriju: ")
        akcije = pretrazi_akcije_string('kategorija', kategorija)
    else:
        print("Greska!Pokusajte ponovo!")

    for akcija in akcije:
        print(akcija)



####???
