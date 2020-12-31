import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QDialogButtonBox, QGridLayout, \
    QDialog
from PyQt5.QtGui import QIcon
from db.db_script import SqliteConnection
import new_card_tab.source_group.book_url_box.book_tab as book
# sys.path.append('../')


class SearchBookDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.button_action_connection()
        self.text = ''
        # self.pushButton.clicked.connect(self.close)

    def setupUi(self):
        self.setWindowTitle('Add New Subject')
        self.book_title = QLabel("Book Title")
        self.book_title_input = QLineEdit()
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.addButton("Search", QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton("Cancel", QDialogButtonBox.RejectRole)
        grid_box = QGridLayout()
        grid_box.addWidget(self.book_title)
        grid_box.addWidget(self.book_title_input)
        grid_box.addWidget(self.buttonBox)
        self.setLayout(grid_box)

        # button
        # button action

    def button_action_connection(self):
        self.buttonBox.accepted.connect(self.apply_button_clicked)

    def apply_button_clicked(self):
        self.book_text = self.book_title_input.text()
        sql_conn = SqliteConnection()

        # Search book by title
        # if returned id is None, open dialog displaying a message that book
        # is not found
        # book_title, year, book_author field is not editable
        book_id = sql_conn.search_book_id_by_title(self.book_title)

        if book_id > 0:
            # if returned id is > 0, pre populate book_title, year, book_author
            (_, book_title, book_year, book_author) = \
                sql_conn.search_book_by_title(self.book_title)
            self.set_book_tab_text(book_title, book_author, str(book_year), \
                book_note)
        self.close()

    def set_book_tab_text(self, book_title, book_author, book_year, book_note):

        book.book_title.setText(book_title)
        book.book_author.setText(book_author)
        book.book_year.setText(book_year)
        book.book_note.setPlainText(book_note)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = QDialog()
    dialog.show()
    sys.exit(app.exec_())
