# classic grid path + DFS/backtracking problem
# --------------------------------------------
    # Board of N rows, M columns
    # Each cell has a digit (0–9)
    # You can move to 4 neighbors (up, down, left, right)
    # Cannot visit the same cell twice
    # Path length = 4 cells → 4 digits
    # Form the biggest 4-digit integer possible from any such path

# 🧠 Idea
# --------
# From every cell in the grid:
# Start DFS
# Walk exactly 4 steps
# Keep track of visited cells
# Build number along the path
# Track the maximum number formed

board1 = [
    [9, 1, 1, 0, 7],
    [1, 0, 2, 1, 0],
    [1, 9, 1, 1, 0]
]
# exp_result = 9121
board2 = [
    [1, 1, 1],
    [1, 3, 4],
    [1, 4, 3]
]
# exp_result = 4343

board3 = [0, 1, 5, 0, 0]
# exp_result = 1500

def solution(board):

    m = len(board)
    n = len(board[0])
    max_num = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(r, c, visited, current_num, depth):
        nonlocal max_num

        if depth == 4:
            max_num = max(max_num, current_num)
            return
        
        for dr, dc in directions:
            nr = r+dr
            nc = c+dc
            if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited:
                visited.add((nr, nc))
                dfs(nr, nc, visited, current_num*10+board[nr][nc], depth+1)
                visited.remove((nr, nc))

    for i in range(m):
        for j in range(n):
            visited = {(i,j)}
            dfs(i, j, visited, board[i][j], 1)
    return max_num


print(solution(board))