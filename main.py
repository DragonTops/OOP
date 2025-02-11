import random

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, enemy):
        enemy.health -= 20
        print(f"{self.name} атаковал {enemy.name}. У {enemy.name} осталось {enemy.health} здоровья.")

warrior1 = Warrior("Воин 1")
warrior2 = Warrior("Воин 2")

while warrior1.health > 0 and warrior2.health > 0:
    attacker, defender = random.choice([(warrior1, warrior2), (warrior2, warrior1)])
    attacker.attack(defender)
    if defender.health <= 0:
        print(f"{defender.name} побежден! Победитель: {attacker.name}")
        break