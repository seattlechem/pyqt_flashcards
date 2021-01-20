import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QDialogButtonBox, QGridLayout, \
    QDialog, QShortcut
from PyQt5.QtGui import QIcon, QKeySequence
from db.db_script import SqliteConnection
from common.cust_qlineedit import CustQLineEdit
from common.my_dialog_box import MessageBox

# sys.path.append('../')


class AddNewSubjectDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.buttonBox.accepted.connect(self.apply_button_clicked)
        self.buttonBox.rejected.connect(self.cancel_button_clicked)
        self.text = ''
        # self.pushButton.clicked.connect(self.close)

    def setupUi(self):
        self.setWindowTitle('Add New Subject')
        self.subject_name = QLabel()
        self.subject_input = CustQLineEdit()
        self.subject_name.setText("Subject Name")
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.addButton("Submit", QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton("Cancel", QDialogButtonBox.RejectRole)
        grid_box = QGridLayout()
        grid_box.addWidget(self.subject_name)
        grid_box.addWidget(self.subject_input)
        grid_box.addWidget(self.buttonBox)
        self.setLayout(grid_box)
        self.shortcut = QShortcut(QKeySequence('Ctrl+Return'), self)
        self.shortcut.activated.connect(self.apply_button_clicked)

        # button
        # button action

    def apply_button_clicked(self):
        self.text = self.subject_input.text()

        if self.text == '':
            self.close()
            msg = MessageBox('Please enter subject')
            msg.exec_()
        else:
            sql_conn = SqliteConnection()

            sql_conn.add_subject_to_db(self.text)

            self.close()

    def cancel_button_clicked(self):
        self.close()

    def getLabelText(self):
        text = subject_input.text()
        return text


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = QDialog()
    dialog.show()
    sys.exit(app.exec_())
