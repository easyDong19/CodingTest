def solution(array):
    answer = [max(array),array.index(max(array))]
    return answer

print(solution([1,8,3]))