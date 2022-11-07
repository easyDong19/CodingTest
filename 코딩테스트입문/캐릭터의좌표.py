

def solution(keyinput, board):
    direct = {
        "left": [-1, 0],
        "right": [1, 0],
        "up": [0, 1],
        "down": [0, -1],
    }
    answer = [0,0]
    max_width = board[0]//2
    max_height = board[1]//2

    for key in keyinput:
        if not abs(answer[0] + direct[key][0])>max_width:
            answer[0] += direct[key][0]
        if not abs(answer[1] + direct[key][1]) > max_height:
            answer[1] += direct[key][1]
    return answer
