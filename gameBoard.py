class GameBoard:
    def __init__(self, players):
        self.winner = None
        self.players = players
        self.current_game = 0
        self.total_games = 0
        self.scores = {player.name: 0 for player in self.players}

    def validate_ships(self, player):
        # Count the number of ships on the player's board
        ship_count = sum(row.count('S') for row in player.board)

        # Sum the sizes of all ships in the fleet
        fleet_size = sum(player.ships.values())

        # Return True if the number of ships matches the fleet size, False otherwise
        return ship_count == fleet_size

    def setup_game(self):
        self.current_game += 1
        for player in self.players:
            player.place_ships()
        print(f"Game {self.current_game} start.")

    def play_game(self):
        # Validate ships for each player before starting the game
        for player in self.players:
            if not self.validate_ships(player):
                print(f"{player.name} has not placed the correct number of ships. Game aborted.")
                return False

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
        return True

    def get_opponent(self, player):
        for p in self.players:
            if p != player:
                return p

    def is_game_over(self):
        # The game is over when one player has no ships left
        for player in self.players:
            if player.has_won():
                self.winner = player
                return True
        return False

    def update_scores(self):
        # Only the winner gets a point
        if self.winner:
            self.scores[self.winner.name] += 1
        print(f"Scores after game {self.current_game}: {self.scores}")

    def play_series(self, games):
        self.total_games = games
        for i in range(games):
            # Reverse the order of players at the start of each game
            self.players.reverse()
            self.setup_game()
            if not self.play_game():
                print("Series aborted due to incorrect ship placement.")
                break