import turtle


def stairs(size, num):
    for i in range(0, num):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)
    t.forward(size)


def square(size):
    for i in range(0,4):
        t.forward(size)
        t.left(90)


def squares(size_start, num):
    for i in range(0, num):
        size = size_start * (i+1)
        square(size)
        t.left(3.6)


t = turtle.Turtle()


# stairs(60,4)
# square(100)
squares(10, 100)

turtle.done()