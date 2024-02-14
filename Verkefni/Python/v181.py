
class Vector:
    def __init__(self, x=0, y=0, z=0) -> None:
        self.vector_t = [x, y, z]
        

    def __str__(self) -> str:
        return "[[ {} {} {} ]]".format(self.vector_t[0], self.vector_t[1], self.vector_t[2])

    def __abs__(self) -> float:
        return (self.vector_t[0] ** 2 + self.vector_t[1] ** 2 + self.vector_t[2] ** 2) ** 0.5

    def __add__(self, other: "Vector") -> "Vector":
        x = self.vector_t[0] + other.vector_t[0]
        y = self.vector_t[1] + other.vector_t[1]
        z = self.vector_t[2] + other.vector_t[2]
        return Vector(x, y, z)

    def __sub__(self, other: "Vector") -> "Vector":
        x = self.vector_t[0] - other.vector_t[0]
        y = self.vector_t[1] - other.vector_t[1]
        z = self.vector_t[2] - other.vector_t[2]
        return Vector(x, y, z)

    def __eq__(self, other: "Vector") -> bool:
        subvect = self - other
        if abs(subvect) <= 0.0000001:
            return True
        return False

    def __mul__(self, scalar: float) -> "Vector":
        return_value = []
        for num in self.vector_t:
            return_value.append((num*scalar))
        return Vector(return_value[0], return_value[1], return_value[2])

    def __rmul__(self, scalar: float) -> "Vector":
        return (self*scalar)

    def __repr__(self) -> str:
        """Returns a parsable string representation of the Vector. """
        return "Vector({}, {}, {})".format(self.vector_t[0], self.vector_t[1], self.vector_t[2])


    def __gt__(self, other: "Vector") -> bool:
        if abs(self) > abs(other):
            return True
        else:
            return False

    def __ge__(self, other: "Vector") -> bool:
        if abs(self) >= abs(other):
            return True
        else:
            return False

    def __lt__(self, other: "Vector") -> bool:
        if abs(self) < abs(other):
            return True
        else:
            return False

    def __le__(self, other: "Vector") -> bool:
        if abs(self) <= abs(other):
            return True
        else:
            return False

    def dot(self, other: "Vector") -> float:
        return_value = 0
        for item1, item2 in zip(self.vector_t, other.vector_t):
            return_value += item1*item2
        return return_value

    def cross(self, other: "Vector") -> "Vector":
        x = (self.vector_t[1] * other.vector_t[2]) - (self.vector_t[2] * other.vector_t[1])
        y = (self.vector_t[2] * other.vector_t[0]) - (self.vector_t[0] * other.vector_t[2])
        z = (self.vector_t[0] * other.vector_t[1]) - (self.vector_t[1] * other.vector_t[0])
        return Vector(x, y, z)
