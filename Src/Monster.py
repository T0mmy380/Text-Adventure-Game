class Monster:

    def __init__(self, id, name, types, health, attack_power, defense, speed, ability, move_list):
        self.id = id
        self.name = name
        self.types = types
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed
        self.stat_mult = {
            'atk': 0,
            'def': 0,
            'spe': 0
        }
        self.ability = None
        self.move_list = []

    info = lambda self: \
        (f"Monster ID: {self.id}"
         f"\nName: {self.name}"
         f"\nTypes: {self.types}"
         f"\nHP: {self.health} ATK: {self.attack_power} DEF: {self.defense} SPE: {self.speed}"
         f"\nAbility: {self.ability}"
         f"\nMoves: {', '.join(self.move_list)}")

    def show_info(self):
        for line in self.info().split('\n'):
            print(line)

    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0
    
    def stat_change(self, stat: str, stages: int):
        if stat in self.stat_mult:
            self.stat_mult[stat] += stages
            print(f"{self.name}'s {stat} changed by {stages} stages.")
        else:
            print(f"Stat {stat} does not exist.")