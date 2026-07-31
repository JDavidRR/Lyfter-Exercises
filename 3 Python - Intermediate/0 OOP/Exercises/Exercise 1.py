"""
Cree una clase de Circle con:
- Un atributo de radius (radio).
- Un método de get_area que retorne su área.
"""
from math import pi

class Circle ():
    radius = 0
    def __init__(self,radius_param):
        self.radius = radius_param

    def get_area(self):
        return pi * (self.radius ** 2)

my_circle = Circle(10)
print (my_circle.get_area())