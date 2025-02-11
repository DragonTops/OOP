class Pupil:
    def __init__(self):
        self.knowledge = []

    def take(self, info):
        self.knowledge.append(info)

    def forget(self):
        import random
        if self.knowledge:
            index = random.randint(0, len(self.knowledge)-1)
            del self.knowledge[index]

pupil = Pupil()
pupil.take("Python")
pupil.take("ООП")
pupil.forget()
print(pupil.knowledge)  # Например: ['Python']