from shape import Shape

class Rectangle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_area(self):
        return self.x * self.y
    
    def get_perimeter(self):
        return self.x * 2 + self.y * 2
