from PySide6 import QtWidgets, QtCore
from gui.loadStyles import parse_css_styles


class Header(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, parent)
        self.setText(text)
        self.setStyleSheet(parse_css_styles('h1', 'styles/styles.css'))
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setGeometry(0, 40, 820, 50)


class Message(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, parent)
        self.setText(text)
        self.setStyleSheet(parse_css_styles('.message', 'styles/styles.css'))
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.setGeometry(390, 193, 300, 50)


class ErrorMessage(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, parent)
        self.setText(text)
        self.setStyleSheet(parse_css_styles('.error_message', 'styles/styles.css'))
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.setGeometry(390, 290, 300, 50)


class MessageBox(QtWidgets.QVBoxLayout):
    def __init__(self, parent=None):
        QtWidgets.QVBoxLayout.__init__(self, parent)
        self.message = Message("")
        self.error_message = ErrorMessage("")
        self.addWidget(self.message)
        self.addWidget(self.error_message)

    def set_message(self, message):
        self.message.setText(message)

    def set_error_message(self, error_message):
        self.error_message.setText(error_message)
