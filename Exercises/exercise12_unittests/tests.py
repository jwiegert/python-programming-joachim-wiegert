from fractionclass import Frac
import unittest

class TestFrac(unittest.TestCase):
    # Setup:
    def setUp(self) -> None:
        self.nom, self.denom = 30, 20
    
    def createfrac(self) -> "Frac":
        return Frac(self.nom, self.denom)

    # Tests:
    # can use asssertEqual for most of these

    # 1. error messages


    # 2. test simplify and mixed
    def test_mixed(self):
        f1 = self.createfrac()
        # Check simplify
        self.assertEqual(f1.simplify()[0]/f1.simplify()[1] , self.nom/self.denom)
        # Check mixed, we need to extract the different components
        c1 = float(f1.mixed().replace("+", "").split("  ")[0])
        c2 = float(f1.mixed().replace("+", "").split("  ")[1].split("/")[0])
        c3 = float(f1.mixed().replace("+", "").split("  ")[1].split("/")[1])
        self.assertEqual(c1+c2/c3, self.nom/self.denom)

    # 3. negative nom, negative denom, negative both
    def test_negatives(self):
        f1 = Frac(-1,2)
        self.assertEqual(f1.simplify()[0]/f1.simplify()[1], -1/2)
        f1 = Frac(1,-2)
        self.assertEqual(f1.simplify()[0]/f1.simplify()[1], 1/-2)
        f1 = Frac(-1,-2)
        self.assertEqual(f1.simplify()[0]/f1.simplify()[1], -1/-2)

    # 4. addition with frac and int, and with +=
    def test_addition(self):
        # Addition with int
        f1 = self.createfrac()
        f2 = f1 + Frac(1)
        fn = float(f2.split("/")[0])
        fd = float(f2.split("/")[1])
        self.assertEqual(fn/fd, 3/2+1)

        # Addition with frac
        f1 = self.createfrac()
        f2 = f1 + Frac(3,4)
        fn = float(f2.split("/")[0])
        fd = float(f2.split("/")[1])
        self.assertEqual(fn/fd, 3/2+3/4)

        # Addition with +=
        f1 = self.createfrac()
        f1 += Frac(2)
        fn = float(f1.split("/")[0])
        fd = float(f1.split("/")[1])
        self.assertEqual(fn/fd, 3/2+2)

    # 5. subtraction with frac and int
    def test_subtraction(self):
        # Subtraction with int
        f1 = self.createfrac()
        f2 = f1 - Frac(1)
        fn = float(f2.split("/")[0])
        fd = float(f2.split("/")[1])
        self.assertEqual(fn/fd, 3/2-1)

        # Subtraction with frac
        f1 = self.createfrac()
        f2 = f1 - Frac(3,4)
        fn = float(f2.split("/")[0])
        fd = float(f2.split("/")[1])
        self.assertEqual(fn/fd, 3/2-3/4)

        # Subtraction with -=
        f1 = self.createfrac()
        f1 -= Frac(2)
        fn = float(f1.split("/")[0])
        fd = float(f1.split("/")[1])
        self.assertEqual(fn/fd, 3/2-2)
    
    # 6. multiply with frac and int

    # division with frac and int

    # equality of two fracs



    # 



    pass

if __name__ == "__main__":
    unittest.main()
