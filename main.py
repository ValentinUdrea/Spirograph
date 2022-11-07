import turtle as t
import random
tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")
for i in range(150):
    tim.color(random_color())
    tim.circle(100)
    tim.left(3)