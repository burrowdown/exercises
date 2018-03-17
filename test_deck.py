import unittest
import deck


class TestCardCreation(unittest.TestCase):

    def setUp(self):
        self.king_hearts = deck.Card(13, "hearts")
        self.four_diamonds = deck.Card(4, "diamonds")
        self.ace_spades = deck.Card(1, "spades")

    def test_card_creation(self):
        self.assertEqual(self.king_hearts.suit, "hearts")
        self.assertEqual(self.four_diamonds.face, "4")
        self.assertEqual(self.ace_spades.value, 11)
        self.assertEqual(self.king_hearts.value, 10)
        self.assertEqual(self.four_diamonds.value, 4)

    def test_card_str_method(self):
        self.assertEqual(str(self.four_diamonds), '4 of diamonds')

    def test_card_repr_method(self):
        self.assertEqual(repr(self.king_hearts), 'Card (K hearts)')


class TestDeckCreation(unittest.TestCase):

    def setUp(self):
        self.card_deck = deck.Deck()
        self.first_card = deck.Card(1, "clubs")

    def test_deck_creation(self):
        self.assertEqual(len(self.card_deck), 52)
        self.assertIsInstance(self.card_deck.deck[0], deck.Card)
        self.assertEqual(str(self.card_deck.deck[0]), str(self.first_card))

    def test_deck_str_method(self):
        self.assertEqual(str(self.card_deck), 'Deck of cards with 52 cards remaining.')
        self.card_deck.draw()
        self.assertEqual(str(self.card_deck), 'Deck of cards with 51 cards remaining.')

    def test_deck_repr_method(self):
        self.assertEqual(repr(self.card_deck), 'Deck')


class TestDeckMethods(TestDeckCreation):

    def test_draw(self):
        self.assertEqual(len(self.card_deck), 52)
        self.card_deck.draw()
        self.assertEqual(len(self.card_deck), 51)

    def test_drawn_card(self):
        self.assertIsInstance(self.card_deck.draw(), deck.Card)
