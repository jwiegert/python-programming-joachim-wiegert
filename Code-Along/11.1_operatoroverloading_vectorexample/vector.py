# A few vector operators
from typing import Tuple


class Vector:
    # A Doc-string:
    """A class to represent Euclidian vector with magnitude and direction"""

    # In our init we don't know the number of dimensions of our vectors.
    # So we don't know the number of numbers here, why we add a *
    # numbers will be a tuple
    def __init__(self, *numbers) -> None:
                
        # Do some error check
        for number in numbers:
            if not isinstance(number, (float, int)):
                raise TypeError(f"{number} must be a float or an int, not {type(number)}")
        
        if len(numbers) <= 0:
            raise ValueError("Vectors can't be empty")
        
        # Then we can add in our numbers to self.number.
        # We do that in a tuple. We must write tuple() here otherwise we get a generator!
        # Remember that Boolians becomes 1s and 0s here.
        # We make this private so that we don't need a setter for this after the getter below.
        self._numbers = tuple(float(number) for number in numbers)
    
    @property
    def numbers(self) -> tuple:
        # Private, but don't need a setter since we set it in the tuple-comprehension above.
        return self._numbers
    
    # Here we now add our methods with vector operations
    # We will overload the normal operators here!
    # self is not necessary here but we use it to show other developers that this is a method
    # So now we have both self and other.
    def __add__(self, other: "Vector") -> "Vector":
        if self.validatevectors(other): # Makes the error check below.
            numbers = (a+b for a,b in zip(self.numbers, other.numbers))
            # Return a vector of our style with these numbers
            # * unpacks the numbers into the Vetor class
            return Vector(*numbers)

    # To check lengths of our vectors we overload the len() function also
    def __len__(self) -> int:
        """Returns number of elements in a vector, not the Euclidian length"""
        return len(self.numbers)

    # We check if vectors are the same dimensions before operating on them
    def validatevectors(self, other: "Vector") -> bool:
        """ Validate that two vectors have same dimensions"""
        if not isinstance(other, Vector) or len(other) != len(self):
            raise TypeError("Both variables must be vectors with same length")
        return len(self) == len(other)
    
    # Standard returner of info. print(vectorname) but the def __str__ overrides this.
    def __repr__(self) -> str:
        return f"Vector{self.numbers}"
    
    # And returner of just the numbers. print(vectorname)
    def __str__(self) -> str:
        return f"{self.numbers}"
    
    # This will make v[n] work for our new type of data
    def __getitem__(self, item: int) -> float:
        return self.numbers[item]
  



