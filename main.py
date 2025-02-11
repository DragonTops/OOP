import random

class Unit:
    count = 0
    def __init__(self, team):
        Unit.count += 1
        self.id = Unit.count
        self.team = team

class Hero(Unit):
    def __init__(self, team):
        super().__init__(team)
        self.level = 1

    def level_up(self):
        self.level += 1

class Soldier(Unit):
    def follow(self, hero):
        print(f"Солдат {self.id} следует за героем {hero.id}")

hero1 = Hero(1)
hero2 = Hero(2)
team1 = []
team2 = []

for _ in range(10):
    soldier = Soldier(random.choice([1, 2]))
    if soldier.team == 1:
        team1.append(soldier)
    else:
        team2.append(soldier)

if len(team1) > len(team2):
    hero1.level_up()
else:
    hero2.level_up()

if team1:
    team1[0].follow(hero1)
    print(f"ID солдата: {team1[0].id}, ID героя: {hero1.id}")
