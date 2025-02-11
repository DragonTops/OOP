class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    def __str__(self):
        return f"Прямоугольник: {self.width}x{self.height}"

rect1 = Rectangle(2, 3)
rect2 = Rectangle(4, 5)
result = rect1 + rect2
print(result)  # Прямоугольник: 6x8