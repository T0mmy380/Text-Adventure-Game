
class MonsterDex:

    MONSTER_DEX = [

    ]

    @classmethod
    def list_monsters(cls):
        return {i: c.__name__ for i, c in enumerate(cls.MONSTER_DEX)}