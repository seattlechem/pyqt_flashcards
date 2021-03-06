import datetime
import new_card_tab.qa_group.question_group_box as q_box
import new_card_tab.qa_group.answer_group_box as a_box
import new_card_tab.source_group.subject_box.subject_combobox as s_combo
import new_card_tab.source_group.url_book_tab_group_box as url_book
from PyQt5.QtWidgets import QDialogButtonBox, QGridLayout, QGroupBox, \
    QPushButton
from db.db_script import SqliteConnection
from .source_group.subject_group_box import SubjectGroupBox
from .source_group.url_book_tab_group_box import URLBookTab
from .search_book_dialog import SearchBookDialog
from common.my_dialog_box import MessageBox


class SourceGroupBox(QGroupBox):
    def __init__(self, title: str):
        super().__init__()
        self.setTitle(title)
        self.setupUi()
        self.buttonBox.accepted.connect(self.submit_button_clicked)
        self.search_book_btn.clicked.connect(self.search_book_btn_clicked)
        self.update_note_btn.clicked.connect(self.update_book_note)
        self.buttonBox.rejected.connect(self.clear_all_input_fields)

    def setupUi(self):
        #self.subject_combo = SubjectComboBox()

        # TODO add subject button (push button)
        #self.add_new_card_button = QPushButton("Add New Subject")
        subject_group_box = SubjectGroupBox()
        url_book_group_box = URLBookTab()

        # self.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.search_book_btn = QPushButton("Search Book")
        self.buttonBox = QDialogButtonBox()
        self.update_note_btn = QPushButton("Update Note")
        # self.buttonBox.addButton("Help", QtWidgets.QDialogButtonBox.HelpRole)
        self.buttonBox.addButton("Submit", QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton(self.search_book_btn,
                                 QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.update_note_btn,
                                 QDialogButtonBox.ActionRole)
        self.buttonBox.addButton("Cancel", QDialogButtonBox.RejectRole)

        gbox = QGridLayout()
        gbox.addWidget(subject_group_box)
        gbox.addWidget(url_book_group_box)
        gbox.addWidget(self.buttonBox)

        self.setLayout(gbox)

    def update_book_note(self):
        # update_book_note method can only be called if search_book btn
        # has called prior
        book_title = url_book.book_tab.title_input.text()
        book_note = url_book.book_tab.note_input.toPlainText()

        if not (url_book.book_tab.title_input.isEnabled()):
            sql_conn = SqliteConnection()
            book_id = sql_conn.search_book_id_by_title(book_title)
            success = sql_conn.update_book_note_to_db(book_id, book_note)

            if success is None:
                updated_dialog = MessageBox('Success: Updated')
                updated_dialog.exec_()
        else:
            dialog_box = MessageBox('Please Search Book first !!!')
            dialog_box.exec_()

    def clear_all_input_fields(self):
        q_box.question_textbox.setPlainText('')
        a_box.answer_textbox.setPlainText('')
        s_combo.cb.setCurrentIndex(0)
        url_book.book_tab.title_input.setText('')
        url_book.book_tab.author_input.setText('')
        url_book.book_tab.year_input.setText('')
        url_book.book_tab.note_input.setPlainText('')
        url_book.url_tab.url_input.setPlainText('')
        url_book.url_tab.url_note_input.setPlainText('')

    def new_card_input_validation(self, question: str, answer: str,
                                  subject_id: int, book_title: str,
                                  book_author: str, book_year: str):
        # check if all fields are provided
        if question != '' and answer != '':
            if subject_id != -1 and book_title != '':
                if book_author != '' and book_year != '':
                    return True
        return False

    def search_book_btn_clicked(self):
        add_dialog = SearchBookDialog()
        add_dialog.exec_()

    def submit_button_clicked(self):
        question = q_box.question_textbox.toPlainText()
        answer = a_box.answer_textbox.toPlainText().replace("'", "''").\
            replace('"', '""')
        subject_id = s_combo.cb.currentIndex()
        book_title = url_book.book_tab.title_input.text()
        book_author = url_book.book_tab.author_input.text()
        book_year = url_book.book_tab.year_input.text()
        book_note = url_book.book_tab.note_input.toPlainText()
        url = url_book.url_tab.url_input.toPlainText()
        url_note = url_book.url_tab.url_note_input.toPlainText()

        sql_conn = SqliteConnection()
        now = datetime.datetime.now()
        date_id = sql_conn.post_datetime(now, now)

        if url_book.book_url_widget.currentIndex() == 0:
            self.save_book_source_qa(question, answer, subject_id, book_title,
                                     book_author, book_year, book_note,
                                     date_id, sql_conn)
        else:
            self.save_url_source_qa(question, answer, url, url_note, date_id,
                                    subject_id, sql_conn)

    def save_url_source_qa(self, question, answer, url, url_note, date_id,
                           subject_id, sql_conn):
        if url != '':
            url_id = sql_conn.search_url_id(url)

            if url_id is None:
                url_id = sql_conn.save_url(url, url_note)
                source_id = sql_conn.save_source_to_tb(None, url_id)
            else:
                source_id = sql_conn.get_source_id(url_id)
            sql_conn.post_question_answer_tb(question, answer, subject_id,
                                             date_id, source_id, 0, 0)
        # success
        # message dialog box
            success_msg = MessageBox('Success: Saved')
            success_msg.exec_()
            self.clear_all_input_fields()

        else:
            msg = MessageBox('URL information is missing')
            msg.exec_()

    def save_book_source_qa(self, question, answer, subject_id, book_title,
                            book_author, book_year, book_note, date_id,
                            sql_conn):

        if self.new_card_input_validation(question, answer, subject_id,
                                          book_title, book_author, book_year):
            # search if book is already saved
            book_id = sql_conn.search_book_id_by_title(book_title)
            if book_id is None:
                # save to source_book table
                book_id = sql_conn.add_book_to_db(book_title, int(book_year),
                                                  book_author, book_note)
                source_id = sql_conn.save_source_to_tb(book_id, None)

            sql_conn.post_question_answer_tb(question, answer, subject_id,
                                             date_id, source_id)
            success_msg = MessageBox('Success: Saved')
            success_msg.exec_()
            self.clear_all_input_fields()
        else:
            msg = MessageBox('Please provide all required information!')
            msg.exec_()
