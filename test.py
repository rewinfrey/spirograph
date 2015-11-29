import math
import turtle

# Draw the circle using Turtle
def drawCircleTurtle(x, y, r):
    # move to start of circle
    turtle.up()
    turtle.setpos(x + r, y)
    turtle.down()

    # draw the circle
    for i in range(0, 365, 10):
        a = math.radians(i)
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))

drawCircleTurtle(100, 100, 50)
turtle.mainloop()
