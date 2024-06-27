import numpy as np

class Circle:

    def __init__(self, radius):
      self.radius = radius

    def calculateArea(self):
      self.area = np.pi * self.radius ** 2
      return self.area

    def calculatePerimeter(self):
      self.perimeter = 2 * np.pi * self.radius
      return self.perimeter

circle1 = Circle(5)

print(circle1.calculateArea())
print(circle1.calculatePerimeter())
