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

    # Остальные методы как в уроке 7