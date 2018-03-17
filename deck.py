from random import shuffle


class Card:

    def __init__(self, face, suit):
        self.suit = suit

        if face == 1:
            self.face = "A"
            # this deck is only good for games with high aces
            self.value = 11
        elif face == 11:
            self.face = "J"
            self.value = 10
        elif face == 12:
            self.face = "Q"
            self.value = 10
        elif face == 13:
            self.face = "K"
            self.value = 10
        else:
            self.face = str(face)
            self.value = face


class Deck:

    def __init__(self):
        suits = ["clubs", "diamonds", "hearts", "spades"]
        cards = [Card(value, suit) for value in range(1, 14) for suit in suits]
        self.deck = cards

    def draw(self):
        shuffle(self.deck)
        return self.deck.pop()

