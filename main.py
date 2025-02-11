class Snow:
    def __init__(self, qty):
        self.qty = qty

    def __add__(self, n):
        return Snow(self.qty + n)

    def __sub__(self, n):
        return Snow(self.qty - n)

    def __mul__(self, n):
        return Snow(self.qty * n)

    def __truediv__(self, n):
        return Snow(round(self.qty / n))

    def __call__(self, new_qty):
        self.qty = new_qty

    def make_snow(self, per_row):
        rows = self.qty // per_row
        remainder = self.qty % per_row
        return ('*' * per_row + '\n') * rows + ('*' * remainder if remainder else '')

snow = Snow(15)
snow + 5
print(snow.make_snow(5))  # *****\n*****\n*****