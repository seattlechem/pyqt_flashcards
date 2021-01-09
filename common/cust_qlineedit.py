from PyQt5.QtWidgets import QLineEdit

class CustQLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setStyleSheet("color: white; background-color: black")
