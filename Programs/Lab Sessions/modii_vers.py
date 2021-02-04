import turtle
import random as rd
from operator import *
from math import *
# User Inputs
min = int(input('Enter Min Number: '))
max = int(input('Enter Max Number: '))
res = int(input('Enter Density of points: '))
start = input('Would you like to draw the square? y/n : ')
startDot = input('Would you like to plot size? y/n : ')

# Degrees of Rotation
d = 90

# Padding around shape
pad= max * 0.5

# Dot size
dot= max * 0.1

joey = turtle.Turtle()

# Turtle Setup, makes screen size based on inputs
turtle.setup(width = max + pad, height = max + pad)
turtle.mode('standard')
joey.penup()

# Starts Turtle in proper location, relitive to inputs
joey.goto((-max+pad),(max-pad))
joey.pendown()
runshape = False
joey.speed('fastest')

# Drawing Sides of Square
def draw( x):
    # Length of Square's Sides
    s = 4 * max
    while s > 0:
        joey.fd(max)
        joey.rt(d)
        # Takes s and removes one side at a time
        s -= max
    
    # Plot curve pi/4
    # -max draws the curve downward
    joey.circle(-max,d)
    joey.penup()


# Dot poulator
def dotPlot( x, y, z):
    dots = 0
    joey.goto((-z+pad),(z-pad))
    while x > 0:
        a = rd.randrange((-z+pad),(z-pad), 1)
        b = rd.randrange((-z+pad),(z-pad), 1)
        d = 1
        joey.penup()
        joey.goto(a,b)
        joey.pendown()
        joey.dot()
        x -= 1

# Circle maths
ca = (pi * (max**2)/4)


# Square Maths
sa = max**2


if start == 'y':
    runshape = True

if runshape == True:
    draw(max)

if startDot == 'y':
    dotPlot(res, min, max)

   
# quit function
turtle.Screen().exitonclick()
