from Src.Types.TypeChart import TypeChart

class Type:

    def __init__(self,id: int,  name: str, color: str, description: str,typeBound: int, classBound: int, typechart):
        self.id = id
        self.name = name
        self.type = name
        self.colour = color
        self.description = description
        self.typeBound = typeBound
        self.classBound = classBound
        self.typechart = TypeChart()

    info = lambda self: \
        (f"Type ID: {self.id}"
         f"\nName: {self.name}"
         f"\nType: {self.type}"
         f"\nColor: {self.colour}"
         f"\nDescription: {self.description}"
         f"\nType Bound: {self.typeBound}"
         f"\nClass Bound: {self.classBound}")

    def show_info(info):
        for line in info.info().split('\n'):
            print(line)