# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
                               QSizePolicy, QVBoxLayout, QWidget)


class MyButton(QLabel):
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
        self.x_btn = MyButton(ChoiceDialog)
        self.x_btn.setObjectName(u"x_btn")
        self.x_btn.setMaximumSize(QSize(45, 45))
        self.x_btn.setPixmap((QPixmap('img/x1.png')))

        self.horizontalLayout.addWidget(self.x_btn)

        self.o_btn = MyButton(ChoiceDialog)
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


