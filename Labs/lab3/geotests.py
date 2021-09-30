import geometryclasses as gc
import unittest
import numpy as np

class TestGeometry(unittest.TestCase):

    # ---------- Setup ----------
    def setUp(self) -> None:
        # Create a few standard objects
        self.c1 = gc.Circle(2,1,1)
        self.c2 = gc.Circle(1,-1,0)
        self.c3 = gc.Circle(2,-1,-1)
        self.r1 = gc.Rectangle(1,2,-3,0)
        self.r2 = gc.Rectangle(2,1,3,0)
        self.r3 = gc.Rectangle(0.7,0.3,0,3)
        # Create some input data
        self.testdata = [-1,0,"one"]

    # ---------- Tests ----------

    # Test input numbers
    def test_inputerrors(self):
        for data in self.testdata[:-2]:
            with self.assertRaises(ValueError):
                c4 = gc.Circle(data,0,0)
            # TODO test different positions of testdata in rectangle and circle
            # and test TypError.
    
    # Test compute area and circumferance
    def test_comparea(self):
        area1 = self.c1.comparea()
        area2 = 2*np.pi*self.c1.radius
        self.assertEqual(area1,area2)
        area1 = self.r1.comparea()
        area2 = self.r1.rsize[0]*self.r1.rsize[1]
        self.assertEqual(area1,area2)
    
    # Test circumferance
    def test_compcircum(self):
        circ1 = self.c1.circumferance()
        circ2 = np.pi*self.c1.radius**2
        self.assertEqual(circ1,circ2)
        circ1 = self.r1.circumferance()
        circ2 = 2*(self.r1.rsize[0]+self.r1.rsize[1])
        self.assertEqual(circ1,circ2)
    
    # Test move object
    def test_moveobj(self):
        neworigin = [self.c1._origin[0]-1,self.c1._origin[1]-1]
        self.c1.moveobj(-1,-1)
        self.assertEqual(self.c1._origin, neworigin)

    # Test check if point is inside or outside
    def test_checkcoords(self):
        self.assertTrue(self.c1.checkcoords(0,0))
        self.assertTrue(self.r1.checkcoords(-3,0))
        self.assertFalse(self.c1.checkcoords(0,-1))
        self.assertFalse(self.r1.checkcoords(-1,0))


        


if __name__ == "__main__":
    unittest.main()

# Things to tests
# - check input numbers, type and valuerror
# - compute area, compute circumferance
# - move object
# - check point inside/outside
# - check equality
# - check repr
# - check plot?
