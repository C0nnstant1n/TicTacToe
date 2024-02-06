from PyQt6 import QtWidgets, QtCore

from gui.loadStyles import parse_css_styles


class EndGameWindow(QtWidgets.QDialog):

    def __init__(self, message: str, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle("Конец игры")
        self.resize(300, 150)

        self.message = QtWidgets.QLabel(message)
        self.message.setStyleSheet(parse_css_styles('h1', 'styles/styles.css'))
        self.message.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hbox = QtWidgets.QHBoxLayout()

        self.new_game_btn = QtWidgets.QPushButton("Новая игра")
        self.new_game_btn.clicked.connect(self.accept)
        self.exit_btn = QtWidgets.QPushButton("Выход")
        self.exit_btn.clicked.connect(self.reject)

        self.hbox.addWidget(self.new_game_btn)
        self.hbox.addWidget(self.exit_btn)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.message)
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)
