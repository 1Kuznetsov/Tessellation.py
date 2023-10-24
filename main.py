import turtle as turtle
import math
import ru_local as ru

n = int(input())


def draw_hexagon(x, y, side_len, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.pd()
    turtle.speed(0)
    turtle.pensize(1)
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
    x_cr, y_cr = -250, 250
    r = 500 / (n + 0.5) / 2
    side = r * 2 / (3 ** 0.5)
    cnt_column = 500 / (1.5 * side)
    cnt_column = int(cnt_column)

    for m in range(cnt_column):
        if m % 4 < 2:
            clr = 'Lime'
        else:
            clr = 'Yellow'

        for k in range(n):
            if k == 0 and m % 2 == 0:
                x_cr += side
            draw_hexagon(x_cr, y_cr, side, clr)
            if clr == 'Lime':
                clr = 'Yellow'
            else:
                clr = 'Lime'

            x_cr += r * 2
        x_cr = -250
        y_cr -= 1.5 * side
