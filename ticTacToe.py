from os import system, name             # import os module
game_desk = [
    ['-', '-', '-'],
    ["-", "-", "-"],
    ["-", "-", "-"]
]


def input_coor():       # Ввод координат и проверка ввода
    x_y_str = input("Введите координаты поля через пробел (Y X)")
    if x_y_str == "":   # Если строка пустая, повторяем ввод
        input_coor()
    x_y_list = x_y_str.split()
    x_y_int = []
    for i in x_y_list:
        if i.isdigit() and len(x_y_list) == 2:  # Если строка содержит только цифры и её длина == 2
            x_y_int.append(int(i))
        else:
            return input_coor()
    for i in x_y_int:                           # Проверяем список координат на вмещение в игровое поле
        if not (0 <= i <= 2):
            return input_coor()
    return x_y_int


def write_matrix(x_y, ch):      # Запись хода в матрицу
    if game_desk[x_y[0]][x_y[1]] == "x" or game_desk[x_y[0]][x_y[1]] == "o":    # Проверям на повтор хода
        print("Такой ход уже был")
        write_matrix(input_coor(), ch)
    else:
        game_desk[x_y[0]][x_y[1]] = ch
    return


def rewrite_screen():
    clear()
    print("Игра - крестики нолики")
    print_matrix(game_desk)


def print_matrix(matrix):       # Вывод матрицы
    print("     0 1 2")
    a = -1
    for i in matrix:
        a += 1
        print("  ", a, *i)


def extract_string(matrix):     # Извлекаем строку из матрицы для проверки
    for i in matrix:
        if i.count("x") == 3 or i.count("o") == 3:
            return True
    return False


def extract_column(matrix):     # Извлекаем столбец из матрицы для проверки
    for i in range(3):
        a = ""
        for j in range(3):
            a += matrix[j][i]
        if a.count("x") == 3 or "ooo" == a:
            return True
    return False


def extract_ldiag(matrix):      # Извлекаем левую диагональ из матрицы для проверки
    c, a = 0, ""
    for i in matrix:
        a += i[c]
        c += 1
    if a == "xxx" or "ooo" == a:
        return True
    return False


def extract_rdiag(matrix):      # Извлекаем правую диагональ из матрицы для проверки
    c, a = 2, ""
    for i in matrix:
        a += i[c]
        c -= 1
    if a == "xxx" or "ooo" == a:
        return True
    return False


def check_turn():               # Перерисовываем экран и обновляем результаты проверок
    result = (extract_string(game_desk), extract_rdiag(game_desk),
              extract_ldiag(game_desk), extract_column(game_desk))
    return result


def clear():                            # Очистка экрана (работает только в терминале, не в IDE)
    if name == 'nt':                    # for windows
        _ = system('cls')
    else:                               # for mac and linux(here, os.name is 'posix')
        _ = system('clear')


number_moves = 0

if __name__ == '__main__':
    while number_moves < 9:
        rewrite_screen()
        print("Ходит 1й игрок")
        number_moves += 1
        write_matrix(input_coor(), "x")
        if any(check_turn()):
            rewrite_screen()
            print("Первый игрок выиграл")
            break
        if number_moves == 9:
            rewrite_screen()
            print("Ничья")
            break
        rewrite_screen()
        print("Ходит 2й игрок")
        number_moves += 1
        write_matrix(input_coor(), "o")
        if any(check_turn()):
            rewrite_screen()
            print("Второй игрок выиграл")
            break
