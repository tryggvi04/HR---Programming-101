class Height:
    ''' Class that models height in feet and inches. '''

    def __init__(self, feet, inches) -> None:
        """Initializes an instance of a height."""

        self.feet = feet
        self.inches = inches
        while self.inches >= 12: # One foot is 12 inches so we convert inches to feet if its applicable.
            self.feet += 1
            self.inches -= 12
        self.calculated_cm = self.cm()
    
    def cm(self):
        self.calculated_cm = 0
        self.calculated_cm += 30.48 * self.feet
        self.calculated_cm += 2.54 * self.inches
        self.calculated_cm = round(self.calculated_cm, 0)
        return int(self.calculated_cm)

    def __add__(self, other: "Height") -> "Height":
        feet = self.feet + other.feet
        inches = self.inches + other.inches
        while inches >= 12: # One foot is 12 inches so we convert inches to feet if its applicable.
            feet += 1
            inches -= 12
        return Height(feet, inches)
    
    def __gt__(self, other: "Height") -> "Height":
        if self.feet > other.feet:
            return True
        elif self.feet == other.feet:
            if self.inches > other.inches:
                return True
        return False
    
    def __repr__(self) -> str:
        """Returns a parsable string representation of the Height."""
        return "{} ft, {} in".format(self.feet, self.inches)
    
    def __str__(self, cm_check=0) -> str:
        if cm_check == "cm":
            return "{} cm".format(self.calculated_cm)
        else:
            return "{} ft, {} in".format(self.feet, self.inches)


