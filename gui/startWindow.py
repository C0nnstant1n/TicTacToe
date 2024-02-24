import random

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt, Signal)
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QDialog, QHBoxLayout, QLabel,QVBoxLayout)
import sys


class LabelBtn(QLabel):
    click_signal = Signal(bool)

    def __init__(self, parent=None):
        QLabel.__init__(self, parent)

    def mousePressEvent(self, evt):
        """Создаем сигнал клика по полю"""
        self.click_signal.emit(True)
        QLabel.mousePressEvent(self, evt)


class Ui_ChoiceDialog(object):
    def setupUi(self, ChoiceDialog):
        if not ChoiceDialog.objectName():
            ChoiceDialog.setObjectName(u"ChoiceDialog")
        ChoiceDialog.setWindowModality(Qt.ApplicationModal)
        ChoiceDialog.setFixedSize(260, 150)
        ChoiceDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(ChoiceDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(ChoiceDialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: Blue")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 20)
        self.x_btn = LabelBtn(ChoiceDialog)
        self.x_btn.setObjectName(u"x_btn")
        self.x_btn.setMaximumSize(QSize(45, 45))
        self.x_btn.setPixmap((QPixmap('img/x1.png')))

        self.horizontalLayout.addWidget(self.x_btn)

        self.o_btn = LabelBtn(ChoiceDialog)
        self.o_btn.setObjectName(u"o_btn")
        self.o_btn.setMaximumSize(QSize(45, 45))
        self.o_btn.setPixmap((QPixmap('img/01.png')))

        self.horizontalLayout.addWidget(self.o_btn)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ChoiceDialog)

        QMetaObject.connectSlotsByName(ChoiceDialog)

    # setupUi

    def retranslateUi(self, ChoiceDialog):
        ChoiceDialog.setWindowTitle(QCoreApplication.translate("ChoiceDialog", u"\u041f\u0443\u0441\u043a", None))
        self.label.setText(
            QCoreApplication.translate("ChoiceDialog", u"\u0427\u0435\u043c \u0438\u0433\u0440\u0430\u0435\u043c ?",
                                       None))
        self.x_btn.setText("")
        self.o_btn.setText("")
    # retranslateUi


class StartDialogWindow(QDialog, Ui_ChoiceDialog):
    def __init__(self, main_window, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.main_window = main_window
        self.x_btn.click_signal.connect(self.x_player)
        self.o_btn.click_signal.connect(self.o_player)

    def x_player(self):
        self.start(True)

    def o_player(self):
        self.start(False)

    def start(self, player: bool):
        print(player)
        self.main_window.player = player
        if self.main_window.player_is_user:
            self.main_window.player = player
            self.main_window.set_message(f'Ход игрока')
        else:
            if player:
                self.main_window.player = player
            else:
                self.main_window.player = not player
            self.main_window.set_message(f'Ход компьютера')
        self.close()

    @staticmethod
    def quit():
        sys.exit()
