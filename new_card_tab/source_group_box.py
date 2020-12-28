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

    def submit_button_clicked(self):
        # question and answer info
        # validation: not empty
        quest_text_box = q_box.question_textbox
        answer_text_box = a_box.answer_textbox

        # combobox for subject
        # current selectio
        # currentText()
        subject_combo = s_combo

        # book tab
        # title, author (QLineEdit), year, note (QPlainTextEdit)
        # toPlainText()
        # text()???
        book_tab = url_book.book_tab
        #url tab
        # url (QPlainTextEdit)
        url_tab = url_book.url_tab

        # save book or url or both first
        # get id for book or url or both
        # get id for subject
        # prepare insert statement
