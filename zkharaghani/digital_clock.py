import turtle
from _datetime import datetime

screen = turtle.getscreen()
clock = turtle.Turtle()
clock.color('green', 'red')
now = datetime.now()
time = now.strftime('%H: %M: %S')
for i in range(2):
    turtle.begin_fill()
    turtle.fillcolor('red')
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()
    turtle.speed(10)
clock.goto(30, -70)
clock.write('{}'.format(time), font=("Arial", 25,
                                     "normal"))
turtle.hideturtle()
turtle.done()
