class GameBoard:
    def __init__(self, players):
        self.players = players
        self.current_game = 0
        self.total_games = 0
        self.scores = {player.name: 0 for player in self.players}

    def setup_game(self):
        self.current_game += 1
        for player in self.players:
            player.place_ships()
        print(f"Game {self.current_game} start.")

    def play_game(self):
        game_over = False
        while not game_over:
            for player in self.players:
                move = player.get_move()
                opponent = self.get_opponent(player)
                result = opponent.receive_attack(move)
                player.receive_result(move, result)
                if self.is_game_over():
                    game_over = True
                    break

        self.update_scores()

    def get_opponent(self, player):
        for p in self.players:
            if p != player:
                return p

    def is_game_over(self):
        # The game is over when one player has no ships left
        for player in self.players:
            if player.has_won():
                return True
        return False

    def update_scores(self):
        # Only the winner gets a point
        for player in self.players:
            if player.has_won():  # Ensure this function checks if the opponent's ships are all hit
                self.scores[player.name] += 1
        print(f"Scores after game {self.current_game}: {self.scores}")

    def play_series(self, games):
        self.total_games = games
        for _ in range(games):
            self.setup_game()
            self.play_game()
