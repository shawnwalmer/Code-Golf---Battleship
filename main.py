import sys
import importlib
from gameBoard import GameBoard

def load_player_module(module_name):
    """Dynamically import a player module based on the module name."""
    try:
        return importlib.import_module(module_name)
    except ImportError as e:
        print(f"Error importing {module_name}: {e}")
        sys.exit(1)

def create_player(module, player_name):
    """Create a player instance from a module."""
    if hasattr(module, 'Player'):
        return module.Player(player_name)
    else:
        print(f"Module {module} does not contain a Player class")
        sys.exit(1)

def main(player1_module, player2_module):
    # Load player modules
    player1 = load_player_module(player1_module)
    player2 = load_player_module(player2_module)

    # Create player instances
    player1_instance = create_player(player1, "Player 1")
    player2_instance = create_player(player2, "Player 2")

    # Initialize game board with players
    game_board = GameBoard([player1_instance, player2_instance])

    # Play a series of games
    num_games = 500  # or any other configuration
    game_board.play_series(num_games)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py player1_module player2_module")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
