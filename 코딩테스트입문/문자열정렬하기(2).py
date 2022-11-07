def solution(my_string):
    answer = sorted(list(my_string.lower()))
    result = "".join(answer)
    return result

print(solution("Bcad"))

