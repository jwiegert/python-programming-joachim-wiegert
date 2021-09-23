class OldCoinstash:
    def __init__(self, owner) -> None: # -> None is a "HINT" to users that this returns nothing
        # This is public
        self.owner = owner
        # Make these private, one convention: with underscore prefix.
        self._riksdaler = 0
        self._skilling  = 0
        # A second method is with name-mangling (comes another time)
    # We can define these functions here so that it's possible to change the values
    # We change them with the variables riksdaler and skilling, without underscore
    # The underscoure simply makes the class-contents "hidden" since no one would
    # use underscore when they write outside the code :P
    #
    # 1. Deposit function
    def deposit(self, riksdaler: float, skilling: float) -> None:
        if riksdaler <= 0 or skilling <= 0:
            raise ValueError(f"Stop depositing negative values. {riksdaler} riksdaler or {skilling} skilling are not OK")
        # So we can change these attributes INSIDE the class
        self._riksdaler += riksdaler
        self._skilling  += skilling
    # 2. withdrawal function
    def withdraw(self, riksdaler: float, skilling: float) -> None:
        if riksdaler > self._riksdaler or skilling > self._skilling:
            raise ValueError("You can't withdraw more coins than you have")
        self._riksdaler -= riksdaler
        self._skilling  -= skilling
    # 3. Check balance function
    def checkbalance(self) -> str:
        return f"Coins in stash: {self._riksdaler} riksdaler and {self._skilling} skilling."
    # 4. And define a standard respons on call of this class
    def __repr__(self) -> str: # -> str is a HINT that this returns a string, this is good practice.
        return f"OldCoindstash(owner='{self.owner}')"
