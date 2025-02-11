import math

"""Модуль для расчета площади обрабатываемой поверхности и количества рулонов обоев."""

class WinDoor:
    """Класс для представления окон и дверей, которые не оклеиваются обоями."""
    def __init__(self, width, height):
        """Конструктор принимает ширину и высоту окна/двери."""
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными числами.")
        self.square = width * height


class Room:
    """Класс для расчета площади стен комнаты и необходимых обоев."""
    def __init__(self, length, width, height):
        """Конструктор принимает длину, ширину и высоту комнаты."""
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Размеры комнаты должны быть положительными числами.")
        self.length = length
        self.width = width
        self.height = height
        self.windows = []

    def add_wd(self, width, height):
        """Добавляет окно/дверь в список неоклеиваемых поверхностей."""
        self.windows.append(WinDoor(width, height))

    def full_surface(self):
        """Рассчитывает общую площадь стен без учета окон/дверей."""
        return 2 * self.height * (self.length + self.width)

    def work_surface(self):
        """Рассчитывает площадь для оклейки с учетом вычетов окон/дверей."""
        total_area = self.full_surface()
        for window in self.windows:
            total_area -= window.square
        return total_area

    def wallpapers_needed(self, roll_length, roll_width):
        """Возвращает количество рулонов с округлением вверх."""
        if roll_length <= 0 or roll_width <= 0:
            raise ValueError("Размеры рулона должны быть положительными.")
        return math.ceil(self.work_surface() / (roll_length * roll_width))