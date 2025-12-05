class Type:

    def __init__(self,id: int,  name: str, color: str, description: str,typeBound: int, classBound: int, typechart):
        self.id = id
        self.name = name
        self.colour = color
        self.description = description
        self.typeBound = typeBound
        self.classBound = classBound
        self.typechart = typechart

    info = lambda self: \
        (f"Type ID: {self.id}"
         f"\nName: {self.name}"
         f"\nColor: {self.colour}"
         f"\nDescription: {self.description}"
         f"\nType Bound: {self.typeBound}"
         f"\nClass Bound: {self.classBound}")

    def show_info(info):
        print(info)

    def get_weakness(self, attacker: str, deffender: str):
        return self.typechart.get_effectiveness(self, attacker, deffender)