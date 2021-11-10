import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        return Vector(self.x - v.x, self.y - v.y)

    def __mul__(self, v):
        if isinstance(v, float) or isinstance(v, int):
            return Vector(self.x * v, self.y * v)
        return Vector(self.x*v.x, self.y*v.y)

    def __truediv__(self, v):
        return Vector(self.x / v, self.y / v)

    def __str__(self) -> str:
        i = f"+{round(self.x, 3)}" if self.x >= 0 else round(self.x, 3)
        j = f"+{round(self.y, 3)}" if self.y >= 0 else round(self.y, 3)
        return f"{i}i, {j}j"

    def unit_vector(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            return Vector(0, 0)
        return Vector(self.x/magnitude, self.y/magnitude)

    def negative_vector(self):
        return Vector(-self.x, -self.y)

    def round(self):
        self.x = round(self.x, 2)
        self.y = round(self.y, 2)

    def magnitude(self):
        return math.sqrt((self.x*self.x) + (self.y*self.y))