import json

datoteka = './datoteke/racun.json'


def sacuvaj_racune(racuni):
    with open(datoteka, "w") as f:
        json.dump(racuni , f)


def ucitaj_racune():
    with open(datoteka, "r") as f:
        return json.load(f)