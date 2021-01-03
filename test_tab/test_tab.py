import sys
import flash_cards_resource
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, \
    QPlainTextEdit, QComboBox, QLabel, QPushButton, QWidget, QFormLayout

from PyQt5.QtGui import QIcon
from db.db_script import SqliteConnection


class TestTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()

    def setupUi(self):
        top_hbox = QHBoxLayout()
        self.top_menu_hbox_setup(top_hbox)
        sub_hbox = QHBoxLayout()
        self.sub_hbox_setup(sub_hbox)
        btm_hbox = QHBoxLayout()
        self.bottom_menu_hbox_setup(btm_hbox)

        vbox = QVBoxLayout()
        vbox.setSpacing(40)
        vbox.addLayout(top_hbox)
        vbox.addLayout(sub_hbox)
        vbox.addLayout(btm_hbox)

        self.setLayout(vbox)

    def sub_hbox_setup(self, hbox: QHBoxLayout):
        self.qabox = QPlainTextEdit()
        self.qabox.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.spacer = QLabel()

        qv_buttons = QVBoxLayout()
        self.pass_btn = QPushButton()
        self.pass_btn.setStyleSheet("background-image: \
            url(images/check_mark_90.png);height:90px;width:90px;")
        self.fail_btn = QPushButton()
        self.fail_btn.setStyleSheet("background-image: \
            url(images/fail.png);height:90px;width:90px;")
        self.flip_btn = QPushButton()
        self.flip_btn.setStyleSheet("background-image: \
            url(images/flip.png);height:90px;width:90px;")


        qv_buttons.addWidget(self.pass_btn)
        qv_buttons.addStretch(1)
        qv_buttons.addWidget(self.fail_btn)
        qv_buttons.addStretch(1)
        qv_buttons.addWidget(self.flip_btn)

        hbox.setSpacing(50)
        hbox.addWidget(self.qabox)
        hbox.addLayout(qv_buttons)

    def top_menu_hbox_setup(self, hbox: QHBoxLayout):
        # top menu: QLabels (last seen, url, pass rate)
        self.last_seen_label = QLabel()
        self.last_seen_label.setText('Last Seen')
        self.last_seen_data = QLabel()

        self.pass_rate_label = QLabel()
        self.pass_rate_label.setText('Pass Rate')
        self.pass_rate_data = QLabel()

        self.url = QLabel()

        hbox.addWidget(self.last_seen_label)
        hbox.addWidget(self.last_seen_data)
        hbox.addWidget(self.pass_rate_label)
        hbox.addWidget(self.pass_rate_data)
        hbox.addWidget(self.url)
        # QPlainTextEdit, vbox (pass, fail, flip) --> another hbox
        # bottom menu: comboBox (subject), comboBox (logic), button (start)

    def bottom_menu_hbox_setup(self, hbox: QHBoxLayout):
        # comboBox
        self.test_subject_cb = QComboBox()
        self.test_logic_cb = QComboBox()
        self.start_btn = QPushButton()
        self.start_btn.setText('Start')

        hbox.addWidget(self.test_subject_cb)
        hbox.addWidget(self.test_logic_cb)
        hbox.addWidget(self.start_btn)
