import sys
import new_card_tab.source_group.book_url_box.book_tab as book
from db.db_script import SqliteConnection
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QDialogButtonBox, \
    QGridLayout, QDialog


class MessageBox(QDialog):
    def __init__(self, msg: str):
        super().__init__()
        self.setupUi(msg)
        self.button_action_connection()
        self.text = ''

    def setupUi(self, msg: str):
        self.setWindowTitle('Notice')
        self.message_title = QLabel(msg)
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.addButton("OK", QDialogButtonBox.AcceptRole)
        grid_box = QGridLayout()
        grid_box.addWidget(self.message_title)
        grid_box.addWidget(self.buttonBox)
        self.setLayout(grid_box)

    def button_action_connection(self):
        self.buttonBox.accepted.connect(self.apply_button_clicked)

    def apply_button_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = QDialog()
    dialog.show()
    sys.exit(app.exec_())
