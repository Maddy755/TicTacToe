def check_winner(board, player):

    for i in range(3):
        # Row and Column Check
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
        # Diagonal Check
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def print_board(board):
    # Printing board after each turn
    print("Current Board:")
    for row in board:
        print("|".join(row))
        print("-" * 5)


def bot_ai(board, opponent):
    player = "X" if opponent == "O" else "O"

    # Check winning moves
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = opponent
                if check_winner(board, opponent):
                    return (i, j)
                board[i][j] = " "
    # Blocks opponent's winning moves
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X" if opponent == "O" else "O"
                if check_winner(board, "X" if opponent == "O" else "O"):
                    return (i, j)
                board[i][j] = " "
    # Block opponet forks
    for i in range(3):
        for j in range(3):
            count1 = 0
            if board[i][j] == " ":
                board[i][j] = player
                for x in range(3):
                    for y in range(3):
                        if board[x][y] == " ":
                            board[x][y] = player
                            if check_winner(board, player):
                                count1 += 1
                            board[x][y] = " "
                board[i][j] = " "
            if count1 >= 2:
                if board[0][1] == " ":
                    return (0, 1)
                elif board[1][0] == " ":
                    return (1, 0)
                elif board[1][2] == " ":
                    return (1, 2)
                elif board[2][1] == " ":
                    return (2, 1)

    # Scans for potential forks
    for i in range(3):
        for j in range(3):
            count = 0
            if board[i][j] == " ":
                board[i][j] = opponent
                for x in range(3):
                    for y in range(3):
                        if board[x][y] == " ":
                            board[x][y] = opponent
                            if check_winner(board, opponent):
                                count += 1
                            board[x][y] = " "
                board[i][j] = " "
    if count >= 2:
        return (i, j)
    # When no blocks or wins are available
    if board[1][1] == " ":
        return (1, 1)

    if opponent == "X":
        if board[1][1] == "O":
            if board[0][0] == " ":
                return (0, 0)
            elif board[2][2] == " ":
                return (2, 2)
            elif board[0][2] == " ":
                return (0, 2)
            elif board[2][0] == " ":
                return (2, 0)

    else:
        if board[1][1] == "X":
            if board[0][0] == " ":
                return (0, 0)
            elif board[2][2] == " ":
                return (2, 2)
            elif board[0][2] == " ":
                return (0, 2)
            elif board[2][0] == " ":
                return (2, 0)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return (i, j)


class game:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.player = input("Enter X or O:) ").upper()
        if self.player not in ["X", "O"]:
            print("Invalid input. Please enter X or O.")
            return
        if self.player == "X":
            self.turn = self.player
            self.opponent = "O"
        else:
            self.opponent = "X"
            self.turn = self.opponent
        self.play()

    def play(self):
        while True:
            print_board(self.board)
            if self.turn == self.player:
                row = int(input("Enter row 0-2:"))
                col = int(input("Enter column 0-2:"))
                if self.board[row][col] != " ":
                    print("Invalid input")
                    return
                self.board[row][col] = self.player
                self.turn = self.opponent

                if check_winner(self.board, self.player):
                    print(self.player + "wins!")
                    break

                if all(
                    self.board[i][j] != " " for i in range(3) for j in range(3)
                ):
                    print("It's a draw!")
                    break

            else:

                print("Bot is thinking...")
                move = bot_ai(self.board, self.opponent)
                if move:
                    self.board[move[0]][move[1]] = self.opponent
                    self.turn = self.player

                    if check_winner(self.board, self.opponent):
                        print(self.opponent + " wins!")
                        break

                    if all(
                        self.board[i][j] != " "
                        for i in range(3)
                        for j in range(3)
                    ):
                        print("It's a draw!")
                        break

                else:
                    print("No valid moves left.")
                    return


Game = game()
Game.play()
