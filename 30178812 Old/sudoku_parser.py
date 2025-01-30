class Sudoku:
    def __init__(self, raw):
        self.board = [raw[i:i+9] for i in range(0, len(raw), 9)]
        print(self.board)
        self.board = [list(self.board[i]) for i in range(0, 8)]
        print(self.board)
        self.board = [[int(self.board[i][x]) for x in range(len(self.board[0]))] for i in range(0, 8)]
        print(self.board)
    def get_row(self, index):
        return self.board[index]
    def get_col(self, index):
        return [self.board[i][index] for i in range(0, len(self.board[0]))]
    def get_sqr(self, sqr, index=3):
        pass
