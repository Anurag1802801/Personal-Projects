class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Board:
    def __init__(self):
        self.cells = [' '] * 9

    def display(self):
        print("\n")
        for row in range(3):
            print(" " + " | ".join(self.cells[row*3:(row+1)*3]))
            if row < 2:
                print("---|---|---")
        print("\n")

    def update_cell(self, index, symbol):
        if self.cells[index] == ' ':
            self.cells[index] = symbol
            return True
        return False

    def is_full(self):
        return ' ' not in self.cells

    def check_winner(self, symbol):
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for combo in win_combinations:
            if all(self.cells[i] == symbol for i in combo):
                return True
        return False

    def reset(self):
        self.cells = [' '] * 9


class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")
        self.current_player = self.player1

    def switch_player(self):
        self.current_player = (
            self.player1 if self.current_player == self.player2 else self.player2
        )

    def play(self):
        print("=== Welcome to Tic-Tac-Toe ===")
        self.board.display()

        while True:
            try:
                move = int(input(f"{self.current_player.name} ({self.current_player.symbol}), choose a position (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Invalid input. Choose a number between 1 and 9.")
                    continue

                if not self.board.update_cell(move, self.current_player.symbol):
                    print("That cell is already taken. Try again.")
                    continue

                self.board.display()

                if self.board.check_winner(self.current_player.symbol):
                    print(f" {self.current_player.name} wins!")
                    break

                if self.board.is_full():
                    print("It's a draw!")
                    break

                self.switch_player()

            except ValueError:
                print("Invalid input. Please enter a number.")

        print("Game over.")


if __name__ == "__main__":
    game = Game()
    game.play()
