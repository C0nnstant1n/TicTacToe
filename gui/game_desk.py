from PyQt6 import QtWidgets, QtGui, QtCore


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

    def change_field(self, idx):
        if not (self.fields[idx].is_active()):
            self.step_signal.emit(idx)
            self.error_signal.emit('')
        else:
            self.error_signal.emit('Такой ход уже был')
            return self.fields[idx].is_active()
