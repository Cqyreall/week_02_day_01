class Team:

    def __init__(self, team_name, team_players, team_coach):
        self.name = team_name
        self.players = team_players
        self.coach = team_coach
        self.points = 0
    
    def add_player(self, new_player):
        self.players.append(new_player)
    
    def has_player(self, players):
        for player in self.players:
            if player == players:
                return True
        return False
    
    def play_game(self, outcome):
        if outcome == True:
            self.points += 3
