import math

#programmer-defined type is also called a class
class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

# my_point = Point()
# my_point
jack = Point
# print(jack)
# print(type(jack))

#points can have attributes and assign values to it then can print
jack.x = 3
jack.y = 4

# print(jack.x, jack.y)

# #create new variable x, this x has nothing to do with jack.x
# x = jack.y #go to jack get the value of y as attribute of jack (4)
# print(x) #now x = 4

# import math
# print('(%g, %g)' % (jack.x, jack.y))
# distance = math.sqrt(jack.x**2 + jack.y**2)
# print(distance)

def print_point(p): #p must have attributes for x and y
    """Print a Point object in human-readable format."""
    print('({}, {}).'.format(p.x, p.y))

print_point(jack)

#add another point
jonathan = Point()
jonathan.x = 50
jonathan.y = 50

print_point(jonathan)

#check for attributes
print(hasattr(jack, 'x')) #True
print(hasattr(jack, 'z')) #False


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

print(distance_between_points(jack, jonathan))




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

angela = Rectangle() #angela the rectangle has 3 attributes
angela.width = 100
angela.height = 200
angela.corner = jack #jack is a point with x and y


def find_center(rect):
    """Returns a Point at the center of a Rectangle.

    rect: Rectangle

    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0  #half of width
    p.y = rect.corner.y + rect.height / 2.0  #half of height
    return p #return center point


sarah = (find_center(angela))
print_point(sarah)

def print_rectangle(rect):
    print('width:', rect.width, 'height:', rect.height)
    print('the lower-left corner:')
    print_point(rect.corner)


#objects are mutable
def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight

print_rectangle(angela)
grow_rectangle(angela, 50, 100)
# angela.width += 50
# angela.height += 100

print('rectangle after growth')
print_rectangle(angela)


def main():
    my_point = Point()
    # print(Point.__doc__)
    # my_point.x = 3
    # my_point.y = 4
    # print('My point', end=' ')
    # print_point(my_point)

    # print('Is my_point an instance of Point?', isinstance(my_point, Point))
    # print('Is my_point an instance of Rectangle?',
    #       isinstance(my_point, Rectangle))
    # print('Does my_point have an attribute x?', hasattr(my_point, 'x'))
    # print('Does my_point have an attribute z?', hasattr(my_point, 'z'))

    # box = Rectangle()
    # box.width = 100.0
    # box.height = 200.0
    # box.corner = Point()
    # box.corner.x = 0.0
    # box.corner.y = 0.0

    # print('Does box have an attribute x?', hasattr(box, 'x'))

    # print('Does box have an attribute corner?', hasattr(box, 'corner'))

    # print('Rectangle has these:', dir(box))

    # center = find_center(box)
    # print('center', end=' ')
    # print_point(center)

    # print(box.width)
    # print(box.height)
    # print('grow')
    # grow_rectangle(box, 50, 100)
    # print(box.width)
    # print(box.height)


if __name__ == '__main__':
    main()
