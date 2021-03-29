# Klondike Solitaire by Kuznetsov V.R.
import random
from PyQt5.QtCore import pyqtSignal, Qt, QMimeData
from PyQt5.QtGui import QPixmap, QDrag, QCursor, QMouseEvent
from PyQt5.QtWidgets import QLabel


class Card(QLabel):
    bank_signal = pyqtSignal()

    def __init__(self, val, suit, parent):
        QLabel.__init__(self, parent)
        card_vals = {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q',
                     13: 'K'}

        suit_vals = {1: 'H', 2: 'D', 3: 'C', 4: 'S'}

        self.fsm = {
            1: "bank",
            2: "stack",
            3: "dump",
            4: "display"
        }
        self.active = False
        self.name = card_vals[val]
        self.suit = suit_vals[suit]
        self.full_n = f'{val}{self.suit}'
        self.val = val
        self.state = self.fsm[2]
        self.update_image()

    def set_state(self, state):
        self.state = self.fsm[state]

    def mousePressEvent(self, event):
        if self.state == "bank":
            self.bank_signal.emit()

        if self.active:
            print(f'Clicked {self.full_n}, current state: {self.state}')
        else:
            print(f'The card is hidden!, current state: {self.state}')

    def update_image(self):
        if self.active:
            pixmap = QPixmap(f'./cards/{self.full_n}.png')
        else:
            pixmap = QPixmap(f'./images/back.png')
        self.setPixmap(pixmap)

    def isActive(self, state):
        self.active = state
        self.update_image()

    def is_under(self, card):
        return self.val == card.val - 1

    def is_suit_compatible(self, card):
        if self.suit == 'Heart' or self.suit == 'Diamond':
            return card.suit == 'Spade' or card.suit == 'Club'
        else:
            return card.suit == 'Heart' or card.suit == 'Diamond'

    def is_fully_compatible(self, card):
        return self.is_under(card) and self.is_suit_compatible(card)
