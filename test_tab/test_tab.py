import sys
import datetime
import flash_cards_resource
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, \
    QPlainTextEdit, QComboBox, QLabel, QPushButton, QWidget, QFormLayout, qApp

from PyQt5.QtGui import QIcon, QFont
from db.db_script import SqliteConnection
from common.my_qlabel import MyQLabel
from common.my_combo_box import ComboBox
from common.my_dialog_box import MessageBox
from common.my_qplaintextedit import MyQPlainTextEdit


class TestTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        # self.test_subject_cb.popupAboutToBeShown()
        self.test_subject_cb.popupAboutToBeShown.connect(
            self.test_subject_cb.add_subject_to_combobox)

        self.test_logic_cb.popupAboutToBeShown.connect(
            self.test_logic_cb.add_logic_to_combobox)

        self.current_card = None
        self.flip = False

        # start button
        self.start_btn.clicked.connect(self.start_test)

        # pass button
        self.pass_btn.clicked.connect(self.pass_btn_clicked)

        # fail button
        self.fail_btn.clicked.connect(self.fail_btn_clicked)

        # flip button
        self.flip_btn.clicked.connect(self.show_answer)

    def setupUi(self):
        top_hbox = QHBoxLayout()
        self.top_menu_hbox_setup(top_hbox)
        sub_hbox = QHBoxLayout()
        self.sub_hbox_setup(sub_hbox)
        btm_hbox = QHBoxLayout()
        self.bottom_menu_hbox_setup(btm_hbox)
        # self.start_btn.setDisabled(True)

        vbox = QVBoxLayout()
        vbox.setSpacing(40)
        vbox.addLayout(top_hbox)
        vbox.addLayout(sub_hbox)
        vbox.addLayout(btm_hbox)

        self.setLayout(vbox)
        self.test_subject_cb.add_subject_to_combobox()
        self.test_logic_cb.add_logic_to_combobox()

        self.disable_pass_fail_flip_btns(True);

    def sub_hbox_setup(self, hbox: QHBoxLayout):
        self.qabox = MyQPlainTextEdit()
        self.qabox.setReadOnly(True)

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

    def start_test(self):
        # get subject
        subject_id = self.test_subject_cb.currentIndex()
        logic = self.test_logic_cb.currentText()

        if subject_id != 0 and logic != 'Select .....':
            sql_stm_dic = {
                'Test all cards in the subject':
                f"SELECT * FROM question_answer WHERE subject_id='{subject_id}'"
            }

            # get cards in list
            sql_conn = SqliteConnection()
            # res is in list containing tuple (card_id, question, answer, ... etc)
            cards = sql_conn.get_sql_query(sql_stm_dic[logic])

            for card in cards:
                while not self.flip:
                    self.current_card = self.create_card_dict(card)
                    self.show_card()
                    self.display_labels(sql_conn)
                    self._pass_fail_btn_disabled(True)
                    self.flip_btn.setDisabled(False)
                    qApp.processEvents()
                while self.flip:
                    self.flip_btn.setDisabled(True)
                    self._pass_fail_btn_disabled(False)
                    qApp.processEvents()
            end_message = MessageBox('End of Test')
            end_message.exec_()
            self._clear()
            # pass or fail button
            # flip button

    def create_card_dict(self, card: tuple):
        card_dict = {}

        card_dict['card_id'] = card[0]
        card_dict['question'] = card[1]
        card_dict['answer'] = card[2]
        card_dict['subject_id'] = card[3]
        card_dict['date_id'] = card[4]
        card_dict['source_id'] = card[5]
        card_dict['total_test_times'] = card[6]
        card_dict['total_fail_times'] = card[7]

        return card_dict

    def show_answer(self):
        self.flip = True
        self.qabox.setPlainText(self.current_card['answer'])

    def _clear(self):
        self.flip = False
        self.qabox.setPlainText('')
        self.test_subject_cb.setCurrentIndex(0)
        self.test_logic_cb.setCurrentIndex(0)
        self.start_btn.setDisabled(False)

    def _pass_fail_btn_disabled(self, answer: bool):
        self.pass_btn.setDisabled(answer)
        self.fail_btn.setDisabled(answer)

    def pass_btn_clicked(self):
        print('pass')
        self.flip = False
        sql_conn = SqliteConnection()
        self.increase_total_times(self.current_card['card_id'], sql_conn)
        now = datetime.datetime.now()
        self.update_last_seen_date(self.current_card['date_id'], now, sql_conn)

    def increase_total_times(self, card_id: int, sql_conn: SqliteConnection):
        sql_stm = f"UPDATE question_answer SET total_test_times=\
            total_test_times + 1 WHERE card_id='{card_id}'"
        sql_conn.post_sql_query(sql_stm)

    def update_last_seen_date(self, date_id: int, now: datetime,
                              sql_conn: SqliteConnection):
        sql_stm = f"UPDATE date SET last_seen_date='{now}' \
            WHERE date_id='{date_id}'"
        sql_conn.post_sql_query(sql_stm)

    def fail_btn_clicked(self):
        print('fail')
        self.flip = False

    def display_labels(self, sql_conn: SqliteConnection):
        date_info = sql_conn.get_date_info(self.current_card['date_id'])
        if date_info[0][3] == 'None':
            last_seen = 'N/A'
        else:
            last_seen = datetime.datetime.strptime(date_info[0][3],
                                                   '%Y-%m-%d %H:%M:%S.%f')
        self.last_seen_data.setText(last_seen.date().strftime('%m/%d/%Y'))

    def show_card(self):
        self.qabox.setPlainText(self.current_card['question'])

    def disable_pass_fail_flip_btns(self, value: bool):
        self.pass_btn.setDisabled(value)
        self.fail_btn.setDisabled(value)
        self.flip_btn.setDisabled(value)
