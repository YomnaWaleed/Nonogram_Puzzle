import random

def generate_random_grid(size,puzzle,fill_probability=0.5):
    for i in range(size):
        for j in range(size):
            if random.random() >= 0.5:
                puzzle[i][j] = 1

def generate_puzzle_col(size, col_idx, puzzle, cols):
    cnt = 0
    for i in range(size):
        if cnt > 0 and puzzle[i][col_idx] == 0:
            cols[col_idx].append(cnt)
            cnt = 0
        elif puzzle[i][col_idx] == 1:
            cnt += 1

    if cnt > 0:
        cols[col_idx].append(cnt)

def generate_puzzle_row(size, row_idx, puzzle, rows):
    cnt = 0
    for i in range(size):
        if cnt > 0 and puzzle[row_idx][i] == 0:
            rows[row_idx].append(cnt)
            cnt = 0
        elif puzzle[row_idx][i] == 1:
            cnt += 1

    if cnt > 0:
        rows[row_idx].append(cnt)
