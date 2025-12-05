from Src.TypeChart import TypeChart

class Type:
    def __init__(self,id: int,  name: str, color: str, description: str,typeBound: int, classBound: int):
        self.id = id
        self.name = name
        self.colour = color
        self.description = description
        self.typeBound = typeBound
        self.classBound = classBound

