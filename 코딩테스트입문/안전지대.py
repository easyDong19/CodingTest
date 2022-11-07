def danger(n,i,j):
    if i<0 or i>=n or j<0 or j>=n:
        return False
    return True
def solution(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for danger_x in range(i-1,i+2):
                    for dange_y in range(j-1,j+2):
                        if danger(n,danger_x,dange_y):
                            if board[danger_x][dange_y] == 1: continue
                            board[danger_x][dange_y] = 2
    count = 0
    for i in board:
        for j in i:
            if j==0:
                count+=1
    return count


def smart_solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            #파이썬에서 0은 false
            if not x:
                continue
            #만약 1이라면 아래로직 실행
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)
