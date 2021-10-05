# Geometry classes for lab3
# -------------------------
#
# Import libraries
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.patches import Patch
import numpy as np

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

    """Setter and getter for origin coordinates of object"""
    @property
    def origin(self) -> list:
        return self._origin
    @origin.setter
    def origin(self, value: list) -> None:
        # Origin-setter handles any number of dimensions
        # and does error handling.
        outvalue = []
        for val in value:
            if self.validatetype(val):
                outvalue.append(val)
        self._origin = outvalue

    # Equality method
    def __eq__(self, other) -> bool:
        """
        Compares class and surface area of two objects
        - Inequality returns both [0]: boolean False, and [1]: string with explanation.
        - Equality returns only boolean True.
        """
        if type(self) == type(other):
            if self.comparea() == other.comparea():
                return True
            else:
                return False, "Objects have different surface areas"
        else:
            return False, "Objects are different classes"

    # Move object
    def moveobj_2d(self, xdiff:float, ydiff:float) -> list:
        """Moves origin of 2D object"""
        self._origin[0] += xdiff
        self._origin[1] += ydiff
        return self._origin

    def moveobj_3d(self, xdiff:float, ydiff:float, zdiff:float) -> list:
        """Moves origin of 3D object"""
        self._origin[0] += xdiff
        self._origin[1] += ydiff
        self._origin[2] += zdiff
        return self._origin

    # 2D Plot methods
    def plotobject_2d(self) -> Figure:
        """
        Plots 2D object
        - Must run gc.GeometryChecks.plotsettings_2d() before plotting to get correct settings.
        """
        plotobject = self.createplotobject(GeometryChecks.cmap)
        GeometryChecks.ax.add_artist(plotobject)

    def plotpoint_2d(self, xcoord:float, ycoord:float) -> Figure:
        """Plot a singular point in the figure"""
        GeometryChecks.ax.plot(xcoord, ycoord, '.', color=self.cmap(np.random.random(1)))

    # "Global" settings for plots
    @staticmethod
    def plotsettings_2d(xmax:float, ymax:float) -> None:
        """
        Set global settings for 2D plots
        - +/- xmax and ymax: limits for the plot axis ranges
        Required if all objects need to be plotted in the same figure.
        """
        # Check correct-ness of axis range limits
        if GeometryChecks.validatetype(xmax) and GeometryChecks.validatevalue(xmax) and \
           GeometryChecks.validatetype(ymax) and GeometryChecks.validatevalue(ymax):
            # Set global settings for subsequent plots
            GeometryChecks.fig = plt.figure(dpi=100)
            GeometryChecks.ax = plt.axes(xlabel="x coordinates", ylabel="y coordinates",
                title="2D geometrical objects", xlim=[-xmax,xmax], ylim=[-ymax,ymax])
            GeometryChecks.ax.grid()
            GeometryChecks.ax.set_aspect(1)
            GeometryChecks.cmap = plt.cm.get_cmap('Spectral')

    # Validate input numbers
    @staticmethod
    def validatetype(value:float) -> bool:
        """Checks input type"""
        if not isinstance(value, (int,float)):
            raise TypeError(f"Value '{value}' must be a float or int, not {type(value)}")
        return True
    @staticmethod
    def validatevalue(value:float) -> bool:
        """Checks input data (> 0)"""
        if value <= 0:
            raise ValueError(f"Value {value} must be positive, not negative or zero")
        return True

    # Default repper
    def __repr__(self) -> str:
        return f"This class is parent to geometry classes and contain general methods."

