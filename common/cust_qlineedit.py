from PyQt5.QtWidgets import QLineEdit

class CustQLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.setStyleSheet("color: white; background-color: black")
