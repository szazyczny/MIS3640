#EXERCISE 3

#CIRCLE WITH 5 PETALS
# import turtle
# import math
# bob=turtle.Turtle()

# def polygon (t, length, n):
#     for i in range(n):
#         t.fd(length) 
#         t.lt(360/n)

# def circle (t, r):
#     """
#     Draws circle with given radius.  t is a turtle.
#     """  
#     circumference = 2 * math.pi * r
#     n = int(circumference / 3) + 1
#     length = circumference / n
#     polygon(t, length, n)

# circle(bob, 100)

# radius= 100
# petals= 5

# def arc(t,r):  #bob the turtle,corner-to-corner length (radius) of petal (assume 60 degree central angle of sector for simplicity)
#     c=2*math.pi*r #Circumference of circle
#     ca=c/(360/60)  #Circumference of arc (assume 60 degree central angle of sector as above)
#     n=int(ca/3)+1  #number of segments
#     l=ca/n  #length of segment
#     for i in range(n):
#         t.fd(l)
#         t.lt(360/(n*6))


# def petal(t,r):
#      """
#     Draws flower petals with defined # of petals and with given radius.  t is a turtle.
#     """  
#     arc(t,r)
#     t.lt(180-60)
#     arc(t,r)
#     t.rt(360/petals-30)  # this will take care of the correct angle b/w petals

# #draw_petal(bob,radius)

# for i in range(petals):
#     petal(bob,radius)
#     bob.lt(360/4)


# turtle.mainloop()


#YIN YANG SYMBOL
from turtle import *

RAD = 100
RAD2 = RAD / 2
RAD6 = RAD / 6

degrees() # Switch to degrees
# Draw the circle, radius 100, half black
fillcolor('black')
begin_fill()
circle(RAD, 180)
end_fill()
circle(RAD, 180)

# Draw smaller black semi-circle
left(180)
penup()
goto(0, RAD)
pendown()
begin_fill()
circle(RAD2, 180)
end_fill()

# Draw smaller white semi-circle
penup()
goto(0, RAD)
pendown()
fillcolor('white')
begin_fill()
circle(RAD2, 180)
end_fill()

# Draw smaller circles
penup()
goto(0, RAD2 + RAD6)
begin_fill()
circle(RAD6)
end_fill()

fillcolor('black')
goto(0, 2 * (RAD - RAD6))
begin_fill()
circle(RAD6)
end_fill()
