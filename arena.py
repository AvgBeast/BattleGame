class Arena:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def fight(self):
        print("Fight starts!")

        while self.first.hp > 0 and self.second.hp > 0:
            
            input("Press ENTER for next attack")
            self.first.attack(self.second)
            print(self.second.name, "HP =", self.second.hp)
            print()

            if self.second.hp <= 0:
                break

            input("Press ENTER for next attack")
            self.second.attack(self.first)
            print(self.first.name, "HP =", self.first.hp)
            print()

        print("Fight is over!")
        if self.first.hp <= 0:
            print(self.first.name, "is defeated!")
        else:
            print(self.second.name, "is defeated!")