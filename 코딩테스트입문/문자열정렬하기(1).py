def solution(my_string):
    arr = list(my_string)
    answer = []

    for i in arr:
        if i.isdigit():
            answer.append(int(i))

    answer.sort()
    return answer

print(solution("hi12392"))