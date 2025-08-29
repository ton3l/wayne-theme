"""Testing theme"""
class ArkhamAsylum():
    """A class representing the Arkham Asylum environment."""

    def __init__(self, enemy, weapon):
        self.enemy = enemy
        self.weapon = weapon

    def attack(self):
        """Attack method"""
        return f"{self.enemy} attacked using a {self.weapon}"

    def defend(self):
        """Defend method"""
        return f"{self.enemy} defended against the attack with a {self.weapon}"

joker = ArkhamAsylum('Joker', 'Knife')
joker.attack()
joker.defend()
