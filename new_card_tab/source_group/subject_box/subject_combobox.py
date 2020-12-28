import sys
import flash_cards_resource
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QDialog, QTabWidget, \
    QVBoxLayout, QDialogButtonBox, QLabel, QPlainTextEdit, QGroupBox, QHBoxLayout, \
    QPlainTextEdit, QLabel, QListWidget, QPushButton, QComboBox, QDialog

from common.my_combo_box import ComboBox
from PyQt5.QtGui import QIcon
#from .add_new_subject_dialog import AddNewSubjectDialog
from db.db_script import SqliteConnection


class SubjectComboBox(QWidget):
    def __init__(self, parent=None):
        super(SubjectComboBox, self).__init__(parent)
        layout = QHBoxLayout()
        self.cb = ComboBox()
        self.cb.popupAboutToBeShown.connect(self.add_subject_to_combobox)

        self.subject = []

        self.cb.setCurrentText('Select .....')
        self.cb.currentIndexChanged.connect(self.selectionchange)

        layout.addWidget(self.cb)
        self.setLayout(layout)

    def show_pop_up(self):
        self.refresh_combobox.emit()

    def add_subject_to_combobox(self):
        # subject is list of tuple
        # i.e. [('Chemistry',)]
        sql_conn = SqliteConnection()
        subject = sql_conn.get_all_subjects()

        self.cb.clear()
        for subj in subject:
            self.cb.addItem(subj[0])

    def trigger_add_new_subject(self):
        if self.cb.currentText() == 'Add New ...':
            print("hello")
            # TODO Open new dialog window

    def selectionchange(self, i):
        print("Items in the list are :")

        for count in range(self.cb.count()):
            print(self.cb.itemText(count))
        print("Current index", i, "selection changed ", self.cb.currentText())

    # def add_new_subject(self):
    #     if self.cb.currentText() == 'Add New ...':
    #         add_dialog = AddNewSubjectDialog()
    #         # print(add_dialog)
    #         # print(add_dialog.launch())
    #         # add button is clicked, combobox selection changes to 'select subject'

    #         add_dialog.exec_()
    #         if add_dialog.text != '':
    #             self.cb.setCurrentText('Select .....')
