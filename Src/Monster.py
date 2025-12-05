class Monster:

    def __init__(self, id, name, type, health, attack_power, defense, speed):
        self.id = id
        self.name = name
        self.type = type
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed


    info = lambda self: \
        (f"Monster ID: {self.id}"
         f"\nName: {self.name}"
         f"\nType: {self.type}"
         f"\nHealth: {self.health}"
         f"\nAttack Power: {self.attack_power}"
         f"\nDefense: {self.defense}")

    def show_info(self):
        for line in self.info().split('\n'):
            print(line)

    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0