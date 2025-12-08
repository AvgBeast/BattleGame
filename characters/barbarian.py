from characters.character import Character

class Barbarian(Character):
    def attack(self, target):
        print(self.name, "(Barbarian) attacks twice!")
        super().attack(target)
        super().attack(target)