from Src.Monsters.FireMonster import FireMonster
from Src.Monsters.GrassMonster import GrassMonster
from Src.Monsters.WaterMonster import WaterMonster


class MonsterDex:

    MONSTER_DEX = [
        GrassMonster(),
        WaterMonster(),
        FireMonster()
    ]

    @classmethod
    def list_monsters(cls):
        return {i: c.__name__ for i, c in enumerate(cls.MONSTER_DEX)}