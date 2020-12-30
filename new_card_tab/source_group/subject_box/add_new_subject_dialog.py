import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QDialogButtonBox, QGridLayout, \
    QDialog
from PyQt5.QtGui import QIcon
from db.db_script import SqliteConnection

# sys.path.append('../')


class AddNewSubjectDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.button_action_connection()
        self.text = ''
        # self.pushButton.clicked.connect(self.close)

    def setupUi(self):
        self.setWindowTitle('Add New Subject')
        self.subject_name = QLabel()
        self.subject_input = QLineEdit()
        self.subject_name.setText("Subject Name")
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.addButton("Help", QDialogButtonBox.HelpRole)
        self.buttonBox.addButton("Apply", QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton("Cancel", QDialogButtonBox.RejectRole)
        grid_box = QGridLayout()
        grid_box.addWidget(self.subject_name)
        grid_box.addWidget(self.subject_input)
        grid_box.addWidget(self.buttonBox)
        self.setLayout(grid_box)

        # button
        # button action

    def button_action_connection(self):
        self.buttonBox.accepted.connect(self.apply_button_clicked)

    def apply_button_clicked(self):
        self.text = self.subject_input.text()
        sql_conn = SqliteConnection()

        #TODO
        # Find out what was the last id, so that id can be assigned
        subj_id = sql_conn.get_last_row_column_data('subject_id', \
            'subject_type')[0][0] + 1

        sql_conn.add_subject_to_db(self.text)

        self.close()

    def getLabelText(self):
        text = subject_input.text()
        return text


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = QDialog()
    dialog.show()
    sys.exit(app.exec_())
