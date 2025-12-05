from Monster import Monster

class WaterMonster(Monster):

    def __init__(self):
        super().__init__(
            id=1,
            name="AquaSerpent",
            type="WATER",
            health=120,
            attack_power=25,
            defense=15,
            speed=10,
            ability="Torrent",
            move_list=["Water Gun", "Bubble Beam", "Hydro Pump"]
        )