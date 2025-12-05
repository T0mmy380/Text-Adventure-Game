from Type import Type

class GrassType(Type):

    def __init__(self):
        super().__init__(
            id=0,
            name="Grass",
            color="#78C850",
            description="Grass type Pokémon are known for their connection to nature and plants. They often have abilities related to growth and healing.",
            typeBound=0,
            classBound=0,
            typechart=None  # Assuming typechart is handled elsewhere
        )

