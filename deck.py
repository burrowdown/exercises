from random import shuffle


class Card:

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

        if face == 1:
            self.face = "A"
        elif face == 11:
            self.face = "J"
        elif face == 12:
            self.face = "Q"
        elif face == 13:
            self.face = "K"
        else:
            self.face = str(face)


class Deck:

    def __init__(self):
        suits = ["clubs", "diamonds", "hearts", "spades"]
        cards = [Card(value, suit) for value in range(1, 14) for suit in suits]
        self.deck = cards

    def draw(self):
        shuffle(self.deck)
        return self.deck.pop()

