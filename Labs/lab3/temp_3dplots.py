# Placeholder file for 3D-plot codes.
# Saved for later reference in case I can get it to work.



# from class GeometryChecks()
# 3D Plot methods
#@staticmethod
def plotsettings_3d(xmax:float, ymax:float, zmax:float):
    """
    Set global settings for 3D plots
    - +/- xmax and ymax: limits for the plot axis ranges
    """
    # Checks correct-ness of axis range limits
    if GeometryChecks.validatetype(xmax) and GeometryChecks.validatevalue(xmax) and \
        GeometryChecks.validatetype(ymax) and GeometryChecks.validatevalue(ymax) and \
        GeometryChecks.validatetype(zmax) and GeometryChecks.validatevalue(zmax):
        GeometryChecks.fig3 = plt.figure(dpi=100)
        GeometryChecks.ax3 = plt.axes(projection = '3d')
        GeometryChecks.ax3.grid()
        GeometryChecks.cmap = plt.cm.get_cmap('Spectral')
        GeometryChecks.ax3.set(
            xlabel="x coordinates", ylabel="y coordinates", zlabel="z coordinates",
            title="3D geometrical objects",
            xlim=[-xmax,xmax],ylim=[-ymax,ymax],zlim=[-zmax,zmax])

def plotobject_3d(self) -> Figure:
    """
    Plots 3D object as wireframe
    - Must run gc.GeometryChecks.plotsettings_3d() before plotting to get correct settings.
    """
    plotobject = self.createplotobject(GeometryChecks.cmap)
    GeometryChecks.ax3.plot_wireframe(
        plotobject[0], plotobject[1], plotobject[2], color=plotobject[3])

def plotpoint_3d(self, xcoord:float, ycoord:float, zcoord:float) -> Figure:
    """Plot a singular point in a 3D figure"""
    GeometryChecks.ax3.plot(xcoord, ycoord, zcoord, '.', color=self.cmap(np.random.random(1)))


# From Cube()


# TODO
# Plotobject
def createplotobject(self, cmap) -> list:
    """Creates list for parent plot method"""
    # Code based on examples here
    # https://stackoverflow.com/questions/11140163/plotting-a-3d-cube-a-sphere-and-a-vector-in-matplotlib
    # Create x-y-z-coordinates for cube wire frame.
    x = [self._origin[0]-0.5*self._side + i for i in range(self._side+1)]
    y = [self._origin[1]-0.5*self._side + i for i in range(self._side+1)]
    z = [self._origin[2]-0.5*self._side + i for i in range(self._side+1)]
    plotobject = [x, y, z, cmap(np.random.random(1))]
    #return plotobject
    return x


# From Sphere()

# Plotobject
def createplotobject(self, cmap) -> list:
    """Creates tuple for parent plot method"""
    # Code based on examples here
    # https://stackoverflow.com/questions/11140163/plotting-a-3d-cube-a-sphere-and-a-vector-in-matplotlib
    u,v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = self._radius*np.cos(u)*np.sin(v) + self._origin[0]
    y = self._radius*np.sin(u)*np.sin(v) + self._origin[1]
    z = self._radius*np.cos(v)           + self._origin[2]
    plotobject = [x, y, z, cmap(np.random.random(1))]
    return plotobject
