class Game:
    def __init__(self):
        self.turn = "X"
        self.tie = False
        self.winner = None
        self.board = {
            "a1": None,
            "b1": None,
            "c1": None,
            "a2": None,
            "b2": None,
            "c2": None,
            "a3": None,
            "b3": None,
            "c3": None,
        }

    def play_game(self):
        print("Welcome to the Game!")
        print("Let's get started!")
        self.render()  # Display the initial state

        while not self.winner and not self.tie:
            self.get_move()  # Get player input
            self.check_winner()  # Check if there's a winner
            self.render()  # Display the board and status
            if not self.winner:
                self.check_for_tie()  # Check if there's a tie
            if not self.winner and not self.tie:
                self.switch_turn()  # Switch turn if no winner or tie

        self.render()  # Display final game state

    def print_board(self):
        b = self.board
        print(
            f"""
        A   B   C
    1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
    2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
    3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
  """
        )

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(
                f"It's player {self.turn}'s turn!"
            )  # Ensure this prints the correct turn

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input("Enter a valid move (example: A1): ").lower()
            if move in self.board:
                if self.board[move] is None:
                    self.board[move] = self.turn
                    break
                else:
                    print("That spot is already taken. Try again.")
            else:
                print("Invalid move. Please enter a valid move.")

    def switch_turn(self):
        turn_lookup = {"X": "O", "O": "X"}
        self.turn = turn_lookup[self.turn]

    def check_winner(self):
        b = self.board
        # Check rows
        if b["a1"] and b["a1"] == b["b1"] == b["c1"]:
            self.winner = b["a1"]
        elif b["a2"] and b["a2"] == b["b2"] == b["c2"]:
            self.winner = b["a2"]
        elif b["a3"] and b["a3"] == b["b3"] == b["c3"]:
            self.winner = b["a3"]

        # Check columns
        elif b["a1"] and b["a1"] == b["a2"] == b["a3"]:
            self.winner = b["a1"]
        elif b["b1"] and b["b1"] == b["b2"] == b["b3"]:
            self.winner = b["b1"]
        elif b["c1"] and b["c1"] == b["c2"] == b["c3"]:
            self.winner = b["c1"]

        # Check diagonals
        elif b["a1"] and b["a1"] == b["b2"] == b["c3"]:
            self.winner = b["a1"]
        elif b["c1"] and b["c1"] == b["b2"] == b["a3"]:
            self.winner = b["c1"]

    def check_for_tie(self):
        if all(value is not None for value in self.board.values()) and not self.winner:
            self.tie = True


game_instance = Game()
game_instance.play_game()
