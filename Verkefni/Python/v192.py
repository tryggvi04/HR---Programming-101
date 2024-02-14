class ComplexNumber:
    def __init__(self, real_part=0, imaginary_part=0):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __str__(self):
        if self.imaginary_part == 0:
            return "{}".format(self.real_part)
        elif self.real_part == 0:
            return "{}i".format(self.imaginary_part)
        elif self.imaginary_part < 0:
            return "{} - {}i".format(self.real_part, (self.imaginary_part*-1))
        else:
            return "{} + {}i".format(self.real_part, self.imaginary_part)

    def __repr__(self) -> str:
        return "ComplexNumber({}, {})".format(self.real_part, self.imaginary_part)

    def re(self) -> float:
        return self.real_part

    def im(self) -> float:
        return self.imaginary_part

    def __eq__(self, other: "ComplexNumber") -> bool:
        if self.re() == other.re() and self.im() == other.im():
            return True
        else:
            return False

    def conjugate(self) -> "ComplexNumber":
        return ComplexNumber(self.re(), -self.im())

    def __neg__(self) -> "ComplexNumber":
        return ComplexNumber(-self.real_part, -self.imaginary_part)
    def __add__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber((self.re() + other.re()), self.im() + other.im())

    def __sub__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber((self.re() - other.re()), self.im() - other.im())

    def __mul__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber((self.re() * other.re() - self.im() * other.im()), (self.re() * other.im() + self.im() * other.re()))

    def inverse(self) -> "ComplexNumber":
        real = self.re()/(self.re() ** 2 + self.im() ** 2)
        imagin = self.im()/(self.re() ** 2 + self.im() ** 2)
        return ComplexNumber(real, -imagin)
        

    def __truediv__(self, other: "ComplexNumber") -> "ComplexNumber":
        real = (self.re() * other.re() + self.im() * other.im())/(other.re() ** 2 + other.im() ** 2)
        imag = (self.im() * other.re() - self.re() * other.im())/(other.re() ** 2 + other.im() ** 2)
        return ComplexNumber(real, imag)
