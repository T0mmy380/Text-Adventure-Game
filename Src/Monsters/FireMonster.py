from Monster import Monster

class FireMonster(Monster):

    def __init__(self):
        super().__init__(
            id=2,
            name="Flamester",
            type="FIRE",
            health=80,
            attack_power=25,
            defense=15,
            speed=20
        )