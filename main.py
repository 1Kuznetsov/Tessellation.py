import turtle as t
import math
import ru_local as ru

n = int(input())
side = 0

for j in range(500, 100**100):
    print(j % int(n+0.5))
    if j % (n + 0.5) == 0:
        side = j / (n + 0.5)
        break


def draw_hexagon(x, y, side_len, color):
    t.up()
    t.goto(x, y)
    t.begin_fill()
    t.pd()
    t.color('black', color)
    t.rt(30)
    for i in range(6):
        t.fd(side_len)
        if i == 5:
            t.rt(30)
        else:
            t.rt(60)
    t.end_fill()
    t.exitonclick()


draw_hexagon(0, 0, side, 'green')

side = int(side)
print(n, side, j)
