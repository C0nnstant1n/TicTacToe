from PyQt6 import QtWidgets, QtGui, QtCore
import sys
from ticTacToe import game_desk, check_turn
from gui.messages import Header, Message, ErrorMessage


class GridWidget(QtWidgets.QLabel):

    """Рисуем решетку. Этот класс используется в учебных целях. Гораздо проще вывести готовую картинку"""
    def __init__(self, parent=None):
        QtWidgets.QLabel.__init__(self, parent)
        self.setGeometry(125, 170, 180, 180)

    def paintEvent(self, a0):
        painter = QtGui.QPainter()
        painter.begin(self)

        color = QtGui.QColor(85, 27, 179)
        pen = QtGui.QPen(color, 3, style=QtCore.Qt.PenStyle.SolidLine)
        painter.setPen(pen)
        painter.drawLine(65, 0, 65, 180)
        painter.drawLine(114, 0, 114, 180)
        painter.drawLine(0, 63, 180, 63)
        painter.drawLine(0, 112, 180, 112)

        painter.end()


class Field(QtWidgets.QLabel):
    """Здесь опишем единичную ячейку игрового поля"""
    click_signal = QtCore.pyqtSignal(int)

    def __init__(self, idx: int, parent=None):
        QtWidgets.QLabel.__init__(self, parent)
        self.setText('')
        if 9 < idx < 0:
            idx = 0
        self.id = idx
        self.active = False

    def mousePressEvent(self, evt):
        """Создаем сигнал клика по полю"""
        self.click_signal.emit(self.id)
        QtWidgets.QLabel.mousePressEvent(self, evt)

    def is_active(self):
        return self.active

    def set_active(self):
        self.active = True


class UiDesk(QtWidgets.QWidget):
    """Класс игрового поля."""
    error_signal = QtCore.pyqtSignal(str)
    step_signal = QtCore.pyqtSignal(int)

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
        if not (self.fields[id].is_active()):
            self.step_signal.emit(id)
            self.error_signal.emit('')
        else:
            self.error_signal.emit('Такой ход уже был')
            print('Такой ход уже был')
            return self.fields[id].is_active()


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle('Крестики - нолики')
        self.setFixedSize(820, 480)
        self.player = False
        self.turn = 0
        pal = self.palette()
        pal.setBrush(QtGui.QPalette.ColorGroup.Normal, QtGui.QPalette.ColorRole.Window,
                     QtGui.QBrush(QtGui.QPixmap('img/math_list.png')))
        pal.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window,
                     QtGui.QBrush(QtGui.QPixmap('img/math_list.png')))
        self.setPalette(pal)
        self.header = Header('Крестики - нолики', parent=self)
        self.message = Message(f"Ходит {self.player + 1}й игрок", parent=self)
        self.error_message = ErrorMessage('', parent=self)
        self.grid_widget = GridWidget(self)
        self.ui = UiDesk(self)
        self.ui.error_signal.connect(self.set_error_message)
        self.ui.step_signal.connect(self.check_step)

    def set_message(self, message):
        self.message.setText(message)

    def set_error_message(self, error_message):
        self.error_message.setText(error_message)

    def check_step(self, id):
        self.ui.fields[id].set_active()
        x, y, m, n = self.ui.grid.getItemPosition(id)

        if self.player:
            self.ui.fields[id].setPixmap((QtGui.QPixmap('img/x1.png')))
            game_desk[x][y] = 'x'
        else:
            self.ui.fields[id].setPixmap((QtGui.QPixmap('img/01.png')))
            game_desk[x][y] = 'o'
        print(check_turn())

        if self.turn == 8:
            print(self.turn)
            self.close()

        self.player = not self.player
        self.set_message(f"Ходит {self.player + 1}й игрок")
        self.turn += 1


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
