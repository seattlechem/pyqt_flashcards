import sys
from PyQt5.QtWidgets import QDialog, QTabWidget, QGridLayout, QGroupBox, QDialog
from .book_url_box.book_tab import BookTab
from .book_url_box.url_tab import URLTab


class URLBookTab(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Book & URL')

        tab_widget = QTabWidget()

        #TODO Book Tab
        tab_widget.addTab(BookTab(), "Book")

        #TODO URL Tab
        tab_widget.addTab(URLTab(), "URL")

        gbox = QGridLayout()
        gbox.addWidget(tab_widget)
        self.setLayout(gbox)
        # self.setFixedSize(320, 480)
