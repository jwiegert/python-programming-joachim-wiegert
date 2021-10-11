class Frac:
    def __init__(self, nominator: int, denominator: int = None) -> None:
        self.nominator   = nominator
        self.denominator = denominator
    
    # Getters
    @property
    def nominator(self) -> int:
        return self._nom
    @property
    def denominator(self) -> int:
        return self._denom
    # Setters and error checks
    @nominator.setter
    def nominator(self, value: int) -> None:
        if Frac.validateinput(value):
            self._nom = value
    @denominator.setter
    def denominator(self, value: int) -> None:
        if value == None:
            value = 1
            self._denom = value
        elif Frac.validateinput(value):
            self._denom = value

    # addition
    def __add__(self ,other: "Frac") -> str:
        """Adds together two fractions"""
        # Find least fitting denominator
        newnom   = self._nom*other._denom + other._nom*self._denom
        newdenom = self._denom*other._denom
        # Create new fraction object and shorten it
        newfrac = Frac(newnom,newdenom)
        newfrac.simplify()
        return newfrac

    # subtraction
    def __sub__(self, other: "Frac") -> str:
        """Subtracts two fractions, self and other"""
        # Find least fitting denominator
        newnom   = self._nom*other._denom - other._nom*self._denom
        newdenom = self._denom*other._denom
        # Create new fraction object
        newfrac = Frac(newnom,newdenom)
        # Shorten the fraction
        newfrac.simplify()
        return newfrac

    # multiplication
    def __mul__(self, other: "Frac") -> str:
        """method to multiply two fraction"""
        newnom   = self._nom * other._nom
        newdenom = self._denom * other._denom
        # Create new fraction object
        newfrac = Frac(newnom,newdenom)
        # Shorten the fraction
        newfrac.simplify()
        return newfrac

    # division
    def __truediv__(self, other: "Frac") -> str:
        newnom   = self._nom * other._denom
        newdenom = self._denom * other._nom
        # Create new fraction object
        newfrac = Frac(newnom,newdenom)
        # Shorten the fraction
        newfrac.simplify()
        return newfrac

    # Equality
    def __eq__(self, other: "Frac") -> bool:
        if self._nom/self._denom == other._nom/other._denom:
            return True
        else:
            return False

    # Simplify method
    def simplify(self) -> int:
        """To shorten fraction to least denominator"""
        # If both are negative, remove the minuses
        if self._nom < 0 and self._denom < 0:
            self._nom = abs(self._nom)
            self._denom = abs(self._denom)
        # From https://stackoverflow.com/questions/64931411/how-to-simplify-a-fraction-in-python
        # Though I added abs in the while statement so that it works for negative numbers.
        nn = 2
        while nn < min(abs(self._nom), abs(self._denom)) + 1:
            if self._nom % nn == 0 and self._denom % nn == 0:
                self._nom = self._nom // nn
                self._denom = self._denom // nn
            else:
                nn += 1
        return self._nom,self._denom

    # Print nicely-function
    def mixed(self) -> str:
        """Used to print results nicely"""
        if self._nom%self._denom == 0:
            return f"{self._nom//self._denom}"
        else:
            if abs(self._nom)/abs(self._denom) > 1:
                return f"{self._nom//self._denom} + {int(self._nom - self._nom//self._denom*self._denom)}/{self._denom}"
            else:
                return f"{self._nom}/{self._denom}"

    # Error handling
    @staticmethod
    def validateinput(value:int) -> bool:
        """Method to check input values"""
        if not isinstance(value, int):
            raise TypeError(f"Value {value} must be an int, not {type(value)}")
        return True

    # Normal return of this class
    def __str__(self) -> str:
        return f"{self._nom}/{self._denom}"

    # Main return of this class
    def __repr__(self) -> str:
        return f"{self.nominator}/{self.denominator}"
