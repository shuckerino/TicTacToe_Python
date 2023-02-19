class TicTacToe:
    def __init__(self):
        self.board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        self.winner = ""

    # Printing game board
    def out(self):
        count = 0
        for x in self.board:
            if count == 3 or count == 6:
                print("\n")
            print(x + " | ", end="")
            count += 1
        print("\n")

    def set(self, p, player):
        self.board[p] = player

    def winV(self):
        if self.board[0] == self.board[3] == self.board[6] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        if self.board[1] == self.board[4] == self.board[7] and self.board[1] != "-":
            self.winner = self.board[1]
            return True
        if self.board[2] == self.board[5] == self.board[8] and self.board[2] != "-":
            self.winner = self.board[2]
            return True
        return False

    def winH(self):
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        if self.board[3] == self.board[4] == self.board[5] and self.board[3] != "-":
            self.winner = self.board[3]
            return True
        if self.board[6] == self.board[7] == self.board[8] and self.board[6] != "-":
            self.winner = self.board[6]
            return True
        return False

    def winD(self):
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        if self.board[6] == self.board[4] == self.board[2] and self.board[6] != "-":
            self.winner = self.board[6]
            return True
        return False


