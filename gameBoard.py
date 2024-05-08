class GameBoard:
    def __init__(self):
        self.board_size = 10
        self.ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
        self.players = []
        self.current_game = 0
        self.total_games = 0
        self.scores = {}

    def add_player(self, player):
        self.players.append(player)
        self.scores[player.name] = 0

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
                result = self.check_hit(player, move)
                player.receive_result(move, result)
                game_over = self.is_game_over()
                if game_over:
                    break

        self.update_scores()

    def check_hit(self, player, move):
        opponent = self.get_opponent(player)
        return opponent.board.receive_attack(move)

    def get_opponent(self, player):
        for p in self.players:
            if p != player:
                return p

    def is_game_over(self):
        # Implement logic to determine if the game is over
        return False

    def update_scores(self):
        for player in self.players:
            if player.has_won():
                self.scores[player.name] += 1
        print(f"Scores after game {self.current_game}: {self.scores}")

    def play_series(self, games):
        self.total_games = games
        for _ in range(games):
            self.setup_game()
            self.play_game()

class Player:
    def __init__(self, name):
        self.name = name
        self.board = None

    def place_ships(self):
        # Initialize board with ships
        pass

    def get_move(self):
        # Implement logic to determine next move
        pass

    def receive_result(self, move, result):
        # Receive the result of a move (hit/miss)
        pass

    def has_won(self):
        # Implement winning condition check
        pass
