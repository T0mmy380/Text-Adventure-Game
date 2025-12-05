from Type import Type

class FireType(Type):

    def __init__(self):
        super().__init__(
            id=2,
            name="Fire",
            color="#F08030",
            description="Fire type Pokémon are known for their fiery abilities and strong offensive capabilities. They often have moves that involve flames and heat.",
            typeBound=2,
            classBound=2,
            typechart=None
        )