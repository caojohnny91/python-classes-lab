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
        self.render()
        while not self.winner and not self.tie:
            self.get_move()
            self.render()
            self.check_winner()
            self.switch_turn()

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
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        # Start an infinite loop
        while True:
            # Ask the user to enter their move
            move = input("Enter a valid move (example: A1): ").lower()

            # Check if the move is a valid key on the board
            if move in self.board:
                # Check if the chosen spot is empty
                if self.board[move] is None:
                    # Update the board with the player's move
                    self.board[move] = self.turn
                    # Exit the loop
                    break
                else:
                    print("That spot is already taken. Try again.")
            else:
                print("Invalid move. Please enter a valid move.")

    def switch_turn(self):
        # Switch turn between 'X' and 'O'
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def check_winner(self):
        # This method will check for a winner or a tie
        pass


# Instantiate the Game class and invoke the play_game method
game_instance = Game()
game_instance.play_game()
