"""Создайте программу для игры в ""Крестики-нолики"".

1. С 14 по 18 строку вывод индексов списка. В столбик выводит хорошо.
   Как только пытаюсь вывести в строку - получается бериберда.
2. Бот часто выдает одинаковые цифры.
3. Если проверку обернуть в функцию, то i и j становятся недоступными.
4. Хотел, что бы после проверки бота на выигрыш, код переходил на 139 строку.
   Но, почему-то не получилось. Пришлось ввести 88-90 строки.
"""


import random

new_list = [
           [' * ', ' * ', ' * '],
           [' * ', ' * ', ' * '],
           [' * ', ' * ', ' * ']]

print(f'new_list = {new_list}')
print()

text = ("Пока никто не выиграл")
count = 0
while count < 9 and text == "Пока никто не выиграл":
    for _ in range(10):     # Бот ходит при помощи random.

        print("Ход бота")
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if new_list[row][column] == ' * ':
            print(f'{row, column}')
            new_list[row][column] = ' X '
            count += 1
            break
        else:
            print("Эта ячейка занята, у бота еще одна попытка")

    def Sells(new_list: list):  # Вывод списка в виде таблицы.
        """Вывод списка в виде таблицы."""
        print('-------------------')
        for i in range(3):
            print('|', end='')
            for j in range(3):
                print(f' {new_list[i][j]} ', end='|')
            print()
            print('-------------------')
        print(new_list)

    Sells(new_list)

    #  def Examination_1(new_list: list):
    #     """Проверка на выигрыш."""
    #     for i in range(3):
    #         for j in range(3):
    #             if new_list[i][0] == new_list[i][1] == new_list[i][2] == ' X ':
    #                 print(" Выиграл бот")
    #             elif new_list[i][0] == new_list[i][1] == new_list[i][2] == ' 0 ':
    #                 print(" Вы выиграли")
    #             break

    # def Examination(new_list):
    #     """Проверка на выигрыш."""
    # for i in range(len(new_list)):
    for j in range(len(new_list)):      # "Проверка на выигрыш бота"
        if new_list[0][0] == ' X ' and new_list[0][1] == ' X ' and new_list[0][2] == ' X ':
            text = "Выиграл бот. Не огорчайтесь."
            break
        elif new_list[1][0] == ' X ' and new_list[1][1] == ' X ' and new_list[1][2] == ' X ':
            text = "Выиграл бот. Не огорчайтесь."
            break
        elif new_list[2][0] == ' X ' and new_list[2][1] == ' X ' and new_list[2][2] == ' X ':
            text = "Выиграл бот. Не огорчайтесь."
            break
        elif new_list[0][0] == ' X ' and new_list[1][0] == ' X ' and new_list[2][0] == ' X ':
            text = "Выиграл бот. Не огорчайтесь."
            break
        elif new_list[0][1] == ' X ' and new_list[1][1] == ' X ' and new_list[2][1] == ' X ':
            text = "Выиграл бот. Не огорчайтесь."
            break
        elif new_list[0][2] == ' X ' and new_list[1][2] == ' X ' and new_list[2][2] == ' X ':
            text = "Выиграл бот. Не огорчайтесь."
            break
        elif new_list[0][0] == ' X ' and new_list[1][1] == ' X ' and new_list[2][2] == ' X ':
            text = "Выиграл бот. Не огорчайтесь."
            break
        elif new_list[2][0] == ' X ' and new_list[1][1] == ' X ' and new_list[0][2] == ' X ':
            text = "Выиграл бот. Не огорчайтесь."
            break
        else:
            break
    if text == "Выиграл бот. Не огорчайтесь.":
        print(f'Игра закончена. {text}')
        break

    # Examination(new_list)
    # Examination_1(new_list)

    for _ in range(2):      # Ход игрока
        print("Ваш ход")
        row = int(input("Введите номер строки: "))
        column = int(input("Введите номер колонки: "))
        if new_list[row][column] == ' * ':
            new_list[row][column] = ' 0 '
            print(f'{row, column}')
            count += 1
            break
        else:
            print("Эта ячейка занята, попытайтесь еще раз ")

    Sells(new_list)

    # def Examination(new_list):

    # for i in range(len(new_list)):
    for j in range(len(new_list)):      # Проверка на выигрыш игрока
        if new_list[0][0] == ' 0 ' and new_list[0][1] == ' 0 ' and new_list[0][2] == ' 0 ':
            text = "Вы выиграли. Поздравляю."
            break
        elif new_list[1][0] == ' 0 ' and new_list[1][1] == ' 0 ' and new_list[1][2] == ' 0 ':
            text = "Вы выиграли. Поздравляю."
            break
        elif new_list[2][0] == ' 0 ' and new_list[2][1] == ' 0 ' and new_list[2][2] == ' 0 ':
            text = "Вы выиграли. Поздравляю."
            break
        elif new_list[0][0] == ' 0 ' and new_list[1][0] == ' 0 ' and new_list[2][0] == ' 0 ':
            text = "Вы выиграли. Поздравляю."
            break
        elif new_list[0][1] == ' 0 ' and new_list[1][1] == ' 0 ' and new_list[2][1] == ' 0 ':
            text = "Вы выиграли. Поздравляю."
            break
        elif new_list[0][2] == ' 0 ' and new_list[1][2] == ' 0 ' and new_list[2][2] == ' 0 ':
            text = "Вы выиграли. Поздравляю."
            break
        elif new_list[0][0] == ' 0 ' and new_list[1][1] == ' 0 ' and new_list[2][2] == ' 0 ':
            text = "Вы выиграли. Поздравляю."
            break
        elif new_list[2][0] == ' 0 ' and new_list[1][1] == ' 0 ' and new_list[0][2] == ' 0 ':
            text = "Вы выиграли. Поздравляю."
            break
        else:
            break
else:
    print(f'Игра закончена. {text}')
