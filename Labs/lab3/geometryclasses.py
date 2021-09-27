# Different geometry classes for lab3
import numpy as np

class GeometryChecks:
    def __init__(self) -> None:
        pass
    

    # print area
    # f"Area of object is {self.area:.2f}."

    # print circumferance

    # print volume

    # print surface area

    # equality method

    # translate x-y

    # check coords inside


    def __repr__(self) -> str:
        return f"This class is a parent to the geometry shapes and error checks the geometry"




class Circle(GeometryChecks):
    def __init__(self, radius:float, originx:float, originy: float) -> None:
        self.radius = radius
        self.origin = [originx,originy]

    # Use geometrycheck to check inputs

    def area(self) -> float:
        self.area = np.pi * self.radius**2
        return self.area
    
    def circumferance(self) -> float:
        self.circum = 2*np.pi*self.radius
        return self.circum
    

    def __repr__(self) -> str:
        return f"A circle with radius {self.radius} and middle at x={self.origin[0]} and y={self.origin[1]}"




class Rectangle(GeometryChecks):
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"A rectangle with x-width=, y-width=, "


# Cube

# Sphere
