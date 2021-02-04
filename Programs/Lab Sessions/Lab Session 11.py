"""
Using the “turtle” module, create a graphic window (canvas) and use the turtle to draw a
square having 250-pixels-long sides (i.e., such that the four corners have coordinates
  (0,0), (250,0), (250,250), and (0, 250)).
 """

from turtle import *
from random import *
from operator import *
from math import *
'''
s = turtle.getscreen()
t = turtle.Turtle()

def tsquare(x):
    x = x
    s = 4*x

    while s > 0:
        t.fd(x)
        t.rt(90)
        s -= x
'''

"""
The “random” module contains two useful built-in functions:
random( ): returns a random floating-point value x, such that 0 ≤ x < 1
randrange(start, stop, step): returns a random element in range(start,
stop, step)

Use one of the above functions from the random module to write a new
(user-defined) Python function that returns a random integer number
between 0 and 250 (inclusive).
"""

'''
min = int(input('Enter Starting Number: '))
max = int(input('Enter Max Number: '))

def randgen(x, y):
    return random.randrange( x, y, 1)

print(randgen(min,max))

'''

"""
Write a second function, called “placeDot”, which plots n random dots in the square
drawn for point A.
Assume n is integer and given to the function as a parameter.

HINT(1): The x and y coordinates of each dot should be random numbers between 0 and
250 (inclusive); use the function written for point B. to generate such random coordinates.

HINT(2): Use the turtle method “goto” to position the turtle, and then use the method
“dot” to print the dot. How can you avoid the turtle leaving a trace when you move it?
"""

FONT = ("Arial", 15, "bold")
LABEL_OFFSET = 1.33


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

# Turtle Setup, makes screen size based on inputs
setup(width = max + pad, height = max + pad)
mode('standard')
penup()

# Starts Turtle in proper location, relitive to inputs
goto((-max+pad),(max-pad))
pendown()
runshape = False

# Drawing Sides of Square
def draw( x):
    # Length of Square's Sides
    s = 4 * max
    while s > 0:
        fd(max)
        rt(d)
        # Takes s and removes one side at a time
        s -= max
    
    # Plot curve pi/4
    # -max draws the curve downward
    circle(-max,d)
    penup()


# Dot poulator
def dotPlot( x, y, z):
    dots = 0
    goto((-z+pad),(z-pad))
    while x > 0:
        a = randrange((-z+pad),(z-pad), 1)
        b = randrange((-z+pad),(z-pad), 1)
        d = 1
        penup()
        goto(a,b)
        pendown()
        monteCarlo.dot()
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
    runDot = True

if runDot == True:
    dotPlot(res, min, max)

   
# quit function
exitonclick()

