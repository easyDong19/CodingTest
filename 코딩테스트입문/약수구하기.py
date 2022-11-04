import math
def solution(n):
    answer = []
    if n == 1: return [1]
    for i in range(1,int(math.sqrt(n)+1)):
        if n%i==0:
            answer.append(i)
            answer.append(n//i)
    return sorted(set(answer))

print(solution(4))