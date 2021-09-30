# Different geometry classes for lab3
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.arraysetops import isin


# ------------------------------------------------------------------------- #

class GeometryChecks:
    # "Class-global" settings for plots
    fig,ax = plt.figure(dpi=100),plt.axes()
    ax.grid()
    ax.set_aspect(1)
    cmap = plt.cm.get_cmap('Spectral')
    xmax,ymax = 10,10
    ax.set(xlabel="x coordinates", ylabel="y coordinates",
        title="Plot of your 2D geometry",
        xlim=[-xmax,xmax], ylim=[-ymax,ymax])

    # Do I need this?
    #def __init__(self) -> None:
    #    pass
    
    # Setter and getter for ORIGIN of object
    # TODO: handle 3D...
    @property
    def origin(self) -> float:
        return self._origin

    @origin.setter
    def origin(self, value: list) -> None:
        if self.validatetype(value[0]) and self.validatetype(value[1]):
            self._origin = [value[0],value[1]]
        # Bug fix: input x,y=0,0 did not create origin at all. This forces it.
        if not hasattr(self, '_origin'):
            self._origin = [0,0]


    # equality method
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

    # --------- Move object ---------
    def moveobj(self, xdiff:float, ydiff:float) -> None:
        """Moves origin of object"""
        self._origin[0] += xdiff
        self._origin[1] += ydiff
        return self._origin



    # check coords inside

    """Plot a singular point in the figure"""
    """
    def plotpoint(self, xcoord, ycoord) -> None:
    
        ax = self.ax
        ax.plot(xcoord, ycoord, '.', color=self.cmap(np.random.random(1)))"""


    # Sets settings for plots
    # TODO: change so that settings are changed when calling this method.

    def plotobject(self) -> Figure:
        plotobject = self.createplotobject(GeometryChecks.cmap)
        GeometryChecks.ax.add_artist(plotobject)

        

    """Set settings for plots and plots, increases plotcounter"""
    """
    def setplotsettings(self) -> None:
        
        fig,self.ax = plt.figure(dpi=100),plt.axes()
        self.ax.grid()
        self.ax.set(xlabel="x coordinates", ylabel="y coordinates",
            title="Plot of your 2D geometry",
            xlim=[-10,10], ylim=[-10,10])
        self.ax.set_aspect(1)
        self.cmap = plt.cm.get_cmap('Spectral')
        return fig, self.ax, self.cmap"""

    # Validate input numbers
    @staticmethod
    def validatetype(value:float) -> float:
        """Method to check input type"""
        if not isinstance(value, (int,float)):
            raise TypeError(f"Value '{value}' must be a float or int, not {type(value)}")
        return value
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
        Input are radius, x, and y coordinates (floats).
        Methods included here are
        - Area: computes area
        - Circumferance: computes circumferance
        - Equality: check if the area of two circles are the same
        - Check if a point is inside the circle
        """
        self.radius = radius
        self.origin = [originx,originy]

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


    """Plots object, run GeometryChecks.setplotsettings() first"""
    """
    def plotcircle(self) -> None:
        
        ax = self.ax
        circleplot = plt.Circle( 
            (self._origin[0],self._origin[1]), self._radius, alpha=0.7,
            color = self.cmap(np.random.random(1)))
        ax.add_artist(circleplot)"""

    def createplotobject(self, cmap):
        plotobject = plt.Circle( 
            (self._origin[0],self._origin[1]), self._radius, alpha=0.7,
            color = cmap(np.random.random(1)))
        return plotobject

        


    # Standard repr
    def __repr__(self) -> str:
        return f"A circle with radius {self._radius} and middle at x={self.origin[0]} and y={self.origin[1]}"


# ------------------------------------------------------------------------- #

class Rectangle(GeometryChecks):
    def __init__(self, width:float, height:float, originx:float, originy:float) -> None:
        """
        Rectangle objects
        -----------------
        Inputs are width, height, and x-y coordinates of centrum.
        Methods:
         - Compute area
         - Compute circumferance
         - Check if point is inside or outside object
        """
        self.rsize = [width,height]
        self.origin = [originx,originy]

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
        self.area = self.rsize[0] * self.rsize[1]
        return self.area
    
    def circumferance(self) -> float:
        """Compute circumferance of the rectangle"""
        self.circum = 2*(self.rsize[0] + self.rsize[1])
        return self.circum
    
    # --------- Check properties ---------
    def checkcoords(self, xcoord, ycoord) -> bool:
        """Check if coordinates are inside or outside rectangle"""
        # Distances to origin
        xdist = abs(xcoord - self._origin[0])
        ydist = abs(ycoord - self._origin[1])
        # Check insider status
        if xdist <= 0.5*self.rsize[0] and ydist <= 0.5*self.rsize[1]:
            return True
        else:
            return False

    # Standard repr
    def __repr__(self) -> str:
        return f"A rectangle with width={self._rsize[0]}, height={self._rsize[1]}, and origin at x,y={self._origin[0]},{self._origin[1]}."


# ------------------------------------------------------------------------- #


# Cube

# Sphere
