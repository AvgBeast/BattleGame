from gears.weapon import Weapon
from gears.armor import Armor
from characters.barbarian import Barbarian
from characters.wizard import Wizard, Spell
from arena import Arena

#weapons
sword = Weapon("Sword", 10)
axe = Weapon("Axe", 12)
#armors
tshirt = Armor("T-Shirt", 2)
iron = Armor("Iron Armor", 5)
#Spells
fireball = Spell("Fireball", 15, 5)
#Characters
john = Barbarian("John", 100, sword, tshirt)
jane = Wizard("Jane", 100, axe, iron, 20, [fireball])
#Arena
arena = Arena(john, jane)
arena.fight()