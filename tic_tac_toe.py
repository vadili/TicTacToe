class TicTacToe:
    def __init__(self):
        self.board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        self.curr_player = "X"

    def check_rows(self):
        for row in self.board:
            if row == ["X"] * 3:
                return "X"
            elif row == ["O"] * 3:
                return "O"
        return False

    def check_cols(self):
        for i in range(3):
            col = [self.board[0][i], self.board[1][i], self.board[2][i]]
            if col == ["X"] * 3:
                return "X"
            elif col == ["O"] * 3:
                return "O"
        return False

    def check_diags(self):
        diag1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
        diag2 = [self.board[0][2], self.board[1][1], self.board[2][0]]
        diags = [diag1, diag2]

        for diag in diags:
            if diag == ["X"] * 3:
                return "X"
            elif diag == ["O"] * 3:
                return "O"
        return False

    def check_win(self):
        if self.check_rows():
            return self.check_rows()
        elif self.check_cols():
            return self.check_cols()
        elif self.check_diags():
            return self.check_diags()
        else:
            return False

    def free_spots(self):
        free = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "_":
                    free.append((i, j))
        return free

    def make_move(self, row, col):
        if (row, col) in self.free_spots():
            self.board[row][col] = self.curr_player
            if self.curr_player == "X":
                self.curr_player = "O"
            elif self.curr_player == "O":
                self.curr_player = "X"
            return True
        return False

    def get_board(self):
        return self.board