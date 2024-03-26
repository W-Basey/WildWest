class Entity():
    def __init__(self):
        self.name = ""

        self.health = 3
        self.ammunition = 5
        self.clip = 3
        self.currentDamage = 0

        self.statistics = {
            "max_health": 3,
            "dexterity": 1,
            "accuracy": 1,
            "speed": 1,
            "damage": 1,
            "strength": 1,
            "clip_size": 3
        }
        self.attackList = ["Dodge", "Single-Shot", "Bullet Spray", "Brawl"]

    def refresh(self):
        self.health = self.statistics.get('max_health')
        self.currentDamage = self.statistics.get('damage')
        self.clip = self.statistics.get('clip_size')
        print (f"refroosh Player Health: {self.health}/{self.statistics.get('max_health')}")