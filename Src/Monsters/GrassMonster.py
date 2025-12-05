from Monster import Monster

class GrassMonster(Monster):

    def __init__(self):
        super().__init__(
            id=0,
            name="Leafy",
            type="Grass",
            health=100,
            attack_power=15,
            defense=10,
            speed=12
        )
