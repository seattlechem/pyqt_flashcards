import sys
from PyQt5.QtWidgets import QPushButton, QApplication, QGroupBox, QGridLayout, \
    QLabel, QVBoxLayout, QDialog, QHBoxLayout
from PyQt5.QtCore import Qt
# from common.my_group_box import MyGroupBox
from .subject_box.subject_combobox import SubjectComboBox
from .subject_box.add_new_subject_dialog import AddNewSubjectDialog


class SubjectGroupBox(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.add_new_card_button.clicked.connect(self.open_dialog)

    def setupUi(self):
        # subject combo
        self.subject_combo = SubjectComboBox()
        self.add_new_card_button = QPushButton("Add New Subject")
        # self.add_new_card_button.setMaximumSize(20, 20)
        self.add_new_card_button.setMinimumWidth(100)
        self.subject_label = QLabel("Subject")

        vbox = QGridLayout()
        vbox.setColumnMinimumWidth(1, 220)
        vbox.addWidget(self.subject_label)
        vbox.addWidget(self.subject_combo)
        vbox.addWidget(self.add_new_card_button)

        # vbox.setAlignment(Qt.AlignAbsolute)
        self.setLayout(vbox)
    def open_dialog(self):
        add_dialog = AddNewSubjectDialog()
        add_dialog.exec_()
