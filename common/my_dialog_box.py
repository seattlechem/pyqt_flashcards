import sys
from db.db_script import SqliteConnection
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QDialogButtonBox, \
    QGridLayout, QDialog, QMessageBox


class MessageBox(QMessageBox):
    def __init__(self, msg: str):
        super(MessageBox, self).__init__()
        self.setupUi(msg)
        self.text = ''

    def setupUi(self, msg: str):
        self.setWindowTitle('Notice')
        self.setText(msg)
        self.setStandardButtons(QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = QDialog()
    dialog.show()
    sys.exit(app.exec_())
