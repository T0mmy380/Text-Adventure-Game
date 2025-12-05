class TypeChart:

    Enum = {
        "NORMAL": 0,
        "FIRE": 1,
        "WATER": 2,
        "ELECTRIC": 3,
        "GRASS": 4,
        "ICE": 5,
        "FIGHTING": 6,
        "POISON": 7,
        "GROUND": 8,
        "FLYING": 9,
        "PSYCHIC": 10,
        "BUG": 11,
        "ROCK": 12,
        "GHOST": 13,
        "DRAGON": 14,
        "DARK": 15,
        "STEEL": 16,
        "FAIRY": 17
    }
    Effectiveness = [
        #|NOR|FIR|WAT|ELE|GRA|ICE|FIG|POI|GRO|FLY|PSY|BUG|ROC|GHO|DRA|DAR|STE|FAI|#
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5, 1],  # NORMAL
        [1, 0.5,0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 2, 1],  # FIRE
        [1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 1, 1],  # WATER
        [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1, 1, 1],  # ELECTRIC
        [1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5, 1],  # GRASS
        [1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0.5, 1],  # ICE
        [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2, 0.5],  # FIGHTING
        [1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 0, 2],  # POISON
        [1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2, 1],  # GROUND
        [1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0.5, 1],  # FLYING
        [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 0, 0.5, 1],  # PSYCHIC
        [1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5, 0.5],  # BUG
        [1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5, 1],  # ROCK
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 1],  # GHOST
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5, 0],  # DRAGON
        [1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 0.5],  # DARK
        [1, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5, 2],  # STEEL
        [1, 0.5, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 2, 0.5, 1]   # FAIRY   
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