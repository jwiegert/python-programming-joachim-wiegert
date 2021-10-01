# Different geometry classes for lab3
from matplotlib.figure import Figure
from matplotlib.patches import Patch
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.arraysetops import isin


# ------------------------------------------------------------------------- #

class GeometryChecks:
    """
    Parent class to geometrical objects
    - For methods check children classes:
      . GeometryChecks.Circle()
      . GeometryChecks.Rectangle()
      . GeometryChecks.Cube()
      . GeometryChecks.Sphere()
    """

    # "Global" settings for plots
    # TODO: there are some bugs here still!
    fig,ax = plt.figure(dpi=100),plt.axes()
    ax.grid()
    ax.set_aspect(1)
    cmap = plt.cm.get_cmap('Spectral')
    xmax,ymax = 10,10
    ax.set(xlabel="x coordinates", ylabel="y coordinates",
        title="Plot of your 2D geometry",
        xlim=[-xmax,xmax], ylim=[-ymax,ymax])

    """Setter and getter for origin coordinates of object"""
    @property
    def origin(self) -> list:
        return self._origin
    # Origin-setter handles any number of dimensions
    @origin.setter
    def origin(self, value: list) -> None:
        outvalue = []
        for val in value:
            if self.validatetype(val):
                outvalue.append(val)
        self._origin = outvalue

    # Equality method
    def __eq__(self, other) -> bool:
        """Compares class and surface area of two objects"""
        if type(self) == type(other):
            self.area = self.comparea()
            other.area = other.comparea()
            if self.area == other.area:
                return True
            else:
                return False, "Objects have different surface areas"
        else:
            return False, "Objects are different classes"

    # Move object
    def moveobj(self, xdiff:float, ydiff:float) -> None:
        """Moves origin of object"""
        self._origin[0] += xdiff
        self._origin[1] += ydiff
        return self._origin

    # Plot methods
    # TODO: change so that fig is not always created...
    # TODO: Add 3D-plot method for cube and sphere
    def plotobject(self) -> Figure:
        """Plots 2D object"""
        plotobject = self.createplotobject(GeometryChecks.cmap)
        GeometryChecks.ax.add_artist(plotobject)

    def plotpoint(self, xcoord, ycoord) -> None:
        """Plot a singular point in the figure"""
        GeometryChecks.ax.plot(xcoord, ycoord, '.', color=self.cmap(np.random.random(1)))

    # Validate input numbers
    @staticmethod
    def validatetype(value:float) -> float:
        """Method to check input type"""
        if not isinstance(value, (int,float)):
            raise TypeError(f"Value '{value}' must be a float or int, not {type(value)}")
        return True
    @staticmethod
    def validatevalue(value:float) -> float:
        if value <= 0:
            raise ValueError(f"Value {value} must be positive, not negative or zero")
        return value

    # Default repper
    def __repr__(self) -> str:
        return f"This class is parent to geometry shapes with general methods for all"

# ------------------------------------------------------------------------- #

class Circle(GeometryChecks):
    def __init__(self, radius:float, originx:float, originy: float) -> None:
        """
        Circle objects
        --------------
        - 3 inputs: radius, x and y coordinates of origin of objects.
        Methods included here are:
        - print(): Prints input coordinates and size
        - comparea(): Computes area
        - circumferance(): Computes circumferance
        - checkcoords(): Check if a point is inside the object
        - moveobj(): Moves object's origin
        - plotobject(): Plots object
        - plotpoint(): Plots a specific point
        - == (i.e. __eq__): Equality compares object class and object area.
                            If both are equal it returns True. If False, it
                            returns a tuple with False at [0] and what was
                            not equal as [1]

        Supplementary methods
        ------------------
        - createplotobject(): Creates patch for the plot method
        - validatetype(): Checks that input data are int or float
        - validatevalue(): Checks that input data are positive numbers
        """
        self.radius = radius
        self.origin = [originx,originy]

    """Setter and getter for circle radius"""
    @property
    def radius(self) -> float:
        return self._radius
    @radius.setter
    def radius(self, value: float) -> None:
        if self.validatetype(value) and self.validatevalue(value):
            self._radius = value
        if not hasattr(self, '_radius'):
            raise ValueError("Radius can not be zero.")


    # --------- Compute properties ---------
    def comparea(self) -> float:
        """Compute area of the circle"""
        self.area = np.pi*self._radius**2
        return self.area
    
    def circumferance(self) -> float:
        """Compute circumferance of a circle"""
        self.circum = 2*np.pi*self._radius
        return self.circum

    # --------- Check properties ---------
    def checkcoords(self, xcoord, ycoord) -> bool:
        """Check if coordinates are inside or outside circle"""
        # Compute euclidian distance between new point and circle origin
        distance = np.sqrt((self._origin[0]-xcoord)**2 + (self._origin[1]-ycoord)**2)
        # Check if this is inside the circle radius
        if distance <= self._radius:
            return True
        else:
            return False

    def createplotobject(self, cmap) -> Patch:
        """Creates pathch for parent plot method"""
        plotobject = plt.Circle( 
            (self._origin[0],self._origin[1]), self._radius, alpha=0.7,
            color = cmap(np.random.random(1)))
        return plotobject

    # Standard repr
    def __repr__(self) -> str:
        return f"A circle with radius {self._radius} and origin at x,y={self.origin[0]},{self.origin[1]}"

# ------------------------------------------------------------------------- #

