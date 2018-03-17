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