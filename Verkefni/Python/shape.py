class Shape:
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
        return "{} with area of {:.2f} and perimeter of {:.2f}".format(type(self).__name__, self.get_area(), self.get_perimeter())