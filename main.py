from logic import *
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import random


class Table(QWidget):
    def __init__(self):
        super().__init__()

        self.v_default = 150
        self.v_offset = 10
        self.h_offset = 100
        self.curr_offset_v = self.v_default
        self.curr_offset_h = 10
        self.bank_pos_x = 10
        self.bank_pos_y = 10
        self.display_start = self.bank_pos_x + self.h_offset
        self.display_curr = self.display_start

        self.deck = [Card(val, suit, self) for val in range(1, 14) for suit in range(1, 5)]
        for card in self.deck:
            card.bank_signal.connect(self.get_bank)
        random.shuffle(self.deck)

        self.stacks = [[], [], [], [], [], [], []]

        for stack in range(len(self.stacks)):
            for c in range(stack+1):
                card = self.deck.pop()
                card.set_state(2)
                card.move(self.curr_offset_h, self.curr_offset_v)
                card.raise_()
                self.stacks[stack].append(card)
                self.curr_offset_v += self.v_offset
            self.stacks[stack][-1].isActive(True)
            self.curr_offset_h += self.h_offset
            self.curr_offset_v = self.v_default

        for card in self.deck:
            card.move(self.bank_pos_x, self.bank_pos_y)
            card.raise_()
            card.set_state(1)

        self.display = []

        self.setGeometry(3000, 250, 700, 500)
        self.setWindowTitle("Solitaire by Kuznetsov V.R.")

    def get_bank(self):
        self.display_curr = self.display_start
        for i in range(1, 4):
            if len(self.display) >= 3:
                cdisp = self.display.pop()
                cdisp.isActive(False)
                cdisp.move(self.bank_pos_x, self.bank_pos_y)
                cdisp.set_state(1)
                self.deck.insert(0, cdisp)
            card = self.deck.pop()
            card.set_state(4)
            card.isActive(True)
            card.move(self.display_curr, self.bank_pos_y)
            card.raise_()
            self.display_curr += self.v_offset*2
            self.display.insert(0, card)


app = QApplication(sys.argv)
window = Table()
window.show()
sys.exit(app.exec_())
