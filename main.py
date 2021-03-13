from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('klondike.ui', self)
        self.tabe = self.findChild(QtWidgets.QLabel, 'table')
        self.dump_1 = self.findChild(QtWidgets.QLabel, 'dump_1')
        self.dump_2 = self.findChild(QtWidgets.QLabel, 'dump_2')
        self.dump_3 = self.findChild(QtWidgets.QLabel, 'dump_3')
        self.dump_4 = self.findChild(QtWidgets.QLabel, 'dump_4')
        self.stack_1 = self.findChild(QtWidgets.QLabel, 'stack_1')
        self.stack_2 = self.findChild(QtWidgets.QLabel, 'stack_2')
        self.stack_3 = self.findChild(QtWidgets.QLabel, 'stack_3')
        self.stack_4 = self.findChild(QtWidgets.QLabel, 'stack_4')
        self.stack_5 = self.findChild(QtWidgets.QLabel, 'stack_5')
        self.stack_6 = self.findChild(QtWidgets.QLabel, 'stack_6')
        self.stack_7 = self.findChild(QtWidgets.QLabel, 'stack_7')
        self.bank = self.findChild(QtWidgets.QLabel, 'bank')
        self.bank_items = self.findChild(QtWidgets.QLabel, 'bank_items')
        self.logo = self.findChild(QtWidgets.QLabel, 'logo')
        self.tabe.setStyleSheet("background-color: green; border: 1px solid green;")
        pixmap = QPixmap('./images/frame.png')
        self.dump_1.setPixmap(pixmap)
        self.dump_2.setPixmap(pixmap)
        self.dump_3.setPixmap(pixmap)
        self.dump_4.setPixmap(pixmap)
        self.stack_1.setPixmap(pixmap)
        self.stack_2.setPixmap(pixmap)
        self.stack_3.setPixmap(pixmap)
        self.stack_4.setPixmap(pixmap)
        self.stack_5.setPixmap(pixmap)
        self.stack_6.setPixmap(pixmap)
        self.stack_7.setPixmap(pixmap)
        self.bank.setPixmap(pixmap)
        self.bank_items.setPixmap(pixmap)
        pixmap = QPixmap('./images/logo.png')
        self.logo.setPixmap(pixmap)
        self.show()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
