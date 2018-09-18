import turtle
import math


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


# def polygon(t, length, n):
#     for i in range(n):
#         t.fd(length)
#         t.lt(360/n)


# def circle(t, r):
#     circumference = 2 * math.pi * r
#     n = int(circumference / 3) + 1
#     length = circumference / n
#     polygon(t, length, n)


# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = angle / n

#     for i in range(n):
#         t.fd(step_length)
#         t.lt(step_angle)


def polyline(t, n, length, angle):
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

# square(jack, 200)
# polygon(jack, 10, 60)
# circle(jack, 150)
# polygon(n=7, t=jack, length=70)
# arc(jack, 100, 270)
# polyline(jack, 3, 100, 30)
circle(jack, 100)

turtle.mainloop()