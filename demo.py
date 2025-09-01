"""Dummy challenge for Kitt Demo"""



def circle_area(radius):
    """Returns the area of the circle of given radius"""
import math  # keep import at the top

def circle_area(radius):
    """Returns the area of the circle of given radius"""
    if radius <= 0:  # check for negative or zero radius
        return 0
    return math.pi * radius ** 2
