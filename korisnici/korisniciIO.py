import json

datoteka = './datoteke/korisnici.json'

def sacuvaj_korisnika(korisnici):
    with open(datoteka, "w") as f:
        json.dump(korisnici, f)


def ucitaj_korisnike():
    with open(datoteka, "r") as f:
        return json.load(f)

