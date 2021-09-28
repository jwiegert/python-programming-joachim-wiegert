# Different geometry classes for lab3
import numpy as np
import matplotlib.pyplot as plt


# ------------------------------------------------------------------------- #

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
    def translateorigin(self, xdiff:float, ydiff:float) -> list:
        if self.validatetype(xdiff) and self.validatetype(ydiff):
            neworigin = []
            neworigin.append(self._origin[0] + xdiff)
            neworigin.append(self._origin[1] + ydiff)
        return neworigin

    # check coords inside

    # Sets settings for plots
    # TODO: change so that settings are changed when calling this method.
    def setplotsettings(self) -> None:
        """Set settings for plots and plots, increases plotcounter"""
        fig,self.ax = plt.figure(dpi=100),plt.axes()
        self.ax.grid()
        self.ax.set(xlabel="x coordinates", ylabel="y coordinates",
            title="Plot of your 2D geometry",
            xlim=[-10,10], ylim=[-10,10])
        self.ax.set_aspect(1)
        self.cmap = plt.cm.get_cmap('Spectral')
        return fig, self.ax, self.cmap

    # Validate input numbers
    @staticmethod
    def validatetype(value:float) -> float:
        """Method to check input type"""
        if not isinstance(value, (int,float)):
            raise TypeError(f"Value '{value}' must be a float or int, not {type(value)}")
        return value
    @staticmethod
    def validatevalue(value:float) -> float:
        if value < 0:
            raise ValueError(f"Value {value} must be positive, not negative")
        return value



    def __repr__(self) -> str:
        return f"This class is a parent to the geometry shapes and error checks the geometry"


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
    @property
    def origin(self) -> float:
        return self._origin

    @radius.setter
    def radius(self, value: float) -> None:
        if self.validatetype(value) and self.validatevalue(value):
            self._radius = value
    @origin.setter
    def origin(self, value: list) -> None:
        if self.validatetype(value[0]) and self.validatetype(value[1]):
            self._origin = [value[0],value[1]]

    # Compute properties ----------------------------
    def comparea(self) -> float:
        """Compute area of the circle"""
        self.area = np.pi*self._radius**2
        return self.area
    
    def circumferance(self) -> float:
        """Compute circumferance of a circle"""
        self.circum = 2*np.pi*self._radius
        return self.circum
    
    # Move circle ----------------------------
    def movecircle(self, xdiff:float, ydiff:float) -> None:
        """Moves origin of circle"""
        self._origin = self.translateorigin(xdiff,ydiff)
        return f"New origin is at {self._origin}"

    # Check properties ----------------------------
    def __eq__(self, other) -> bool:
        """Compare the area of two circles"""
        self.area = self.comparea()
        other.area = other.comparea()
        if self.area == other.area:
            return True
        else:
            return False

    def checkcoords(self, xcoord, ycoord) -> bool:
        """Check if coordinates are inside or outside circle"""
        # Compute euclidian distance between new point and circle origin
        distance = np.sqrt((self._origin[0]-xcoord)**2 + (self._origin[1]-ycoord)**2)
        # Check if this is inside the circle radius
        if distance <= self._radius:
            return True
        else:
            return False

    def plotpoint(self, xcoord, ycoord) -> None:
        ax = self.ax
        ax.plot(xcoord, ycoord, '.', color=self.cmap(np.random.random(1)))

    def plotcircle(self) -> None:
        """Plots object, run GeometryChecks.setplotsettings() first"""
        ax = self.ax
        circleplot = plt.Circle( 
            (self._origin[0],self._origin[1]), self._radius, alpha=0.7,
            color = self.cmap(np.random.random(1)))
        ax.add_artist(circleplot)


        



    def __repr__(self) -> str:
        return f"A circle with radius {self._radius} and middle at x={self.origin[0]} and y={self.origin[1]}"


# ------------------------------------------------------------------------- #

class Rectangle(GeometryChecks):
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"A rectangle with x-width=, y-width=, "


# Cube

# Sphere
