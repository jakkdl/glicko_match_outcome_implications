"""Calculates probability of pro- & demoting for each possible outcome of a league match, simulating the remaining matches"""
import json

from glicko2 import glicko2


def read_json(filename="data.json"):
    """read & return json file with player & match data"""
    with open(filename, encoding="utf-8") as file:
        return json.loads(file.read())


def main():
    """do all the stuff"""
    data = read_json()

    players = {p[0]: glicko2.Glicko2(*p[1:]) for p in data["players"]}
    print([(p.mu, p.phi, p.sigma) for p in players.values()])


if __name__ == "__main__":
    main()
