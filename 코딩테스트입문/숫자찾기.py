def solution(num, k):
    if str(k) in str(num):
        answer = str(num).index(str(k))+1
    else:
        answer = -1
    return answer

print(solution(29183,1))