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
        return f"{round(self.x, 1)}, {round(self.y, 1)}"

    def unit_vector(self):
        magnitude = math.sqrt((self.x*self.x) + (self.y*self.y))
        if magnitude == 0:
            return Vector(0, 0)
        return Vector(self.x/magnitude, self.y/magnitude)

    def negative_vector(self):
        return Vector(-self.x, -self.y)