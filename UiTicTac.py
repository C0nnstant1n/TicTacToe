from PyQt6 import QtWidgets, QtGui, QtCore
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


class GridWidget(QtWidgets.QLabel):
    def __init__(self, parent=None):
        QtWidgets.QLabel.__init__(self, parent)
        self.setGeometry(125, 170, 180, 180)

    def paintEvent(self, a0):
        painter = QtGui.QPainter()
        painter.begin(self)

        color = QtGui.QColor('#00f')
        pen = QtGui.QPen(color, 3, style=QtCore.Qt.PenStyle.SolidLine)
        painter.setPen(pen)
        painter.drawLine(65, 0, 65, 180)
        painter.drawLine(114, 0, 114, 180)
        painter.drawLine(0, 63, 180, 63)
        painter.drawLine(0, 112, 180, 112)

        painter.end()


class UiDesk(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setGeometry(142, 184, 147, 146)


class Field(QtWidgets.QLabel):
    def __init__(self, parent=None):
        QtWidgets.QLabel.__init__(self, parent)
        self.my_signal = QtCore.pyqtSignal(str)

    def onMySignal(self):
        print('my signal')


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()

    label = QtWidgets.QLabel('Крестики - нолики', window)
    label.setStyleSheet('color: #29f; font-family: Comic Sans MS; font-style: italic;'
                        ' font-weight: bold; font-size: 26px')
    label.setGeometry(260, 50, 300, 30)

    grid = GridWidget(window)
    desk = UiDesk(window)
    desk_grid = QtWidgets.QGridLayout()
    desk_grid.setContentsMargins(0, 0, 0, 0)
    desk_grid.setSpacing(3)

    x = 0
    for i in range(0, 3):
        for j in range(0, 3):
            x += 1
            field = Field()
            field.setObjectName(str(x))
            field.setPixmap(QtGui.QPixmap('img/field.png'))
            # field.setStyleSheet('background-color: gray')

            desk_grid.addWidget(field, i, j)
    desk.setLayout(desk_grid)

    window.show()
    sys.exit(app.exec())
