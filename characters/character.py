class Character:
    def __init__(self, name, hp, weapon, armor):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor

    def attack(self, target):
        damage = self.weapon.damage - target.armor.defense
        if damage < 0:
            damage = 0
        target.hp -= damage
        print(self.name, "attacks", target.name, "and deals", damage)