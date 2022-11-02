def solution(n):
    i = 1
    num = 1
    while True:
        i *= num
        if i > n: break
        num += 1

    answer = num
    return answer-1

