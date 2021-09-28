from vector import Vector
import unittest

#v1 = Vector(1,1)
#print(v1)

class TestVector(unittest.TestCase):

    # This is the setup from HERE -----------------

    # Setup will run, it will give x and y = 1 and 2
    # this is used in create 2d vec
    def setUp(self) -> None:
        self.x, self.y = 1, 2
    
    # here x,y=1,2 is put into a vector which is returned
    def create_2D_vec(self) -> "Vector":
        return Vector(self.x, self.y)
    
    # setup TO HERE -------------------------------

    # Testing starts HERE below -------------------
    # All tests must start with the word test_
    # When we run this it will look for all methods with 
    # test_ included in the method name


    # Start with testing different ways of creating vectors ------
    # 1
    def test_create_2D_vector(self) -> None:
        # Create a 2D vector with the method above, using the object we have
        v = self.create_2D_vec()
        # Now we check that the two arguments we put in are equal
        # ie v.numbers are the same as a tuple with x and y.
        # v.numbers uses the vector class, lists the elements of it as a tuple
        # and we compare it with a manually written tuple with the same numbers as
        # used to create the vector to begin with.
        self.assertEqual(v.numbers, (self.x, self.y))
    
    # 2
    def test_create_5D_vector(self) -> None:
        # Create 5D vector
        v = Vector(1,2,3,4,5)
        # Check that it's correct
        self.assertEqual(v.numbers, (1,2,3,4,5))

    # Test an empty vector - ie test error messages
    # We expect a ValueError (see line15 of vector.py)
    # 3
    def test_empty_vector(self):
        # We need to assert that we get the correct error
        # We expect a valueerror, if we get another error we Fail.
        with self.assertRaises(ValueError):
            v = Vector()

    # Test more error messages, invalid vector
    # 4
    def test_create_invalid_vector(self):
        with self.assertRaises(TypeError):
            v = Vector("1", "Two")
    

    # Test equality methods for vectors ---------------
    # line 83 of vector.py

    # Test if they are equal
    # 5
    def test_2_vector_equal(self):
        # Create two equal vectors
        v1 = self.create_2D_vec()
        v2 = Vector(1,2)
        # asserequal uses the __eq__ which is overloaded in Vector()
        self.assertEqual(v1,v2)

    # Test not equal
    # 6
    def test_2_vectors_not_equal(self):
        v1 = self.create_2D_vec()
        v2 = Vector(-1,2)
        self.assertNotEqual(v1, v2)

    # 7
    def test_2_vectors_not_equal_diffdim(self):
        v1 = self.create_2D_vec()
        v2 = Vector(1,2,3)
        with self.assertRaises(TypeError):
            v1 == v2


# To run the tests
if __name__ == "__main__":
    unittest.main()
