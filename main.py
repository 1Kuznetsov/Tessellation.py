import turtle as turtle
import math
import ru_local as ru


def get_num_hexagons():
    while True:
        try:
            num_hex = int(input(ru.QUEST_1))
            if num_hex < 4 or num_hex > 20:
                print(ru.ANOTHER_NUMB)
            else:
                break
        except ValueError:
            print(ru.TRY_AGAIN)
    return num_hex


def get_color_choice():
    choices = {1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Yellow',
               5: 'Orange', 6: 'Purple', 7: 'Pink'}

    print(ru.QUEST_2)

    print(ru.COLOR_1)
    print(ru.COLOR_2)
    print(ru.COLOR_3)
    print(ru.COLOR_4)
    print(ru.COLOR_5)
    print(ru.COLOR_6)
    print(ru.COLOR_7)

    while True:
        choice = input(ru.CHOOSE_COLOR)
        if choice in choices:
            return choices[choice]
        else:
            print(ru.TRY_AGAIN)


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
