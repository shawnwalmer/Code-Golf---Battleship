import random

class Player:
    def __init__(self, name):
        self.name = name
        self.board = [['-' for _ in range(10)] for _ in range(10)]
        self.ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Destroyer': 3, 'Submarine': 2}
        self.enemy_attacks = [['-' for _ in range(10)] for _ in range(10)]

    def place_ships(self):
        for ship, size in self.ships.items():
            placed = False
            while not placed:
                vertical = random.choice([True, False])
                if vertical:
                    col = random.randint(0, 9)
                    row = random.randint(0, 10 - size)
                else:
                    row = random.randint(0, 9)
                    col = random.randint(0, 10 - size)

                if self.can_place_ship(row, col, size, vertical):
                    self.place_ship(row, col, size, vertical)
                    placed = True

    def can_place_ship(self, row, col, size, vertical):
        if vertical:
            return all(self.board[row + i][col] == '-' for i in range(size))
        else:
            return all(self.board[row][col + i] == '-' for i in range(size))

    def place_ship(self, row, col, size, vertical):
        if vertical:
            for i in range(size):
                self.board[row + i][col] = 'S'  # 'S' denotes a ship part
        else:
            for i in range(size):
                self.board[row][col + i] = 'S'

    def get_move(self):
        return random.randint(0, 9), random.randint(0, 9)

    def receive_result(self, move, result):
        x, y = move
        self.enemy_attacks[x][y] = 'H' if result else 'M'

    def receive_attack(self, move):
        x, y = move
        if self.board[x][y] == 'S':
            self.board[x][y] = 'X'  # Mark as hit
            return True
        return False

    def has_won(self):
        return not any('S' in row for row in self.board)  # No 'S' means all ships are hit