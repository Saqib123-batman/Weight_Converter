import sys

from PyQt6.QtWidgets import QLabel, QLineEdit, QMainWindow, QApplication, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUi


class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()
        loadUi("weight_converter.ui", self)
        self.show()
        self.setWindowTitle("Weight Converter App")
        self.setWindowIcon(QIcon("weight_icon.jpg"))

        # define our widgets

        self.weight_label = self.findChild(QLabel, "weight_label")
        self.label = self.findChild(QLabel, "label")
        self.input_weight = self.findChild(QLineEdit, "input_weight")
        self.kg_to_lb = self.findChild(QPushButton, "kg_to_lb")
        self.lb_to_kg = self.findChild(QPushButton, "lb_to_kg")

        # do something
        self.lb_to_kg.clicked.connect(self.kilogram)
        self.kg_to_lb.clicked.connect(self.pounds)

    def kilogram(self):
        weight = int(self.input_weight.text())
        result = weight * 0.45
        self.weight_label.setText("Weight in Kg: {}".format(result))

    def pounds(self):
        weight = int(self.input_weight.text())
        result = weight * 2.2
        self.weight_label.setText("Weight in lb: {}".format(result))


app = QApplication(sys.argv)
UIwindow = UI()
sys.exit(app.exec())