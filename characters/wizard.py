from characters.character import Character

class Spell:
    def __init__(self, name, damage, mana):
        self.name = name
        self.damage = damage
        self.mana = mana

class Wizard(Character):
    def __init__(self, name, hp, weapon, armor, mana, spells):
        super().__init__(name, hp, weapon, armor)
        self.mana = mana
        self.spells = spells

    def attack(self, target):
        print(self.name, "(Wizard) uses weapon!")
        super().attack(target)