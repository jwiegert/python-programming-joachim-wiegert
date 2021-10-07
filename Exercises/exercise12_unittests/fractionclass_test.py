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
    def test_errors(self):
        with self.assertRaises(TypeError):
            f1 = Frac("one","two")
        with self.assertRaises(TypeError):
            f1 = Frac(1.2,1.3)

    # 2. test simplify and mixed
    def test_mixed(self):
        f1 = self.createfrac()
        # Check simplify
        self.assertEqual(f1.simplify()[0]/f1.simplify()[1] , self.nom/self.denom)
        # Check mixed, we need to extract the different components
        # From the "nice" outputs
        c1 = float(f1.mixed().replace("+", "").split("  ")[0])
        c2 = float(f1.mixed().replace("+", "").split("  ")[1].split("/")[0])
        c3 = float(f1.mixed().replace("+", "").split("  ")[1].split("/")[1])
        self.assertEqual(c1+c2/c3, self.nom/self.denom)

    # 3. negative nom, negative denom, negative both
    def test_negatives(self):
        f1 = Frac(-1,2)
        f1.simplify()
        self.assertEqual(f1.nominator/f1.denominator, -1/2)
        f1 = Frac(1,-2)
        f1.simplify()
        self.assertEqual(f1.nominator/f1.denominator, 1/-2)
        f1 = Frac(-1,-2)
        f1.simplify()
        self.assertEqual(f1.nominator/f1.denominator, -1/-2)

    # 4. addition with frac and int, and with +=
    def test_addition(self):
        # Addition with int
        f1 = self.createfrac()
        f2 = f1 + Frac(1)
        self.assertEqual(f2.nominator/f2.denominator, 3/2+1)

        # Addition with frac
        f1 = self.createfrac()
        f2 = f1 + Frac(3,4)
        self.assertEqual(f2.nominator/f2.denominator, 3/2+3/4)

        # Addition with +=
        f1 = self.createfrac()
        f1 += Frac(2)
        self.assertEqual(f1.nominator/f1.denominator, 3/2+2)

    # 5. subtraction with frac and int
    def test_subtraction(self):
        # Subtraction with int
        f1 = self.createfrac()
        f2 = f1 - Frac(1)
        self.assertEqual(f2.nominator/f2.denominator, 3/2-1)

        # Subtraction with frac
        f1 = self.createfrac()
        f2 = f1 - Frac(3,4)
        self.assertEqual(f2.nominator/f2.denominator, 3/2-3/4)

        # Subtraction with -=
        f1 = self.createfrac()
        f1 -= Frac(2)
        self.assertEqual(f1.nominator/f1.denominator, 3/2-2)
    
    # 6. multiply with frac and int
    def test_multiply(self):
        # Multiply with int
        f1 = self.createfrac()
        f2 = f1 * Frac(2)
        self.assertEqual(f2.nominator/f2.denominator, 3/2*2)
        # Multiply with int - communicative
        f1 = self.createfrac()
        f2 = Frac(2) * f1
        self.assertEqual(f2.nominator/f2.denominator, 2*3/2)

        # Multiply with frac
        f1 = self.createfrac()
        f2 = f1 * Frac(2,3)
        self.assertEqual(f2.nominator/f2.denominator, 3/2*2/3)
        # Multiply with frac - communicative
        f1 = self.createfrac()
        f2 = Frac(2,3) * f1
        self.assertEqual(f2.nominator/f2.denominator, 2/3*3/2)
    
    # 7 division with frac and int
    def test_divide(self):
        # Divide with int
        f1 = self.createfrac()
        f2 = f1 / Frac(2)
        self.assertEqual(f2.nominator/f2.denominator, (3/2) / 2)
        # Divide with int - communicative
        f1 = self.createfrac()
        f2 = Frac(2) / f1
        self.assertEqual(f2.nominator/f2.denominator, 2 / (3/2))

        # Divide with frac
        f1 = self.createfrac()
        f2 = f1 / Frac(2,3)
        self.assertEqual(f2.nominator/f2.denominator, (3/2) / (2/3))
        # Divide with frac - communicative
        f1 = self.createfrac()
        f2 = Frac(2,3) / f1
        self.assertEqual(f2.nominator/f2.denominator, (2/3) / (3/2))
    
    # 8. equality of two fracs
    def test_equality(self):
        f1 = self.createfrac()
        f2 = self.createfrac()
        f3 = Frac(5)
        f1.simplify()
        self.assertTrue(f1 == f2)
        self.assertFalse(f1 == f3)

if __name__ == "__main__":
    unittest.main()
