# Kuznetsov Igor - 60 %, Yadreeva Maria - 40 %.

import turtle as turtle
import ru_local as ru


def get_color_choice():
    choices = {ru.COLOR_1: 'Red', ru.COLOR_2: 'Blue', ru.COLOR_3: 'Lime', ru.COLOR_4: 'Yellow',
               ru.COLOR_5: 'Orange', ru.COLOR_6: 'Purple', ru.COLOR_7: 'Pink'}

    choice = input(ru.CHOOSE_COLOR).lower()

    while True:
        if choice in choices:
            return choices[choice]
        else:
            print('\'{}\' {}'.format(choice, ru.INCORRECT_CLR))
            choice = input(ru.TRY_AGAIN).lower()


def get_num_hexagons():
    num_hex = int(input(ru.COUNT))

    while True:
        try:
            if num_hex < 4 or num_hex > 20:
                print(ru.REQ_COUNT)
                num_hex = int(input(ru.TRY_AGAIN))
            else:
                return num_hex

        except ValueError:
            print(ru.REQ_COUNT)
            num_hex = int(input(ru.TRY_AGAIN))


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
    print(ru.COLORS_ALLOWED)
    print(ru.COLOR_1, ru.COLOR_2, ru.COLOR_3, ru.COLOR_4, ru.COLOR_5, ru.COLOR_6, ru.COLOR_7, sep='\n')

    clr_1 = get_color_choice()
    clr_2 = get_color_choice()
    n = get_num_hexagons()

    turtle.hideturtle()

    x_cr, y_cr = -250, 250
    r = 500 / (n + 0.5) / 2
    side = r * 2 / (3 ** 0.5)
    cnt_column = n

    for m in range(cnt_column):
        if m % 4 < 2:
            clr = clr_2
        else:
            clr = clr_1

        if m % 2 == 0:
            x_cr += 2 * r
        else:
            x_cr += r

        for k in range(n):
            draw_hexagon(x_cr, y_cr, side, clr)

            if clr == clr_2:
                clr = clr_1
            else:
                clr = clr_2

            x_cr += r * 2

        x_cr = -250
        y_cr -= 1.5 * side

    turtle.exitonclick()
