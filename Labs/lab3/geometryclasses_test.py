import geometryclasses as gc
import unittest
import numpy as np

# Things to tests
# - check input numbers, type and valuerror
# - compute area and - compute circumferance
# - move object
# - check point inside/outside
# - check equality
# - check repr
# - check plot?
# SPECIFIC FOR 3D
# - check surface area and volume

class TestGeometry(unittest.TestCase):

    # ---------- Setup ----------
    def setUp(self) -> None:

        # Create a few standard 2D objects
        self.c1 = gc.Circle(2,1,1) # Same area as c2
        self.c2 = gc.Circle(2,-1,-1)
        self.c3 = gc.Circle(1,-1,0)
        self.r1 = gc.Rectangle(1,2,-3,0) # Same area as r2
        self.r2 = gc.Rectangle(2,1,3,0)
        self.r3 = gc.Rectangle(0.7,0.3,0,3)

        # Create a few standard 3D objects
        self.cu1 = gc.Cube(1.5,1,2,3) # Same volume&area as cu2
        self.cu2 = gc.Cube(1.5,-1,-2,-3)
        self.cu3 = gc.Cube(0.5,0,0,0)
        self.s1 = gc.Sphere(1.2,1,2,3)
        self.s2 = gc.Sphere(1.2,-1,-2,-3)
        self.s3 = gc.Sphere(1,0,0,0)

        # Create some input data
        self.testdata = [-1,0,"one"]

    # Test input numbers
    def test_inputerrors(self):
        for data in self.testdata[:-2]:
            with self.assertRaises(ValueError):
                c4  = gc.Circle(data,0,0)
                r4  = gc.Rectangle(data,data,0,0)
                cu4 = gc.Cube(data,0,0,0)
                s4  = gc.Sphere(data,0,0,0)
        data = self.testdata[2]
        with self.assertRaises(TypeError):
            c4  = gc.Circle(data,0,0)
            r4  = gc.Rectangle(1,data,data,0)
            cu4 = gc.Cube(1,0,data,0)
            s4  = gc.Sphere(1,0,0,data)

    # Test compute volume
    def test_compvolume(self):
        # Sphere volume
        volume1 = self.s1.compvolume()
        volume2 = 4/3 * np.pi * self.s1.radius**3
        self.assertEqual(volume1,volume2)
        # Cube volume
        volume1 = self.cu1.compvolume()
        volume2 = self.cu1.side**3
        self.assertEqual(volume1,volume2)

    # Test compute area
    def test_comparea(self):
        # Circle area
        area1 = self.c1.comparea()
        area2 = 2 * np.pi * self.c1.radius
        self.assertEqual(area1,area2)
        # Rectangle area
        area1 = self.r1.comparea()
        area2 = self.r1.rsize[0] * self.r1.rsize[1]
        self.assertEqual(area1,area2)
        # Sphere surface area
        area1 = self.s1.comparea()
        area2 = 4 * np.pi * self.s1.radius**2
        self.assertEqual(area1, area2)
        # Cube surface area
        area1 = self.cu1.comparea()
        area2 = self.cu1.side**2 * 6
        self.assertEqual(area1, area2)

    # Test circumferance
    def test_compcircum(self):
        # Circle circumferance
        circ1 = self.c1.circumferance()
        circ2 = np.pi*self.c1.radius**2
        self.assertEqual(circ1,circ2)
        # Rectangle circumferance
        circ1 = self.r1.circumferance()
        circ2 = 2*(self.r1.rsize[0]+self.r1.rsize[1])
        self.assertEqual(circ1,circ2)
    
    # Test move object
    def test_moveobj_2d(self):
        # Move circle (same method for rectangle)
        neworigin = [self.c1.origin[0]-1, self.c1.origin[1]-1]
        self.c1.moveobj_2d(-1,-1)
        self.assertEqual(self.c1.origin, neworigin)
        # Move sphere (same method for cube)
        neworigin = [self.s1.origin[0]-1, self.s1.origin[1]-1, self.s1.origin[2]-1]
        self.s1.moveobj_3d(-1,-1,-1)
        self.assertEqual(self.s1.origin, neworigin)

    # Test check if point is inside or outside
    def test_checkcoords(self):
        self.assertTrue(self.c1.checkcoords(0,0))
        self.assertTrue(self.r1.checkcoords(-3,0))
        self.assertTrue(self.cu1.checkcoords(1,2,3))
        self.assertTrue(self.s1.checkcoords(1,2,3))
        self.assertFalse(self.c1.checkcoords(0,-1))
        self.assertFalse(self.r1.checkcoords(-1,0))
        self.assertFalse(self.cu1.checkcoords(-1,0,-1))
        self.assertFalse(self.s1.checkcoords(-1,-1,0))

    # Test equality
    def test_equality(self):
        self.assertTrue(self.c1 == self.c2) # Circles with same area
        self.assertTrue(self.r1 == self.r2) # Rects with same area
        self.assertTrue(self.cu1 == self.cu2) # Cubes with same area
        self.assertTrue(self.s1 == self.s2) # Sphere with same area
        # Falses are combined with a message of what is false:
        self.assertFalse((self.c1 == self.c3)[0]) # Circles with different area
        self.assertFalse((self.r1 == self.r3)[0]) # Rects with different area
        self.assertFalse((self.cu1 == self.cu3)[0]) # Cubes with different area
        self.assertFalse((self.s1 == self.s3)[0]) # Sphere with different area
        self.assertFalse((self.c1 == self.r1)[0]) # Different geometry classes

if __name__ == "__main__":
    unittest.main()
