import turtle as turtle
import math
import ru_local as ru


def get_num_hexagons():
    while True:
        try:
            num_hex = int(input("Введите число от 4 до 20: "))
            if num_hex < 4 or num_hex > 20:
                print("Введите другое число")
            else:
                break
        except ValueError:
            print("Попробуйте снова")
    return num_hex


def get_color_choice():
    choices = {"1": "Red", "2": "Orange", "3": "Yellow", "4": "Green", "5": "Purple", "6": "Blue", "7": "Black",
               "8": "Grey", "9": "Brown", "10": "Pink"}

    print("Выберите цвет заливки шестиугольника: ")
    print("1 - Красный")
    print("2 - Оранжевый")
    print("3 - Желтый")
    print("4 - Зеленый")
    print("5 - Фиолетовый")
    print("6 - Голубой")
    print("7 - Черный")
    print("8 - Серый")
    print("9 - Коричневый")
    print("10 - Розовый")

    while True:
        choice = input("Введите цвет (число от 1 до 10): ")
        if choice in choices:
            return choices[choice]
        else:
            print("Попробуйте еще раз")


def draw_hexagon(x, y, side_len, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.pd()
    turtle.speed(0)
    turtle.color('Black', color)
    turtle.rt(30)
    for i in range(6):
        turtle.fd(side_len)
        if i == 5:
            turtle.rt(30)
        else:
            turtle.rt(60)
    turtle.end_fill()


if __name__ == '__main__':
    n = get_num_hexagons()
    clr_1 = get_color_choice()
    clr_2 = get_color_choice()

    x_cr, y_cr = -250, 250
    r = 500 / (n + 0.5) / 2
    side = r * 2 / (3 ** 0.5)
    cnt_column = 500 / (1.5 * side)
    cnt_column = int(cnt_column)

    for m in range(cnt_column):
        if m % 4 < 2:
            clr = clr_1
        else:
            clr = clr_2

        for k in range(n):
            if k == 0 and m % 2 == 0:
                x_cr += 2 *r
            draw_hexagon(x_cr, y_cr, side, clr)
            if clr == clr_1:
                clr = clr_2
            else:
                clr = clr_1

            x_cr += r * 2
        x_cr = -250 + r
        y_cr -= 1.5 * side
