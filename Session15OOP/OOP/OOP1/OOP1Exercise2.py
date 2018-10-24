import math

#Exercise 2

# PART 1
#Write a definition for a class named Circle with attributes 
# center and radius, where center is a Point object and radius 
# is a number.
class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

# my_point = Point()
# my_point.x = 0
# my_point.y = 0

def print_point(p): 
    """Print a Point object in human-readable format."""
    print('({}, {})'.format(p.x, p.y))

#print_point(my_point)

class Circle:
    """
    Represents a circle in 2-D space.

    attributes: center (point) and radius (number)
    """

# my_circle = Circle()
# my_circle.r = 5 #radius
# my_circle.center = Point() 
# # my_circle.center.x = 0
# # my_circle.center.y = 0 
# my_circle.center = my_point #point


def print_circle(circ): #p is point, r is radius
    """Print a Circle object in human-readable format."""
    #print('center: ({}, {}).'.format(p.x, p.y))
    print('center point:')
    print_point(circ.center)
    print('radius:', circ.r)

# print_circle(my_circle)

# PART 2
#Instantiate a Circle object that represents a circle with its 
# center at (150, 100) and radius 75.

    # my_point = Point()
    # my_point.x = 150
    # my_point.y = 100

    # my_circle = Circle()
    # my_circle.r = 75
    # my_circle.center = Point() 
    # my_circle.center = my_point
    # print_circle(my_circle)

#Write a function named point_in_circle that takes a Circle and a 
# Point and returns True if the Point lies in or on the boundary 
# of the circle.
# d=(xp−xc)**2+(yp−yc)**2
# The point ⟨xp,yp⟩ is inside the circle if d<r, on the circle if d=r, 
# and outside the circle if d>r. You can save yourself a little work by 
# comparing d2 with r2 instead: the point is inside the circle if d2<r2,
#  on the circle if d2=r2, and outside the circle if d2>r2. Thus, you 
# want to compare the number (xp−xc)2+(yp−yc)2 with r2.
# my_point = Point()
# my_point.x = 150
# my_point.y = 100

# my_circle = Circle()
# my_circle.r = 75
# my_circle.center = Point() 
# my_circle.center = my_point
# print_circle(my_circle)
# point_in_circle(my_circle, (0, 0))

# testpoint = Point()
# testpoint.x = 0
# testpoint.y = 0

def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    x_diff = (p2.x - p1.x)
    y_diff = (p2.y - p1.y)
    distance = math.sqrt(x_diff**2 + y_diff**2)

    return distance

# distance_between_points(my_circle.center, testpoint)

def point_in_circle(circ, p):
    if distance_between_points(circ.center, p) > circ.r:
        return False
    else:
        return True

# point_in_circle(my_circle, testpoint)


#PART 4
#Write a function named rect_in_circle that takes a Circle and a 
# Rectangle and returns True if the Rectangle lies entirely in or 
# on the boundary of the circle.

# my_point = Point()
# my_point.x = 150
# my_point.y = 100

# my_circle = Circle()
# my_circle.r = 75
# my_circle.center = Point() 
# my_circle.center = my_point
# print_circle(my_circle)
# point_in_circle(my_circle, (0, 0))

class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """

# box = Rectangle()
# box.width = 100.0
# box.height = 200.0
# box.corner = Point() 
# box.corner.x = 0.0
# box.corner.y = 0.0

def rect_in_circle(circ, rect):
    for corner in rect:
        if distance_between_points(circ.center, rect.corner) <= circ.r:
            #how to check other corners?
            return True
        else:
            return False

#rect_in_circle(my_circle, box)

# def find_center(rect):
#     """Returns a Point at the center of a Rectangle.

#     rect: Rectangle

#     returns: new Point
#     """
#     p = Point()
#     p.x = rect.corner.x + rect.width / 2.0  #half of width
#     p.y = rect.corner.y + rect.height / 2.0  #half of height
#     return p #return center point


#PART 5
#Write a function named rect_circle_overlap that takes a 
# Circle and a Rectangle and returns True if any of the corners 
# of the Rectangle fall inside the circle. Or as a more challenging 
# version, return True if any part of the Rectangle falls inside the
#  circle.





def main():
    #PART 1
    # my_point = Point()
    # my_point.x = 0
    # my_point.y = 0
    # print_point(my_point)

    # my_circle = Circle()
    # my_circle.r = 5
    # my_circle.center = Point() 
    # # my_circle.center.x = 0
    # # my_circle.center.y = 0 
    # my_circle.center = my_point 

    # print_circle(my_circle)

    #PART 2
    # my_point = Point()
    # my_point.x = 150
    # my_point.y = 100

    # my_circle = Circle()
    # my_circle.r = 75
    # my_circle.center = Point() 
    # my_circle.center = my_point
    # print_circle(my_circle)

    #PART 3         HELP WHEN FORMATTING IN MAIN
    # my_point = Point()
    # my_point.x = 150
    # my_point.y = 100

    # my_circle = Circle()
    # my_circle.r = 75
    # my_circle.center = Point() 
    # my_circle.center = my_point
    # print_circle(my_circle)
    # point_in_circle(my_circle, (0, 0))

    # testpoint = Point()
    # testpoint.x = 0
    # testpoint.y = 0

    # distance_between_points(my_circle.center, testpoint)
    # point_in_circle(my_circle, testpoint)

if __name__ == '__main__': 
    main()