import json

datoteka = './datoteke/racun.json'


def sacuvaj_racune(racuni):
    with open(datoteka, "w") as f:
        json.dump(racuni , f, indent=4, sort_keys=True)


def ucitaj_racune():
    with open(datoteka, "r") as f:
        return json.load(f)