# ------------------------------------------------------------------------- #
# 2D objects

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
        - moveobj_2d(): Moves object's origin
        - plotsettings_2d(): Sets global settings for plots
        - plotobject(): Plots object
        - plotpoint(): Plots a specific point
        - == (i.e. __eq__): Equality compares object class and object area.
                            If both are equal it returns True. If False, it
                            returns a tuple with False at [0] and what was
                            not equal as [1]

        Ancillary methods
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
        """
        Creates patch for parent plot method
        - Use plotobject_2d() to plot!
        """
        plotobject = plt.Circle( 
            (self._origin[0],self._origin[1]), self._radius, alpha=0.7,
            color = cmap(np.random.random(1)))
        return plotobject

    # Standard repr
    def __repr__(self) -> str:
        return f"A circle with radius {self._radius} and origin at x,y={self.origin[0]},{self.origin[1]}"



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
        - moveobj_2d(): Moves object's origin
        - plotsettings_2d(): Sets global settings for plots
        - plotobject(): Plots object
        - plotpoint(): Plots a specific point
        - == (i.e. __eq__): Equality compares object class and object area.
                            If both are equal it returns True. If False, it
                            returns a tuple with False at [0] and what was
                            not equal as [1]

        Ancillary methods:
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
        if self.validatetype(value[0]) and self.validatevalue(value[0]) and \
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
    
    # --------- Check properties and objects ---------
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
        """
        Creates patch for parent plot method
        - Use plotobject_2d() to plot!
        """
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
        - 4 inputs: length of side, x, y and z coordinates of origin of object.
        Methods included here are:
        - print(): Prints input coordinates and size
        - compvolume(): Computes volume
        - comparea(): Computes surface area
        - checkcoords(): Check if a point is inside the object
        - moveobj_3d(): Moves object's origin
        - == (i.e. __eq__): Equality compares object class and object area.
                            If both are equal it returns True. If False, it
                            returns a tuple with False at [0] and what was
                            not equal as [1]

        Ancillary methods
        ------------------
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
    def side(self, value: float) -> None:
        if self.validatetype(value) and self.validatevalue(value):
            self._side = value

    # --------- Compute properties ---------
    def compvolume(self) -> float:
        """Computes volume of cube"""
        self.volume = self._side**3
        return self.volume

    def comparea(self) -> float:
        """Compute surface area of the cube"""
        self.area = 6*self.side**2
        return self.area
   
    # --------- Check properties ---------
    def checkcoords(self, xcoord, ycoord, zcoord) -> bool:
        """Check if coordinates are inside or outside rectangle"""
        # Distances to origin
        xdist    = abs(xcoord - self._origin[0])
        ydist    = abs(ycoord - self._origin[1])
        zdist    = abs(zcoord - self._origin[2])
        halfside = 0.5*self._side
        # Check insider status
        if xdist <= halfside and ydist <= halfside and zdist <= halfside:
            return True
        else:
            return False

    # Standard repr
    def __repr__(self) -> str:
        return f"A cube with side={self._side} and origin at x,y,z={self._origin[0]},{self._origin[1]},{self._origin[2]}."



# Sphere
class Sphere(GeometryChecks):
    def __init__(self, radius:float, originx:float, originy:float, originz: float) -> None:
        """
        Sphere objects
        -----------------
        - 4 inputs: radius and x, y and z coordinates of origin of objects.
        Methods included here are:
        - print(): Prints input coordinates and size
        - compvolume(): Computes volume
        - comparea(): Computes surface area
        - checkcoords(): Check if a point is inside the object
        - moveobj_3d(): Moves object's origin
        - == (i.e. __eq__): Equality compares object class and object area.
                            If both are equal it returns True. If False, it
                            returns a tuple with False at [0] and what was
                            not equal as [1]

        Ancillary methods
        ------------------
        validatetype(): Checks that input data are int or float
        validatevalue(): Checks that input data are positive numbers
        """
        self.radius = radius
        self.origin = [originx,originy,originz]

    """Setter and getter for cube size"""
    @property
    def radius(self) -> float:
        return self._radius
    @radius.setter
    def radius(self, value: float) -> None:
        if self.validatetype(value) and self.validatevalue(value):
            self._radius = value

    # --------- Compute properties ---------
    def compvolume(self) -> float:
        """Computes volume of sphere"""
        self.volume = 4/3 * np.pi * self._radius**3
        return self.volume

    def comparea(self) -> float:
        """Computes surface area of sphere"""
        self.area = 4 * np.pi * self._radius**2
        return self.area
   
    # --------- Check properties ---------
    def checkcoords(self, xcoord, ycoord, zcoord) -> bool:
        """Checks if coordinates are inside or outside sphere"""
        # Distance between new point and sphere origin
        distance = np.sqrt((self._origin[0]-xcoord)**2 + \
                           (self._origin[1]-ycoord)**2 + \
                           (self._origin[2]-zcoord)**2)
        # Check if this is inside the circle radius
        if distance <= self._radius:
            return True
        else:
            return False

    # Standard repr
    def __repr__(self) -> str:
        return f"A sphere with radius={self._radius} and origin at x,y,z={self._origin[0]},{self._origin[1]},{self._origin[2]}."
