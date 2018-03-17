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

    def __str__(self):
        return '{0.face} of {0.suit}'.format(self)

    def __repr__(self):
        return '{0.__class__.__name__} ({0.face} {0.suit})'.format(self)


class Deck:

    def __init__(self):
        suits = ["clubs", "diamonds", "hearts", "spades"]
        cards = [Card(value, suit) for value in range(1, 14) for suit in suits]
        self.deck = cards

    def draw(self):
        shuffle(self.deck)
        return self.deck.pop()

    def __str__(self):
        return 'Deck of cards with {0} cards remaining.'.format(len(self.deck))

    def __repr__(self):
        return '{0.__class__.__name__}'.format(self)