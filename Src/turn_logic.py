class TurnLogic:
    def __init__(self, players):
        self.players = players
        self.current_player_index = 0

    def get_current_player(self):
        return self.players[self.current_player_index]

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        return self.get_current_player()