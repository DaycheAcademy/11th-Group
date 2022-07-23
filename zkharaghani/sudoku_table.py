# This is a 9*9 empty sudoku table, with properties: outer lines width: 5, 3*3 lines width: 3, 9*9 lines width:1.
# Also hide turtle and speed = highest speed.

import turtle

for _ in range(4):
    turtle.width(5)
    turtle.forward(270)
    turtle.right(90)

turtle.width(3)
turtle.forward(270)
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(270)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(270)
turtle.right(90)
turtle.forward(90)
turtle.right(90)

turtle.width(3)
turtle.forward(90)
turtle.right(90)
turtle.forward(270)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(270)
turtle.right(90)
turtle.forward(90)
for _ in range(4):
    turtle.width(1)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(270)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(270)

turtle.hideturtle()
turtle.speed(speed=10)
