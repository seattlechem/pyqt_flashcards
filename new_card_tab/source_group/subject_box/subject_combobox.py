from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from common.my_combo_box import ComboBox
from db.db_script import SqliteConnection

cb = None
class SubjectComboBox(QWidget):
    def __init__(self, parent=None):
        super(SubjectComboBox, self).__init__(parent)
        layout = QHBoxLayout()

        global cb
        cb = ComboBox()
        cb.popupAboutToBeShown.connect(self.add_subject_to_combobox)

        self.subject = []

        cb.setCurrentText('Select .....')
        cb.currentIndexChanged.connect(self.selectionchange)

        layout.addWidget(cb)
        self.setLayout(layout)

    def show_pop_up(self):
        self.refresh_combobox.emit()

    def add_subject_to_combobox(self):
        # subject is list of tuple
        # i.e. [('Chemistry',)]
        sql_conn = SqliteConnection()
        subject = sql_conn.get_all_subjects()

        cb.clear()
        for subj in subject:
            cb.addItem(subj[0])

    def trigger_add_new_subject(self):
        if cb.currentText() == 'Add New ...':
            print("hello")
            # TODO Open new dialog window

    def selectionchange(self, i):
        print("Items in the list are :")

        for count in range(cb.count()):
            print(cb.itemText(count))
        print("Current index", i, "selection changed ", cb.currentText())
