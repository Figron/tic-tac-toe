import numpy as np
import datetime


class Player(object):
    """Class for players."""

    score = 0

    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name


class Game(object):
    """Class for game logic."""

    players = []
    tokens = ['x', 'o']
    victory = False
    turn_count = 0  # Adding a turn counter for draw

    def __init__(self):
        super(Game, self).__init__()

    def view_logs(self):
        with open('E:/Labs/Python/Data Engineers/Tictactoe/logs.txt', 'r') as file:
            for line in file:
                print(line)

    def delete_logs(self):
        open('E:/Labs/Python/Data Engineers/Tictactoe/logs.txt', 'w').close()

    def edit_logs(self, string):
        with open('E:/Labs/Python/Data Engineers/Tictactoe/logs.txt', 'a') as file:
            file.write(string)

    def play(self, board):
        board.reset_board()
        while 1:
            if self.victory is True or self.turn_count == 9:
                break
            for index, token in enumerate(self.tokens):

                # Make no mistakes, because everything will break
                move = int(input("Please make your move(1-9):"))

                if move == 1:
                    board.put_token([0, 0], token)
                elif move == 2:
                    board.put_token([0, 1], token)
                elif move == 3:
                    board.put_token([0, 2], token)
                elif move == 4:
                    board.put_token([1, 0], token)
                elif move == 5:
                    board.put_token([1, 1], token)
                elif move == 6:
                    board.put_token([1, 2], token)
                elif move == 7:
                    board.put_token([2, 0], token)
                elif move == 8:
                    board.put_token([2, 1], token)
                elif move == 9:
                    board.put_token([2, 2], token)

                board.view_board()
                self.victory = board.victory_check(self.players[index])

                if self.victory is True:
                    if self.players[index].score == 0:
                        self.edit_logs(str(datetime.datetime.now()) + " " + self.players[index].name + ' Wins!\n')
                    again = input("Would you like to play again, with the same players? y/n")
                    if again == 'y':
                        self.victory = False
                        self.players[index].score += 1
                        self.turn_count = 0
                        self.play(Board())
                        break
                    else:
                        if self.players[0].score > 0 or self.players[1].score > 0:
                            self.edit_logs(str(datetime.datetime.now()) + " " + self.players[0].name + " vs " + self.players[1].name + " " + str(self.players[0].score) + "-" + str(self.players[1].score))
                    break

                self.turn_count += 1
                if self.turn_count == 9 and self.victory is False:
                    self.edit_logs(str(datetime.datetime.now()) + " It's a draw!")
                    print("Nobody wins!")
                    break
    def init(self):
        print("Starting new game...")

        board = Board()

        player1 = Player(input('Enter your name'))
        player2 = Player(input('Enter your name'))
        self.players = [player1, player2]

        self.play(board)



class Board(object):
    """Class describing board board"""

    board = np.array([['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']])

    def reset_board(self):
        self.board = np.array([['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']])

    def view_board(self):
        print(self.board)

    def put_token(self, arr, token):
        """Put 'x' or 'o' on a board"""
        self.board[arr[0], arr[1]] = token

    def victory_check(self, player):
        """Check if rows, columns or diagonals are of the same token"""
        if self.board[0, 0] == self.board[0, 1] and self.board[0, 1] == self.board[0, 2] and self.board[0, 1] != '_':
            print(player.name + " Wins!")
            return True
        if self.board[0, 0] == self.board[1, 0] and self.board[1, 0] == self.board[2, 0] and self.board[1, 0] != '_':
            print(player.name + " Wins!")
            return True
        if self.board[0, 2] == self.board[1, 2] and self.board[1, 2] == self.board[2, 2] and self.board[1, 2] != '_':
            print(player.name + " Wins!")
            return True
        if self.board[2, 0] == self.board[2, 1] and self.board[2, 1] == self.board[2, 2] and self.board[2, 1] != '_':
            print(player.name + " Wins!")
            return True
        if self.board[0, 0] == self.board[1, 1] and self.board[1, 1] == self.board[2, 2] and self.board[1, 1] != '_':
            print(player.name + " Wins!")
            return True
        if self.board[2, 0] == self.board[1, 1] and self.board[1, 1] == self.board[0, 2] and self.board[1, 1] != '_':
            print(player.name + " Wins!")
            return True
        if self.board[1, 0] == self.board[1, 1] and self.board[1, 1] == self.board[1, 2] and self.board[1, 1] != '_':
            print(player.name + " Wins!")
            return True
        if self.board[0, 1] == self.board[1, 1] and self.board[1, 1] == self.board[2, 1] and self.board[1, 1] != '_':
            print(player.name + " Wins!")
            return True


def main():
    choice = int(input("Please select what you would like to do:"))
    print("1: Play a new board")
    print("2: View logs")
    print("3: Delete logs")
    print("4: Exit")

    game = Game()

    if choice == 1:
        game.init()
    elif choice == 2:
        print("Here are your logs:")
        game.view_logs()
    elif choice == 3:
        print("Deleting logs...")
        game.delete_logs()
    elif choice == 4:
        print("Goodbye!")
        exit()


if __name__ == "__main__":
    main()
