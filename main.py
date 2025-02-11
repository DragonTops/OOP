class Person:
    def __init__(self, name, surname, qualification=1):
        self.name = name
        self.surname = surname
        self.qualification = qualification

    def __del__(self):
        print(f"До свидания, мистер {self.name} {self.surname}")

    def info(self):
        return f"{self.surname} {self.name}, квалификация: {self.qualification}"

person1 = Person("Иван", "Иванов", 3)
person2 = Person("Петр", "Петров", 1)
person3 = Person("Сидор", "Сидоров", 2)

staff = [person1, person2, person3]
print([p.info() for p in staff])

# Удаляем сотрудника с минимальной квалификацией
del staff
del person2

input("Нажмите Enter для выхода...")