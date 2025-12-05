class TypeChart:

    Enum = {
        "Grass" : 0,
        "Water" : 1,
        "Fire"  : 2,
    }
    Effectiveness = [
    #    G   W   F    #
        [1, 0.5, 2],  # Grass
        [2, 1, 0.5],  # Water
        [0.5, 2, 1],  # Fire
    ]

    def __init__(self, chart= None):
        # build chart from Effectiveness matrix if no chart provided
        if chart is None:
            self.chart = {}
            for attacker_name, i in TypeChart.Enum.items():
                row = TypeChart.Effectiveness[i]
                self.chart[attacker_name] = {}
                for defender_name, j in TypeChart.Enum.items():
                    self.chart[attacker_name][defender_name] = row[j]

    def set_effectiveness(self, attacker_type: str, defender_type: str, multiplier: float):
        if attacker_type not in self.chart:
            self.chart[attacker_type] = {}
        self.chart[attacker_type][defender_type] = multiplier

    def get_effectiveness(self, attacker_type: str, defender_type: str) -> float:
        return self.chart.get(attacker_type, {}).get(defender_type, 1.0)

    def get_types(self):
        print(TypeChart.Enum)