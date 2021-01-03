import sys
import flash_cards_resource
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, \
    QPlainTextEdit, QComboBox, QLabel, QPushButton, QWidget, QFormLayout

from PyQt5.QtGui import QIcon, QFont
from db.db_script import SqliteConnection
from common.my_qlabel import MyQLabel
from common.my_combo_box import ComboBox


class TestTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        # self.test_subject_cb.popupAboutToBeShown()
        self.test_subject_cb.popupAboutToBeShown.connect(\
            self.test_subject_cb.add_subject_to_combobox)

        self.test_logic_cb.popupAboutToBeShown.connect( \
            self.test_logic_cb.add_logic_to_combobox)
        # self.show()

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
        self.test_subject_cb.add_subject_to_combobox()
        self.test_logic_cb.add_logic_to_combobox()

    def sub_hbox_setup(self, hbox: QHBoxLayout):
        self.qabox = QPlainTextEdit()
        self.qabox.setStyleSheet("background-color: rgb(128, 128, 128);")

        qv_buttons = QVBoxLayout()
        self.pass_btn = QPushButton()
        self.pass_btn.setStyleSheet("background-image: \
            url(images/pass.png);height:50px;width:50px;")
        self.fail_btn = QPushButton()
        self.fail_btn.setStyleSheet("background-image: \
            url(images/fail.png);height:50px;width:50px;")
        self.flip_btn = QPushButton()
        self.flip_btn.setStyleSheet("background-image: \
            url(images/flip.png);height:50px;width:50px;")


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
        self.last_seen_label = MyQLabel()
        self.last_seen_label.setText('Last Seen')
        self.last_seen_data = MyQLabel()

        self.pass_rate_label = MyQLabel()
        self.pass_rate_label.setText('Pass Rate')
        self.pass_rate_data = MyQLabel()

        self.url = MyQLabel()

        hbox.addWidget(self.last_seen_label)
        hbox.addWidget(self.last_seen_data)
        hbox.addWidget(self.pass_rate_label)
        hbox.addWidget(self.pass_rate_data)
        hbox.addWidget(self.url)
        # QPlainTextEdit, vbox (pass, fail, flip) --> another hbox
        # bottom menu: comboBox (subject), comboBox (logic), button (start)

    def bottom_menu_hbox_setup(self, hbox: QHBoxLayout):
        # comboBox
        self.test_subject_cb = ComboBox()
        self.test_logic_cb = ComboBox()
        self.start_btn = QPushButton()
        self.start_btn.setText('Start')

        hbox.addWidget(self.test_subject_cb)
        hbox.addWidget(self.test_logic_cb)
        hbox.addWidget(self.start_btn)
