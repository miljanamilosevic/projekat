import json

datoteka = './datoteke/knjige.json'

def sacuvaj_knjige(korisnici):
    with open(datoteka, "w") as f:
        json.dump(korisnici, f)


def ucitaj_knjige():
    with open(datoteka, "r") as f:
        return json.load(f)

