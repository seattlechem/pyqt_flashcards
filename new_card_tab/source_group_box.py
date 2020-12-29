import new_card_tab.qa_group.question_group_box as q_box
import new_card_tab.qa_group.answer_group_box as a_box
import new_card_tab.source_group.subject_box.subject_combobox as s_combo
import new_card_tab.source_group.url_book_tab_group_box as url_book
from PyQt5.QtWidgets import QDialogButtonBox, QGridLayout, QGroupBox
from db.db_script import SqliteConnection
from .source_group.subject_group_box import SubjectGroupBox
from .source_group.url_book_tab_group_box import URLBookTab


class SourceGroupBox(QGroupBox):
    def __init__(self, title: str):
        super().__init__()
        self.setTitle(title)
        self.setupUi()
        self.buttonBox.clicked.connect(self.submit_button_clicked)

    def setupUi(self):
        #self.subject_combo = SubjectComboBox()

        # TODO add subject button (push button)
        #self.add_new_card_button = QPushButton("Add New Subject")
        subject_group_box = SubjectGroupBox()
        url_book_group_box = URLBookTab()

        # self.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.buttonBox = QDialogButtonBox()
        # self.buttonBox.addButton("Help", QtWidgets.QDialogButtonBox.HelpRole)
        self.buttonBox.addButton(
            "Submit", QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton(
            "Cancel", QDialogButtonBox.RejectRole)

        gbox = QGridLayout()
        gbox.addWidget(subject_group_box)
        gbox.addWidget(url_book_group_box)
        gbox.addWidget(self.buttonBox)

        self.setLayout(gbox)

    def new_card_input_validation(self, question: str, answer: str, subject_id: int,
                                  book_title: str, book_author: str, book_year: str):
        # check if all fields are provided
        if question != '' and answer != '':
            if subject_id != -1 and book_title != '':
                if book_author != '' and book_year != '':
                    return True
        return False

    def submit_button_clicked(self):
        question = q_box.question_textbox.toPlainText()
        answer = a_box.answer_textbox.toPlainText()
        subject_id = s_combo.cb.currentIndex()
        book_title = url_book.book_tab.title_input.text()
        book_author = url_book.book_tab.author_input.text()
        book_year = url_book.book_tab.year_input.text()
        book_note = url_book.book_tab.note_input.toPlainText()
        book_id = None
        url_id = None

        # call validation method
        if self.new_card_input_validation(question, answer, subject_id, book_title, book_author,
                                          book_year):
            # search if book is already saved
            sql_conn = SqliteConnection()
            book_id = sql_conn.check_book_title(book_title)
            if book_id is None:
                # save to source_book table
                data = tuple([book_title, int(book_year), book_author])
                book_id = sql_conn.add_book_to_db(data)

            # at this point book exists in source_book table
            # save information to source table
            source_id = sql_conn.save_to_source_tb(book_id, url_id)

            # save into date table
            # created_date and modified_date are required info
            # get date_id
            # save question and aswer information to question_answer table

            # save into question_answer

            # save book or url or both first
            # save book, url, subject id to temp tablet
            # get id for book or url or both
            # get id for subject
            # prepare insert statement
