from logic import *
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import random


class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()

        self.setWindowTitle("My Ebaniy app")
        layout = QHBoxLayout()

        v_offset = 10
        h_offset = 100
        curr_offset_v = 10
        curr_offset_h = 10

        self.deck = [Card(val, suit) for val in range(1, 14) for suit in range(1, 5)]
        random.shuffle(self.deck)

        self.stacks = [[], [], [], [], [], [], []]

        for stack in range(len(self.stacks)):
            for c in range(stack+1):
                self.stacks[stack].append(self.deck.pop())
            self.stacks[stack][-1].isActive(True)

        for stack in self.stacks:
            for card in stack:
                card.move(curr_offset_h, curr_offset_v)
                layout.addWidget(card)
                curr_offset_v += v_offset
                curr_offset_h += h_offset

        self.setLayout(layout)
        self.setGeometry(300, 300, 250, 150)


app = QApplication(sys.argv)
window = Table()
window.show()
sys.exit(app.exec_())