class SecureData:
    def __init__(self):
        self.__value = 0

    def get_value(self):
        return self.__value

    def set_value(self, value):
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")
        self.__value = value

data = SecureData()
data.set_value(10)
print(data.get_value())  # 10
# data.set_value(-5)  # Ошибка