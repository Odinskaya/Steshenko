#Вариант 1
class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self.power = 10
        self.agility = 10
        self.intellect = 10

    def therapy(self):
        if self.health < 100:
            self.health += 10


class Mage(Unit):
    def __init__(self, name, clan, air, fire, water):
        super().__init__(name, clan)
        self.air = air
        self.fire = fire
        self.water = water

    def augment(self):
        if self.intellect < 10:
            self.intellect += 1


class Archer(Unit):
    def __init__(self, name, clan, bow, crossbow):
        super().__init__(name, clan)
        self.bow = bow
        self.crossbow = crossbow

    def augment(self):
        if self.agility < 10:
            self.agility += 1


class Knight(Unit):
    def __init__(self, name, clan, sword, axe, pike):
        super().__init__(self, name)
        self.sword = sword
        self.axe = axe
        self.pike = pike

    def augment(self):
        if self.power < 10:
            self.power += 1

#Вариант 2

class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.max_health = 100
        self.min_health = 0
        self.max_strength = 10
        self.min_strength = 0
        self.max_agility = 10
        self.min_agility = 0
        self.max_intelligence = 10
        self.min_intelligence = 0

    def read_unit(self):
        read = self.name + " " + self.clan
        return read.title()

    def read_health(self):
        if self.min_health + 10 > self.max_health:
            self.max_health = 100
        else:
            self.min_intelligence += 10

    def health_read(self):
        print("У персонажа: " + str.read_health + " hp")


class Mage(Unit):
    def __init__(self, name, clan, air, fire, water):
        super().__init__(name, clan, air, fire, water)

    def intelligence_mage(self):
        if self.min_intelligence + 1 < self.max_intelligence:
            self.max_intelligence = 10
        else:
            self.min_intelligence += 10


class Archer(Unit):
    def __init__(self, name, clan, bow, crossbow):
        super().__init__(name, clan, bow, crossbow)

    def agility_archer(self):
        if self.min_agility + 1 < self.max_agility:
            self.max_agility = 10
        else:
            self.min_agility += 10


class Knight(Unit):
    def __init__(self, name, clan, sword, axe, pike):
        super().__init__(self, name, clan, sword, axe, pike)

    def agility_knight(self):
        if self.min_strengthx + 1 < self.max_strength:
            self.max_strength = 10
        else:
            self.min_strength += 10


Eridan = Mage("Eridan", "Fresh", "fire")
print(Eridan.read_unit())
print(Eridan.intelligence_mage)
Eridan.health_read()

Erifan = Mage("Erifan", "Dradon", "water")
print(Erifan.read_unit())
print(Erifan.intelligence_mage)
Erifan.health_read()

Eren = Knight("Eren", "Fresh", "pike")
print(Eren.read_unit())
print(Eren.agility_knight)
Eren.health_read()

Selfi = Archer("Selfi", "Archer_best", "crossbow")
print(Selfi.read_unit())
print(Selfi.agility_archer)
Selfi.health_read()

Antalia = Mage("Antalia", "Fresh", "air")
print(Antalia.read_unit())
print(Antalia.intelligence_mage)
Antalia.health_read()

Enifar = Archer("Enifar", "Archer_best", "bow")
print(Enifar.read_unit())
print(Enifar.agility_archer)
Enifar.health_read()





