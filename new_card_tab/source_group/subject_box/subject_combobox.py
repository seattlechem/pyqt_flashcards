from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from common.my_combo_box import ComboBox
from db.db_script import SqliteConnection

cb = None


class SubjectComboBox(QWidget):
    def __init__(self, parent=None):
        super(SubjectComboBox, self).__init__(parent)
        self.setupUI()
        cb.currentIndexChanged.connect(self.selectionchange)
        cb.popupAboutToBeShown.connect(cb.add_subject_to_combobox)

    def setupUI(self):
        layout = QHBoxLayout()

        global cb
        cb = ComboBox()

        self.subject = []
        cb.clear()
        # self.add_subject_to_combobox()
        cb.add_subject_to_combobox()
        cb.setCurrentIndex(0)

        layout.addWidget(cb)
        self.setLayout(layout)

    def show_pop_up(self):
        self.refresh_combobox.emit()

    def trigger_add_new_subject(self):
        if cb.currentText() == 'Add New ...':
            print("hello")
            # TODO Open new dialog window

    def selectionchange(self, i):
        print("Items in the list are :")

        for count in range(cb.count()):
            print(cb.itemText(count))
        print("Current index", i, "selection changed ", cb.currentText())
