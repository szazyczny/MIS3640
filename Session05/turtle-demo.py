#TURTLE MODULE
# import turtle

# jack = turtle.Turtle() #importing module and using class called turtle

# jack.fd(100) #call a method, this means forward 100 pixels, draw a horizontal line
# jack.lt(90) #lt means left turn 90 degrees
# jack.fd(100)
# jack.lt(90)
# jack.fd(100)
# jack.lt(90)
# jack.fd(100) #to draw a square just add more fd lt, 4 repeating tasks

#EXERCISE 2,1 CREATE A FUNCTION to create square
# import turtle

# def square(t):
#     for i in range(4):
#         t.fd(100) #call a method, this means forward 100 pixels, draw a horizontal line
#         t.lt(90) #lt means left turn 90 degrees

# jack = turtle.Turtle() #passing jack through the function

# square(jack) #function call

# turtle.mainloop()

#SIMPLE REPETITION, full loop
# for i in range(4):
#     print('Hello!') #prints hello 4 times

# for i in range(4):
#     jack.fd(100)
#     jack.lt(90)

#EXERCISE 2.2, add length parameter (abstraction)
# import turtle 

# def square(t, length):
#     for i in range(4):
#         t.fd(length) 
#         t.lt(90) 

# jack = turtle.Turtle() #passing jack through the function

# square(jack, 200) #function call

# turtle.mainloop()

#EXERCISE 2.3
# import turtle 
        
# def polygon (t, length, n):
#     for i in range(n):
#         t.fd(length) 
#         t.lt(360/n)

# jack = turtle.Turtle() #passing jack through the function

# polygon(jack, 100, 3) #function call

# turtle.mainloop()

# #EXERCISE 2.4
# import turtle
# import math
        
# def polygon (t, length, n):
#     for i in range(n):
#         t.fd(length) 
#         t.lt(360/n)

# def circle (t, r):
#     circumference = 2 * math.pi * r
#     n = 50
#     length = circumference / n
#     polygon(t, length, n)

# jack = turtle.Turtle() 

# circle(jack, 150) 

# turtle.mainloop()


#EXERCISE 2.3 CONT
# import turtle
# import math
        
# def polygon (t, length, n):
#     for i in range(n):
#         t.fd(length) 
#         t.lt(360/n)

# def circle (t, r):
#     circumference = 2 * math.pi * r
#     n = int(circumference / 3) + 1
#     length = circumference / n
#     polygon(t, length, n)

# jack = turtle.Turtle() 

#polygon(t = jack, n = 50, length = 70) #keyword argument
# circle(jack, 150)

# turtle.mainloop()

#REFACTORING ARC 
# import turtle
# import math

# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = angle / n
    
#     for i in range(n):
#         t.fd(step_length)
#         t.lt(step_angle)

# jack = turtle.Turtle() 

# arc(jack, 100, 180)

# turtle.mainloop()


import turtle
import math

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle.
    """  
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

jack = turtle.Turtle() 

circle(jack, 100)

turtle.mainloop()