class Solve:
    def __init__(self, size = 5, rows =[[]], cols =[[]]):
        self.size = size
        self.rows = rows
        self.cols = cols
        self.puzzle = [[0 for _ in range(size)] for _ in range(size)]
        self.solved = False

    def solve(self):
        return self.backtrack(0, 0)

    def backtrack(self, row , col):
        if row == self.size:  # if we have filled all cells
            return self.is_valid()

        next_row, next_col = (row, col + 1) if col < self.size - 1 else (row + 1, 0)

        for value in [1, 0]:
            self.puzzle[row][col] = value
            if self.is_partial_valid(row, col):
                if self.backtrack(next_row, next_col):
                    return True
            self.puzzle[row][col] = 0  # backtrack

        return False

    def is_valid(self):
        """
        Checks if the current state of the puzzle is valid
        :return: True if the entire puzzle is valid, False otherwise
        """
        for i in range(self.size):
            if self.get_run_length(self.puzzle[i]) != self.rows[i]:
                return False
            if self.get_run_length([self.puzzle[j][i] for j in range(self.size)]) != self.cols[i]:
                return False
        return True

    def is_partial_valid(self, row, col):
        """
        Checks if the current state in the backtracking case is valid or not
        :param row: the row index that was just filled
        :param col: the column index that was just filled
        """
        # Get the filled cells in the current row up to the current column
        current_row = self.puzzle[row][:col + 1]
        # Get the filled cells in the current column up to the current row
        current_col = [self.puzzle[i][col] for i in range(row + 1)]

        # Check if the filled cells in the current row match the row clue up to the current length
        if col == self.size - 1:  # If we are at the end of the row
            if self.get_run_length(current_row) != self.rows[row]:
                return False
        else:
            if not self.is_partial_clue_valid(current_row, self.rows[row]):
                return False

        # Check if the filled cells in the current column match the column clue up to the current length
        if row == self.size - 1:  # If we are at the end of the column
            if self.get_run_length(current_col) != self.cols[col]:
                return False
        else:
            if not self.is_partial_clue_valid(current_col, self.cols[col]):
                return False

        # If both checks pass, the current state is valid
        return True

    def is_partial_clue_valid(self, line, clues):
        """
        Checks if the partial line matches the given clues
        :param line: the current partial line (row or column)
        :param clues: the clues for the full line
        :return: True if the line can be valid given the clues, False otherwise
        """
        #[,1,1,0,0,1]  2 , 1
        runs = self.get_run_length(line)  #[1,1,0,]  2
        clues = clues[:len(runs)]  # Truncate clues to match runs length  [1,1,0,0,1] -- [2,1]    2

        # Check if the number of runs exceeds the number of clues
        if len(runs) > len(clues):
            return False

        # Check if the total run length doesn't exceed the clue sum
        if sum(runs) > sum(clues):
            return False

        for run, clue in zip(runs, clues):
            if run > clue:
                return False

        return True

    def get_run_length(self, line):
        runs, current_run = [], 0
        for cell in line + [0]:  # Sentinel to end the last run
            if cell == 1:
                current_run += 1
            else:
                if current_run:
                    runs.append(current_run)
                current_run = 0
        return runs