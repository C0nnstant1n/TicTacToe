from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QPixmap
import sys


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle('Крестики - нолики')
        self.setFixedSize(820, 480)
        pal = self.palette()
        pal.setBrush(QtGui.QPalette.ColorGroup.Normal, QtGui.QPalette.ColorRole.Window,
                     QtGui.QBrush(QtGui.QPixmap('img/math_list.png')))
        pal.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window,
                     QtGui.QBrush(QtGui.QPixmap('img/math_list.png')))
        self.setPalette(pal)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()

    # label = QtWidgets.QLabel('', window)
    # label.setPixmap(QPixmap('img/math_list.png'))

    window.show()
    sys.exit(app.exec())
