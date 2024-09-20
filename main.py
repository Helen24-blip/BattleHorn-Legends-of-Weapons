from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "Смертельный удар мечом!"

class Bow(Weapon):
    def attack(self):
        return "Стрела в цель!"

class ВattleAxe(Weapon):
    def attack(self):
        return "Нанесение раны топором!"


class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def attack(self):
        return f"{self.name} атакует: {self.weapon.attack()}"


class Monster:
    def __init__(self, name,):
        self.name = name


def battle(fighter: Fighter, monster: Monster):
    print(f"{fighter.name} сражается с {monster.name}!")
    print(f"{fighter.name} атакует {weapon.attack})
    print(f"{monster.name} побежден ")


if __name__ == "__main__":
    sword = Sword()
    bow = Bow()
    battleaxe = ВattleAxe()

    fighter = Fighter("Богатырь", sword)
    monster = Monster("Злобный монстр")

    battle(fighter, monster)

    # Смена оружия
    fighter.change_weapon(bow)
    battle(fighter, monster)

    fighter.change_weapon(battleaxe)
    battle(fighter, monster)

