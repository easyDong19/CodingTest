def solution(num_list, n):
    answer = []
    num = 0
    j = 0
    result = []
    for i in num_list:
        result.append(i)
        num+=1
        if num==n:
            j+=1
            num=0
            answer.append(result)
            result = []

    return answer

print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948],3))