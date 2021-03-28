from logic import *
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import random


class Table(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Ebaniy app")

        v_default = 200
        v_offset = 10
        h_offset = 100
        curr_offset_v = v_default
        curr_offset_h = 10

        self.deck = [Card(val, suit, self) for val in range(1, 14) for suit in range(1, 5)]
        random.shuffle(self.deck)

        self.stacks = [[], [], [], [], [], [], []]

        for stack in range(len(self.stacks)):
            for c in range(stack+1):
                card = self.deck.pop()
                card.move(curr_offset_h, curr_offset_v)
                card.raise_()
                self.stacks[stack].append(card)
                curr_offset_v += v_offset
            self.stacks[stack][-1].isActive(True)
            curr_offset_h += h_offset
            curr_offset_v = v_default

        self.setGeometry(0, 0, 700, 500)


app = QApplication(sys.argv)
window = Table()
window.show()
sys.exit(app.exec_())
