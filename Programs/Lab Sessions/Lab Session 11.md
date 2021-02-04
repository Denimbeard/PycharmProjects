# Foundations of Programming – Lab Session 11

- Using the “turtle” module, create a graphic window (canvas) and use the turtle to draw a
square having 250-pixels-long sides (i.e., such that the four corners have coordinates
  (0,0), (250,0), (250,250), and (0, 250)).

- The “random” module contains two useful built-in functions:
  - random( ): returns a random floating-point value x, such that 0 ≤ x < 1
  - randrange(start, stop, step): returns a random element in range(start, stop, step)
- Use one of the above functions from the random module to write a new (user-defined) Python function that returns a random integer number between 0 and 250 (inclusive).

- Write a second function, called “placeDot”, which plots n random dots in the square
drawn for point A. Assume n is integer and given to the function as a parameter.
  - HINT(1): The x and y coordinates of each dot should be random numbers between 0 and
250 (inclusive); use the function written for point B. to generate such random coordinates.
HINT(2): Use the turtle method “goto” to position the turtle, and then use the method
“dot” to print the dot. How can you avoid the turtle leaving a trace when you move it?

- Adapt and re-use the code written for points A-C above to solve the following problem:
  - The famous mathematical constant called Pi (usually denoted as ‘π’) is most often used to
calculate the circumference or the area of a circle. For simplicity, the value that is commonly used
for π is 3.14. However, pi is what mathematicians call an irrational number, meaning that that it
has an infinite, non-repeating number of decimal digits. The value is

## 3.14159265358979323846264338327950288419716939937510582097494459230781642...

## The Monte Carlo Simulation method enables calculating an approximation of the value of π. It is based on two observations:

- The ratio between the area under the curve (a “quarter” of a circle of radius 1) and the area of
the square (having side 1) show below is exactly π/4:

- If we “throw” at random a number N of darts(ensuring they all fall on the square), the portion
of darts hitting the shaded area (by chance) will be proportional to the size of that area. In
other words, if x is the number of darts falling on the shaded area, then the value x/N is an approximation of π/4.

*HINT (1)*: use the “placeDot” function written for point C. above to plot 100 dots at random in
the 250x250 square drawn in point A. The percentage of dots which fall within the “shaded” part
of the square gives you an estimate of the value π/4…
(How can you get a better estimate?..)

*HINT (2)*: A randomly placed dot can be counted as falling within the “shaded” area if its distance
from the origin (0,0) is less than or equal to 250. The “distance” method of the turtle module
can be used to test how far a turtle is from the origin..

## *OPTIONAL*
- Parameterize the functions and code written for points A-D, so that the value 250 (the
side of the square in pixels) is no longer fixed a priori but is taken as input from the user
at the start of the program. Note: the value the user inputs should be *validated* (refer
to Lecture 13, “Input validation”), so that the square size won’t exceed the current x-y
dimensions of the canvas.
