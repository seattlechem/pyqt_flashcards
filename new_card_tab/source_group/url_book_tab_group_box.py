import sys
from PyQt5.QtWidgets import QDialog, QTabWidget, QGridLayout, QGroupBox, QDialog
from .book_url_box.book_tab import BookTab
from .book_url_box.url_tab import URLTab


book_tab = None
url_tab = None
book_url_widget = None

class URLBookTab(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Book & URL')
        global book_url_widget
        book_url_widget = QTabWidget()

        #TODO Book Tab
        global book_tab
        book_tab = BookTab()
        book_url_widget.addTab(book_tab, "Book")

        #TODO URL Tab
        global url_tab
        url_tab = URLTab()
        book_url_widget.addTab(url_tab, "URL")

        gbox = QGridLayout()
        gbox.addWidget(book_url_widget)
        self.setLayout(gbox)
        # self.setFixedSize(320, 480)
