class Monster:

    def __init__(self, mon_id, name, types, health, attack_power, defense, speed, ability, move_list):
        self.mon_id = mon_id
        self.name = name
        self.types = types                    
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed
        self.stat_mult = {
            'atk': 0,
            'def': 0,
            'spe': 0,
            'acc': 0,
            'eva': 0
        }
        self.status = []
        self.ability = ability                
        self.move_list = list(move_list)      

    def info(self) -> str:
        return (
            f"Monster ID: {self.mon_id}"
            f"\nName: {self.name}"
            f"\nTypes: {self.types}"
            f"\nHP: {self.health} ATK: {self.attack_power} DEF: {self.defense} SPE: {self.speed}"
            f"\nStat Multipliers: {self.stat_mult}"
            f"\nStatuses: {self.status}"
            f"\nAbility: {self.ability}"
            f"\nMoves: {', '.join(self.move_list)}"
        )

    def show_info(self):
        for line in self.info().split('\n'):
            print(line)

    def attack(self, target: "Monster"):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

    def is_alive(self) -> bool:
        return self.health > 0
    
    def stat_change(self, stat: str, stages: int):        

        if stat in self.stat_mult:
            self.stat_mult[stat] += stages
            print(f"{self.name}'s {stat} changed by {stages} stages.")
        else:
            print(f"Stat {stat} does not exist.")
        
        if self.stat_mult[stat] > 6:
            print(f"{self.name}'s {stat} can't go higher!")
            self.stat_mult[stat] = 6
        elif self.stat_mult[stat] < -6:
            print(f"{self.name}'s {stat} can't go lower!")
            self.stat_mult[stat] = -6
        
    def apply_status(self, status: str):
        if status not in self.status:
            self.status.append(status)
            print(f"{self.name} is now affected by {status}.")
        else:
            print(f"{self.name} is already affected by {status}.")
