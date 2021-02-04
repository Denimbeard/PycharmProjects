import turtle
import math
import random as rd

class graph(object):
    print('Welcome to the Monte Carlo Simulator')
    sml = int(input('Enter Min Number: '))
    lrg = int(input('Enter Max Number: '))
    res = int(input('Enter Density of points: '))
    pad= lrg * 0.5

    # Rotation
    d = 90

    def __init__(self):
        self.name = name
        self.sml = sml
        self.max = lrg
        self.res = res

    def draw(self):
        turtle.setup(width = self.lrg + self.pad, height = self.lrg + self.pad)
        turtle.mode('standard')
        turtle.penup()
        turtle.goto(((-self.lrg + 1) + self.pad),((self.lrg + 1) - self.pad))
        turtle.pendown()
        turtle.write('Monte Carlo Simulation | Dots = ' + str(self.res),
            align='left', font=('Arial', 12, 'normal'))  
        turtle.penup()
        turtle.goto((-self.lrg + self.pad),(self.lrg - self.pad))
        turtle.pendown()

        # Length of Square's Sides
        s = 4 * self.lrg
        while s > 0:
            turtle.fd(self.lrg)
            turtle.rt(self.d)
            # Takes s and removes one side at a time
            s -= self.lrg

        turtle.circle(-self.lrg,self.d)
        turtle.penup()

    def dotPlot(self):
        turtle.hideturtle()
        turtle.speed('fastest')
        res = self.res
        turtle.goto((-self.lrg + self.pad),(self.lrg - self.pad))

        # Area of the Circle
        aoc = (math.pi * (self.lrg**2))/4

        # Area of the Square
        aos = (2*self.lrg)**2

        #Ratio of dots in circle / dots in square
        C = aos - (aos-aoc)

        while res > 0:
            a = rd.randrange((-self.lrg+self.pad),(self.lrg - self.pad), 1)
            b = rd.randrange((-self.lrg+self.pad),(self.lrg - self.pad), 1)
            d = 1
            turtle.penup()
            turtle.goto(a,b)
            turtle.pendown()
            turtle.dot()
            res -= 1
        turtle.penup()
        turtle.goto(((-self.lrg + 1) + (self.pad),
            -((self.lrg + 1) - self.pad) - 13))
        turtle.pendown()
        turtle.write(str(round(math.pi, 3)) +
            ' vs Ratio of dots in Circle/Square ' + str(round(C/self.res,3)),
                     align='left', font=('Arial', 12, 'normal'))

graph.draw(graph)
graph.dotPlot(graph)
