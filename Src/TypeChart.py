class TypeChart:

    Enum = {
        "Grss" : 0,
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
        self.chart = chart or {}

    def set_effectiveness(self, attacker_type: str, defender_type: str, multiplier: float):
        if attacker_type not in self.chart:
            self.chart[attacker_type] = {}
        self.chart[attacker_type][defender_type] = multiplier

    def get_effectiveness(self, attacker_type: str, defender_type: str) -> float:
        return self.chart.get(attacker_type, {}).get(defender_type, 1.0)