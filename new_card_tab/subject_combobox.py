import sys
import flash_cards_resource
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QDialog, QTabWidget, \
    QVBoxLayout, QDialogButtonBox, QLabel, QPlainTextEdit, QGroupBox, QHBoxLayout, \
    QPlainTextEdit, QLabel, QListWidget, QPushButton, QComboBox, QDialog

from PyQt5.QtGui import QIcon
from .add_new_subject_dialog import AddNewSubjectDialog
from db.db_script import SqliteConnection

class SubjectComboBox(QWidget):
    def __init__(self, parent=None):
        super(SubjectComboBox, self).__init__(parent)

        layout = QHBoxLayout()
        self.cb = QComboBox()
        # self.cb.setEditable(True)
        # self.cb.addItem("Select Subject")
        sql_conn = SqliteConnection()
        subjet = sql_conn.get_all_subjects()
        # self.cb.addItem("C")
        # self.cb.addItem("C++")
        # self.cb.addItems(["Select .....", "Java", "C#", "Python", "Add New ..."])
        self.cb.addItems(subjet)
        self.cb.setCurrentText('Select .....')
        self.cb.currentIndexChanged.connect(self.selectionchange)

        layout.addWidget(self.cb)
        self.setLayout(layout)
        self.setWindowTitle("combo box demo")
        self.cb.activated.connect(
            self.add_new_subject)

    def trigger_add_new_subject(self):
        if self.cb.currentText() == 'Add New ...':
            print("hello")
            #TODO Open new dialog window

    def selectionchange(self, i):
        print("Items in the list are :")

        for count in range(self.cb.count()):
            print(self.cb.itemText(count))
        print("Current index", i, "selection changed ", self.cb.currentText())

    def add_new_subject(self):
        if self.cb.currentText() == 'Add New ...':
            add_dialog = AddNewSubjectDialog()
            # print(add_dialog)
            # print(add_dialog.launch())
            # add button is clicked, combobox selection changes to 'select subject'

            add_dialog.exec_()
            if add_dialog.text != '':
                self.cb.setCurrentText('Select .....')