class Rectangle(GeometryChecks):
    def __init__(self, width:float, height:float, originx:float, originy:float) -> None:
        """
        Rectangle objects
        -----------------
        - 4 inputs: width and height, x and y coordinates of origin of objects.
        Methods included here are:
        - print(): Prints input coordinates and size
        - comparea(): Computes area
        - circumferance(): Computes circumferance
        - checkcoords(): Check if a point is inside the object
        - moveobj(): Moves object's origin
        - plotobject(): Plots object
        - plotpoint(): Plots a specific point
        - == (i.e. __eq__): Equality compares object class and object area.
                            If both are equal it returns True. If False, it
                            returns a tuple with False at [0] and what was
                            not equal as [1]

        Supplementary methods
        ------------------
        - createplotobject(): Creates patch for the plot method
        - validatetype(): Checks that input data are int or float
        - validatevalue(): Checks that input data are positive numbers
        """
        self.rsize = [width,height]
        self.origin = [originx,originy]

    """Setter and getter for rectangle sizes"""
    @property
    def rsize(self) -> float:
        return self._rsize
    @rsize.setter
    def rsize(self, value: list) -> None:
        if self.validatetype(value[0]) and self.validatevalue(value[0]) and\
            self.validatetype(value[1]) and self.validatevalue(value[1]):
            self._rsize = [value[0],value[1]]

    # --------- Compute properties ---------
    def comparea(self) -> float:
        """Compute area of the rectangle"""
        self.area = self._rsize[0] * self._rsize[1]
        return self.area
    
    def circumferance(self) -> float:
        """Compute circumferance of the rectangle"""
        self.circum = 2*(self._rsize[0] + self._rsize[1])
        return self.circum
    
    # --------- Check properties ---------
    def checkcoords(self, xcoord, ycoord) -> bool:
        """Check if coordinates are inside or outside rectangle"""
        # Distances to origin
        xdist = abs(xcoord - self._origin[0])
        ydist = abs(ycoord - self._origin[1])
        # Check insider status
        if xdist <= 0.5*self._rsize[0] and ydist <= 0.5*self._rsize[1]:
            return True
        else:
            return False

    def createplotobject(self, cmap) -> Patch:
        """Creates patch for parent plot method"""
        anchorpoint = [orig - 0.5*rsiz for orig,rsiz in zip(self._origin,self._rsize)]
        plotobject = plt.Rectangle(anchorpoint,self._rsize[0],self._rsize[1], 
            alpha=0.7,color = cmap(np.random.random(1)))
        return plotobject

    # Standard repr
    def __repr__(self) -> str:
        return f"A rectangle with width={self._rsize[0]}, height={self._rsize[1]}, and origin at x,y={self._origin[0]},{self._origin[1]}."

# ------------------------------------------------------------------------- #
# 3D objects

# Cube
class Cube(GeometryChecks):
    def __init__(self, side:float, originx:float, originy:float, originz: float) -> None:
        """
        Cube objects
        -----------------
        - 4 inputs: length of size, x, y and z coordinates of origin of objects.
        Methods included here are:
        - print(): Prints input coordinates and size
        - compvolume(): Computes volume
        - comparea(): Computes surface area
        - checkcoords(): Check if a point is inside the object
        - moveobj(): Moves object's origin
        - plotobject(): Plots object
        - plotpoint(): Plots a specific point
        - == (i.e. __eq__): Equality compares object class and object area.
                            If both are equal it returns True. If False, it
                            returns a tuple with False at [0] and what was
                            not equal as [1]

        Supplementary methods
        ------------------
        createplotobject(): Creates patch for the plot method
        validatetype(): Checks that input data are int or float
        validatevalue(): Checks that input data are positive numbers
        """
        self.side = side
        self.origin = [originx,originy,originz]

    """Setter and getter for cube size"""
    @property
    def side(self) -> float:
        return self._side
    @side.setter
    def side(self, value: list) -> None:
        if self.validatetype(value) and self.validatevalue(value):
            self._side = value

    # --------- Compute properties ---------
    def compvolume(self):
        """Computes volume of cube"""
        self.volume = self._side**3
        return self.volume




    def comparea(self) -> float:
        """Compute area of the rectangle"""
        self.area = self._rsize[0] * self._rsize[1]
        return self.area
    
    def circumferance(self) -> float:
        """Compute circumferance of the rectangle"""
        self.circum = 2*(self._rsize[0] + self._rsize[1])
        return self.circum
    
    # --------- Check properties ---------
    def checkcoords(self, xcoord, ycoord) -> bool:
        """Check if coordinates are inside or outside rectangle"""
        # Distances to origin
        xdist = abs(xcoord - self._origin[0])
        ydist = abs(ycoord - self._origin[1])
        # Check insider status
        if xdist <= 0.5*self._rsize[0] and ydist <= 0.5*self._rsize[1]:
            return True
        else:
            return False

    def createplotobject(self, cmap) -> Patch:
        """Creates patch for parent plot method"""
        anchorpoint = [orig - 0.5*rsiz for orig,rsiz in zip(self._origin,self._rsize)]
        plotobject = plt.Rectangle(anchorpoint,self._rsize[0],self._rsize[1], 
            alpha=0.7,color = cmap(np.random.random(1)))
        return plotobject





    # Standard repr
    def __repr__(self) -> str:
        return f"A cube with side={self._side} and origin at x,y,z={self._origin[0]},{self._origin[1]},{self._origin[2]}."



# Sphere
