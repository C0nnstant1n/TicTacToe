import time

from PySide6 import QtWidgets, QtGui
import sys
from gui.EndGameWindow import EndGameWindow
from gui.GameDesk import GridWidget, UiDesk
from gui.messages import Header, Message, ErrorMessage
import ticTacToe
from importlib import reload
from startWindow import StartDialogWindow
import random

module_game_desk = reload(ticTacToe)


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle('Крестики - нолики')
        self.setFixedSize(820, 480)
        self.message = Message("", self)
        self.player = True
        self.player_is_user = True
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

    def showEvent(self, event):
        time.sleep(1)
        print('Show Window')
        self.setting_window.exec()
        self.player_is_user = not random.randint(0, 1)
        print('choice-', self.check_player())
        self.start_message()
        print('after start message', self.check_player())
        QtWidgets.QWidget.showEvent(self, event)

    def start_message(self):
        if self.player_is_user:
            self.set_message(f'Ход игрока')
        else:
            self.set_message(f'Ход компьютера')
        if not self.player_is_user:
            self.player = not self.player
            time.sleep(1)
            self.comp_turn()

    def reset(self):
        print('reset')
        print('sym choice - ', self.check_player())
        reload(ticTacToe)

        self.ui.reset()
        self.setting_window.exec()
        self.player_is_user = not (random.randint(0, 1))
        self.start_message()
        print('sym - ', self.check_player())
        print('player - ', self.player_is_user)
        print('end_reset')

    def set_message(self, message):
        self.message.setText(message)

    def set_error_message(self, error_message):
        self.error_message.setText(error_message)

    def check_step(self, idx):
        if self.player_is_user:
            print(f'player turn, symbol - {self.check_player()}')
        else:
            print(f'pause, comp turn, symbol - {self.check_player()}')

        self.ui.fields[idx].set_active()
        x, y, m, n = self.ui.grid.getItemPosition(idx)

        if self.player:
            self.ui.fields[idx].setPixmap((QtGui.QPixmap('img/x.png')))
            module_game_desk.game_desk[x][y] = 'x'
        else:
            self.ui.fields[idx].setPixmap((QtGui.QPixmap('img/0.png')))
            module_game_desk.game_desk[x][y] = 'o'

        if any(ticTacToe.check_turn()) and self.player_is_user:
            self.pop_up_window(f'Игрок победил')
        elif any(ticTacToe.check_turn()) and not self.player_is_user:
            self.pop_up_window(f'Компьютер победил')

        print(self.check_player())
        self.player = not self.player
        print(self.check_player())
        self.player_is_user = not self.player_is_user

        if self.player_is_user:
            self.set_message(f'Ход игрока')
        else:
            self.set_message(f'Ход Компьютера')
            self.repaint()
            time.sleep(1)
            self.comp_turn()
            self.repaint()

        print(module_game_desk.game_desk)
        if not ('-' in module_game_desk.game_desk[0] or
                '-' in module_game_desk.game_desk[1] or
                '-' in module_game_desk.game_desk[1]):
            self.pop_up_window("Ничья")

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

    def comp_turn(self):
        random_idx = random.randint(0, 8)
        if not self.ui.fields[random_idx].is_active():
            self.ui.change_field(random_idx)
        else:
            self.comp_turn()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
