from PyQt6 import QtWidgets, QtGui, QtCore
import sys
from loadStyles import parse_css_styles
from ticTacToe import game_desk


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


class Field(QtWidgets.QLabel):
    click_signal = QtCore.pyqtSignal(int)

    def __init__(self, idx: int, parent=None):
        QtWidgets.QLabel.__init__(self, parent)
        self.setText('')
        if 9 < idx < 0:
            idx = 0
        self.id = idx
        self.active = False

    def mousePressEvent(self, evt):
        self.click_signal.emit(self.id)
        QtWidgets.QLabel.mousePressEvent(self, evt)

    def is_active(self):
        return self.active

    def set_active(self):
        self.active = True


class UiDesk(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setGeometry(142, 184, 147, 146)
        self.grid = QtWidgets.QGridLayout()
        self.grid.setSpacing(3)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.fields = [Field(i) for i in range(0, 10)]
        x = 0
        for i in range(0, 3):
            for j in range(0, 3):
                self.grid.addWidget(self.fields[x], i, j)
                x += 1
        for field in self.fields:
            field.setPixmap(QtGui.QPixmap('img/field.png'))
            field.click_signal.connect(self.change_field)
        self.setLayout(self.grid)

    def change_field(self, id):
        if not(self.fields[id].is_active()):
            print(game_desk)
            self.fields[id].set_active()
            self.fields[id].setPixmap((QtGui.QPixmap('')))
            x, y, m, n = self.grid.getItemPosition(id)
            game_desk[x][y] = 'x'
            print(game_desk)
        else:
            return self.fields[id].is_active()


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
        self.header = QtWidgets.QLabel('Крестики - нолики', self)
        self.header.setStyleSheet(parse_css_styles('h1', 'styles/styles.css'))
        self.header.setGeometry(260, 50, 300, 30)
        self.grid_widget = GridWidget(self)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    ui = UiDesk(window)

    window.show()
    sys.exit(app.exec())
