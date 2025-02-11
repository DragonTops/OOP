from room import Room

# Ввод данных
length = float(input("Введите длину комнаты (м): "))
width = float(input("Введите ширину комнаты (м): "))
height = float(input("Введите высоту комнаты (м): "))

room = Room(length, width, height)

# Добавление окон/дверей
while True:
    choice = input("Добавить окно/дверь? (да/нет): ").lower()
    if choice != 'да':
        break
    w = float(input("Ширина окна/двери (м): "))
    h = float(input("Высота окна/двери (м): "))
    room.add_window(w, h)

# Расчет обоев
roll_length = float(input("Длина одного рулона (м): "))
roll_width = float(input("Ширина одного рулона (м): "))

print("\nРезультаты:")
print(f"Площадь для оклейки: {room.work_area():.2f} м²")
print(f"Требуется рулонов: {room.rolls_needed(roll_length, roll_width)}")