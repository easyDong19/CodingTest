def solution(array, n):
    Min = 1000
    answer = 0

    array.sort()
    for i in array:
        if Min> abs(n-i):
            Min = abs(n-i)
            answer = i
    return answer

print(solution([3, 10, 28],20))
print(solution([10, 11, 12],13))