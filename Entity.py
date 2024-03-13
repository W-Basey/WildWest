class Entity():
    def __init__(self):
        self.name = ""

        self.health = 3
        self.ammunition = 5
        self.currentDamage = 0

        self.statistics = {
            "max_health": 3,
            "dexterity": 1,
            "accuracy": 1,
            "speed": 1,
            "damage": 1,
            "strength": 1
        }
        self.attackList = ["Dodge", "Single-Shot", "Bullet Spray", "Brawl"]