from Type import Type

class WaterType(Type):

    def __init__(self):
        super().__init__(
            id=2,
            name="Water",
            color="#F08030",
            description="Water type Pokémon are known for their adaptability and versatility in battle. They often have moves that involve water-based attacks and can thrive in aquatic environments.",
            typeBound=1,
            classBound=1,
            typechart=None
        )

