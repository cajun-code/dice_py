"""
Author : Allan Davis

Answer to question 1 for CCP Games

To Run the test the test just type:

python -m doctest rectangle.py

"""

class Point(object):
    """ A point class """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class Rectangle(object):
    def __init__(self, x, y, width, height):
        self.left = Point(x, y)
        self.width = width
        self.height = height
        self.right = Point(self.left.x + width -1, self.left.y + height -1)
    
    def is_within(self, point):
        """
        Check to see if point is within Rectangle
        
        >>> rect = Rectangle(0,0, 5, 5)
        >>> rect.is_within(Point(2,4))
        True
        
        >>> rect = Rectangle(0,0, 5,5)
        >>> rect.is_within(Point(5,5))
        False
        """
        return (self.left.x <= point.x and self.right.x >= point.x) and (self.left.y <= point.y and self.right.y >= point.y)
    
    