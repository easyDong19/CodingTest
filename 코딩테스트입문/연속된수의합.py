def solution(num, total):
    answer = []
    maxx = total

    if total==0:
        answer.append(0)
        for i in range(1,num//2+1):
            answer.append(i)
            answer.append(-i)

    while sum(answer) != total:
        answer = []
        for i in range(num):
            answer.append(maxx - i)
        maxx = maxx - 1

    return sorted(answer)

