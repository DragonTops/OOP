class WinDoor:
    """Класс для представления окна или двери."""
    def __init__(self, width, height):
        self.area = width * height  # Площадь окна/двери


class Room:
    """Класс для расчета площади комнаты и необходимых обоев."""
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.windows = []

    def add_window(self, width, height):
        """Добавить окно/дверь в комнату."""
        self.windows.append(WinDoor(width, height))

    def total_wall_area(self):
        """Общая площадь стен (без учета окон/дверей)."""
        return 2 * self.height * (self.length + self.width)

    def work_area(self):
        """Площадь для оклейки (с учетом окон/дверей)."""
        total_area = self.total_wall_area()
        for window in self.windows:
            total_area -= window.area
        return total_area

    def rolls_needed(self, roll_length, roll_width):
        """Рассчитать количество рулонов обоев."""
        from math import ceil
        return ceil(self.work_area() / (roll_length * roll_width))