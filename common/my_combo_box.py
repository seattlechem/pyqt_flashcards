from PyQt5 import QtCore, QtWidgets
from db.db_script import SqliteConnection

class ComboBox(QtWidgets.QComboBox):
    popupAboutToBeShown = QtCore.pyqtSignal()

    def showPopup(self):
        self.popupAboutToBeShown.emit()
        super(ComboBox, self).showPopup()

    def add_subject_to_combobox(self):
        # subject is list of tuple
        # i.e. [('Chemistry',)]
        sql_conn = SqliteConnection()
        subject = sql_conn.get_all_subjects()

        self.clear()
        for subj in subject:
            self.addItem(subj[0])

    def add_logic_to_combobox(self):
        logics = [
            'Select .....',
            'Test all cards in the subject'

        ]

        self.clear()
        for logic in logics:
            self.addItem(logic)
