from turtle import *
import random

speed(0)
setup(500,500) # window size
pensize(5)
penup()
goto(-200,-150) # B
pendown()
goto(200,-150) # C
goto(0,150) # A
goto(-200,-150)
hideturtle()

dotX = random.randint(-80, 80) # circumference of the first point
dotY = random.randint(-80, 80)

penup()
goto(dotX, dotY)
a = pos()
dot(5)

while True:
    ch = random.choice([1,2,3])
    if ch == 1: # point will move a half distance to A 
        goto(0,150)
        b = pos()
        goto((a[0]+b[0])/2, (a[1]+b[1])/2)
        dot(5, "green")
        a = pos()
    elif ch == 2: # point will move a half distance to B
        goto(-200,-150)
        b = pos()
        goto((a[0]+b[0])/2, (a[1]+b[1])/2)
        dot(5, "red")
        a = pos()
    else:
        goto(200,-150) # point will move a half distance to C
        b = pos()
        goto((a[0]+b[0])/2, (a[1]+b[1])/2)
        dot(5, "blue")
        a = pos()
