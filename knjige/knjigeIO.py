import json

datoteka = './datoteke/knjige.json'

def sacuvaj_knjige(nove_knjige):
    with open(datoteka, "w") as f:
        json.dump(nove_knjige , f, indent=4, sort_keys=True)


def ucitaj_knjige():
    with open(datoteka, "r") as f:
        return json.load(f)



