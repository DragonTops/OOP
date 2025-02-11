import math

class WinDoor:
    def __init__(self, width, height):
        self.area = width * height

class Room:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.windows = []

    def add_window(self, w, h):
        self.windows.append(WinDoor(w, h))

    def total_wall_area(self):
        return 2 * self.height * (self.length + self.width)

    def work_area(self):
        total = self.total_wall_area()
        for window in self.windows:
            total -= window.area
        return total

    def rolls_needed(self, roll_length, roll_width):
        return math.ceil(self.work_area() / (roll_length * roll_width))