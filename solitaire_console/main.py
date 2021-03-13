# Klondike Solitaire by Kuznetsov V.R.
import random
from PyQt5 import QtWidgets
import PyQt5.QtGui


class Card():
    """
    Card class that can hold its value and a suit.

    :parameter val: Holds a value of a card in range (1:13).
    :parameter name: Name of a card, for example - 'Q'.
    :parameter full_n: Full name of a card, for example - 'J Club'.
    :parameter suit: Suit of a card, for example - 'Heart'.
    """

    card_vals = {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q',
                 13: 'K'}

    suit_vals = {1: 'Heart', 2: 'Diamond', 3: 'Club', 4: 'Spade'}

    def __init__(self, val, suit):
        self.name = self.card_vals[val]
        self.suit = self.suit_vals[suit]
        self.full_n = f'{self.name} {self.suit}'
        self.val = val

    def __str__(self):
        return self.full_n

    def is_under(self, card):
        """
        Checks if given card is on top of self.

        :param card: Card to compare with.
        :return: True if the card is under a given card by value.
        """
        return self.val == card.val - 1

    def is_suit_compatible(self, card):
        """
        Check for suit compatibility.

        :param card: Card to compare with.
        :return: bool object, that indicates if given card is compatible.
        """

        if self.suit == 'Heart' or self.suit == 'Diamond':
            return card.suit == 'Spade' or card.suit == 'Club'
        else:
            return card.suit == 'Heart' or card.suit == 'Diamond'

    def is_fully_compatible(self, card):
        """
        Checks for full compatibility with a given card.

        :param card: Card to compare with.
        :return: bool object, True if given card is fully compatible.
        """

        return self.is_under(card) and self.is_suit_compatible(card)


class Deck:
    """
    Class that generates a deck of cards.
    """

    deck_generator = [Card(val, suit) for val in range(1, 14) for suit in range(1, 5)]

    def __init__(self):
        self.deck = self.deck_generator
        random.shuffle(self.deck)

    def pop_card(self):
        """
        Pops a card from the deck.

        :return: Card object.
        """
        return self.deck.pop()


class Stack:
    """
    Class that holds a set number of cards and has a string representation.
    """
    def __init__(self, deck, num_of_cards):
        self.cards = []
        self.name = num_of_cards
        for c in range(num_of_cards):
            self.cards.append(deck.pop_card())

    def __str__(self):
        result = f'Stack {self.name}:\nCards in this stack: {len(self.cards)}\nTop most card: {self.cards[-1]}\n'
        return result

    def add_card(self, card):
        """
        Add a card to the list.
        :param card:
        :return:
        """
        self.cards.append(card)


class Table:
    def __init__(self, num_of_stacks=7):
        self.deck = Deck()
        self.stacks = []
        for s in range(num_of_stacks):
            self.stacks.append(Stack(self.deck, s+1))


if __name__ == "__main__":
    t = Table()
    for st in t.stacks:
        print(st)
    print('Number of cards left: ', len(t.deck.deck))
