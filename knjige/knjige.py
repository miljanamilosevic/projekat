from knjige.knjigeIO import ucitaj_knjige

def pretrazi_knjige_string(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []
    for knjiga in knjige:
        if vrednost.lower() in knjiga[kljuc].lower():
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige

def pretrazi_knjige_brojevi(kljuc, vrednost):
    knjige = ucitaj_knjige()                                      ##jos jedna funkcija za range da li je u nekom opsegu, ali umesto jednako poredimo sa vece ili manje
    filtrirane_knjige = []
    for knjiga in knjige:
        if vrednost == knjiga[kljuc]:
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige


def pretrazi_knjige():
    print("1. Pretrazi po naslovu")  ##prepravi sve
    print("2.Po kategoriji")
    print("3.po autoru")
    print("4.po izdavacu")
    print("5. po ceni")

    stavka = int(input("Izaberite stavku:"))
    knjige = []
    if stavka == 1:
        naslov = input("Unesite naslov")
        knjige = pretrazi_knjige_string('naslov', naslov)  #dodaj elif za sve ostalo

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
    print("1. Sortiraj po naslovu")
    print("2.Po kategoriji")
    print("3.po autoru")
    print("4.po izdavacu")
    print("5. po ceni")  #popravi pisanje

    stavka = int(input("Izaberite stavku: "))

    knjige = []

    if stavka == 1:
        knjige = sortiraj_knjige("naslov")
    elif stavka == 2:
        knjige = sortiraj_knjige("kategorija")
        #itd

    #ispis sa formatom itd,tabela
    for knjiga in knjige:
        print(knjiga)