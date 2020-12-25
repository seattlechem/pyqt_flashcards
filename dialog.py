import sys
import flash_cards_resource
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, \
    QAction, QDialog, QTabWidget, QVBoxLayout, QDialogButtonBox,\
        QPlainTextEdit, QGroupBox, QHBoxLayout, QPlainTextEdit,\
        QListWidget, QPushButton, QComboBox, QDialog, QPushButton,\
        QGridLayout, QLineEdit
from PyQt5.QtGui import QIcon


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.button_action_connection()
        # self.pushButton.clicked.connect(self.close)

    def setupUi(self):
        # label
        subject_name = QLabel()
        subject_input = QLineEdit()
        subject_name.setText("Subject Name")
        self.buttonBox = QtWidgets.QDialogButtonBox()
        self.buttonBox.addButton("Help", QtWidgets.QDialogButtonBox.HelpRole)
        self.buttonBox.addButton("Apply", QtWidgets.QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton("Cancel", QtWidgets.QDialogButtonBox.RejectRole)
        grid_box = QGridLayout()
        grid_box.addWidget(subject_name)
        grid_box.addWidget(subject_input)
        grid_box.addWidget(self.buttonBox)
        self.setLayout(grid_box)
        # button
        # button action

    def button_action_connection(self):
        self.buttonBox.accepted.connect(self.apply_button_clicked)

    def apply_button_clicked(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())
