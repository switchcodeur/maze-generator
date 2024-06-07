class Vector2:
    def __init__(self, X, Y):
        self.X, self.Y = self.position = X, Y

    def calculate(self, other, operator: str):
        if isinstance(other, Vector2):
            return Vector2(eval(f"{other.X}{operator}{self.X}"), eval(f"{other.Y}{operator}{self.Y}"))

        return Vector2(eval(f"{other}{operator}{self.X}"), eval(f"{other}{operator}{self.Y}"))

    def __add__(self, other):
        return self.calculate(other, "+")

    def __sub__(self, other):
        return self.calculate(other, "-")

    def __mul__(self, other):
        return self.calculate(other, "*")

    def __truediv__(self, other):
        return self.calculate(other, "/")