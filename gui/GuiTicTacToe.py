from PySide6 import QtWidgets, QtGui
import sys
from gui.EndGameWindow import EndGameWindow
from gui.GameDesk import GridWidget, UiDesk
from gui.messages import Header, Message, ErrorMessage
import ticTacToe
from importlib import reload
from startWindow import Ui_ChoiceDialog as StartDialog

module_game_desk = reload(ticTacToe)


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle('Крестики - нолики')
        self.setFixedSize(820, 480)
        self.message = Message("", self)
        self.player = False
        self.turn = 0
        pal = self.palette()
        pal.setBrush(QtGui.QPalette.ColorGroup.Normal, QtGui.QPalette.ColorRole.Window,
                     QtGui.QBrush(QtGui.QPixmap('img/math_list.png')))
        pal.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window,
                     QtGui.QBrush(QtGui.QPixmap('img/math_list.png')))
        self.setPalette(pal)
        self.header = Header('Крестики - нолики', parent=self)
        self.error_message = ErrorMessage('', parent=self)
        self.grid_widget = GridWidget(self)
        self.ui = UiDesk(self)
        self.ui.error_signal.connect(self.set_error_message)
        self.ui.step_signal.connect(self.check_step)
        self.setting_window = StartDialogWindow(self, self)

    def showEvent(self, e):
        self.setting_window.exec()

    def reset(self):
        reload(ticTacToe)
        self.ui.reset()
        self.turn = -1
        self.showEvent('')
        self.player = not self.player

    def set_message(self, message):
        self.message.setText(message)

    def set_error_message(self, error_message):
        self.error_message.setText(error_message)

    def check_step(self, idx):
        self.ui.fields[idx].set_active()
        x, y, m, n = self.ui.grid.getItemPosition(idx)

        if self.player:
            self.ui.fields[idx].setPixmap((QtGui.QPixmap('img/x.png')))
            module_game_desk.game_desk[x][y] = 'x'
        else:
            self.ui.fields[idx].setPixmap((QtGui.QPixmap('img/0.png')))
            module_game_desk.game_desk[x][y] = 'o'
        if any(ticTacToe.check_turn()):
            self.pop_up_window(f'Игрок "{self.check_player()}" победил')

        if self.turn == 8:
            self.pop_up_window("Ничья")

        self.player = not self.player
        self.set_message(f'Ходит игрок "{self.check_player()}"')

        self.turn += 1

    def check_player(self):
        if self.player:
            return 'X'
        else:
            return 'O'

    def pop_up_window(self, message):
        win_window = EndGameWindow(message, self)
        if win_window.exec():
            self.reset()
        else:
            app.exit(0)


class StartDialogWindow(QtWidgets.QDialog, StartDialog):
    def __init__(self, main_window: MainWindow, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.main_window = main_window
        self.x_btn.click_signal.connect(self.x_player)
        self.o_btn.click_signal.connect(self.o_player)

    def x_player(self):
        self.start(0)

    def o_player(self):
        self.start(1)

    def start(self, player: int):
        if player:
            self.main_window.player = False
        else:
            self.main_window.player = True
        self.main_window.set_message(f'Ходит игрок "{self.main_window.check_player()}"')
        self.close()

    @staticmethod
    def quit():
        sys.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
