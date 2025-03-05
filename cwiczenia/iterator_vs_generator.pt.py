"""


["A", "B", "C"]

("A", "B")
("A", "C")

"""

from itertools import permutations

def tournament1(players):
    for i, player1 in enumerate(players):
        for j, player2 in enumerate(players):
            if i != j:
                yield player1, player2


def tournament2(players):
    for p1, p2 in permutations(players, 2):
        yield p1, p2


t = tournament1(["A", "B", "C"])
t2 = tournament2(["A", "B", "C"])
print(next(t))
print(next(t2))

print(next(t))
print(next(t2))


class Tournament:

    def __init__(self, players):
        self.players = players
        self.player1_idx = 0
        self.player2_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.player1_idx >= len(self.players):
            raise StopIteration

        while self.player1_idx == self.player2_idx:
            self.player2_idx += 1
            if self.player2_idx >= len(self.players):
                self.player1_idx += 1
                self.player2_idx = 0
                if self.player1_idx >= len(self.players):
                    raise StopIteration

        player1 = self.players[self.player1_idx]
        player2 = self.players[self.player2_idx]

        self.player2_idx += 1
        if self.player2_idx >= len(self.players):
            self.player1_idx += 1
            self.player2_idx = 0

        return player1, player2

t = Tournament(["A", "B", "C"])
print(next(t))
print(next(t))
print(next(t))
print(next(t))


